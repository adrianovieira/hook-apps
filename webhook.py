# coding: utf-8
'''
App: Webhook
description: permitir hook de conversão pandoc em "documentos/artigos"
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
'''
from flask import Flask, render_template, request, json
import requests
import ConfigParser
import gitlab
import zipfile, StringIO
import os, subprocess

# Webhook packages: classes e metodos relacionados a verificações em artigos
import artigo
from webhookerror import WebhookError

'''
getConfig: obtem dados de configuracao do ambiente

abtidos dos arquivos:
webhook-dist.cfg - padrão para o "webhook" (obrigatório)
webhook.cfg - personalizado para o ambiente de trabalho/produção (opcional)
'''
def getConfig():
  Config = ConfigParser.ConfigParser()

  '''
  # obtem dados de configuracao padrao
  '''
  try:
    ok = Config.read(os.path.dirname(os.path.abspath(__file__))+'/webhook-dist.cfg')
    if not ok: raise
  except:
    app.log_message = "ERROR: trying to read dist-config file."
    return False

  app.setup['production'] = Config.get('enviroment', 'production')
  app.setup['gitlab_host'] = Config.get('enviroment', 'gitlab_host')
  app.setup['gitlab_url'] = Config.get('enviroment', 'gitlab_url')
  app.setup['gitlab_url_download'] = Config.get('enviroment', 'gitlab_url_download')
  app.setup['gitlab_target_branch'] = Config.get('enviroment', 'gitlab_target_branch')
  app.setup['gitlab_webhook_user'] = Config.get('enviroment', 'gitlab_webhook_user')
  app.setup['gitlab_webhook_pass'] = Config.get('enviroment', 'gitlab_webhook_pass')
  app.setup['path_template'] = Config.get('enviroment', 'path_template')
  app.setup['path_tmp'] = Config.get('enviroment', 'path_tmp')
  app.setup['pandoc'] = Config.get('enviroment', 'pandoc')
  app.setup['make'] = Config.get('enviroment', 'make')
  app.setup['DEBUG'] = Config.get('enviroment', 'DEBUG')
  app.setup['DEBUG_LEVEL'] = Config.get('enviroment', 'DEBUG_LEVEL')
  app.setup['DEBUG_HOST'] = Config.get('enviroment', 'DEBUG_HOST')
  app.setup['DEBUG_PORT'] = int(Config.get('enviroment', 'DEBUG_PORT'))

  '''
  obtem dados de configuracao personalizados
  '''
  try:
    ok = Config.read(os.path.dirname(os.path.abspath(__file__))+'/webhook.cfg')
    if not ok: raise
    if Config.get('enviroment', 'production'):
      app.setup['production'] = Config.get('enviroment', 'production')
    if Config.get('enviroment', 'gitlab_host'):
      app.setup['gitlab_host'] = Config.get('enviroment', 'gitlab_host')
    if Config.get('enviroment', 'gitlab_webhook_user'):
      app.setup['gitlab_webhook_user'] = Config.get('enviroment', 'gitlab_webhook_user')
    if Config.get('enviroment', 'gitlab_webhook_pass'):
      app.setup['gitlab_webhook_pass'] = Config.get('enviroment', 'gitlab_webhook_pass')
    if Config.get('enviroment', 'gitlab_url'):
      app.setup['gitlab_url'] = Config.get('enviroment', 'gitlab_url')
    if Config.get('enviroment', 'gitlab_url_download'):
      app.setup['gitlab_url_download'] = Config.get('enviroment', 'gitlab_url_download')
    if Config.get('enviroment', 'gitlab_target_branch'):
      app.setup['gitlab_target_branch'] = Config.get('enviroment', 'gitlab_target_branch')
    if Config.get('enviroment', 'path_template'):
      app.setup['path_template'] = Config.get('enviroment', 'path_template')
    if Config.get('enviroment', 'path_tmp'):
      app.setup['path_tmp'] = Config.get('enviroment', 'path_tmp')
    if Config.get('enviroment', 'pandoc'):
      app.setup['pandoc'] = Config.get('enviroment', 'pandoc')
    if Config.get('enviroment', 'make'):
      app.setup['make'] = Config.get('enviroment', 'make')
    if Config.get('enviroment', 'DEBUG'):
      app.setup['DEBUG'] = Config.get('enviroment', 'DEBUG')
    if Config.get('enviroment', 'DEBUG_LEVEL'):
      app.setup['DEBUG_LEVEL'] = Config.get('enviroment', 'DEBUG_LEVEL')
    if Config.get('enviroment', 'DEBUG_HOST'):
      app.setup['DEBUG_HOST'] = Config.get('enviroment', 'DEBUG_HOST')
    if Config.get('enviroment', 'DEBUG_PORT'):
      app.setup['DEBUG_PORT'] = int(Config.get('enviroment', 'DEBUG_PORT'))
  except:
    app.log_message = "WARNING: can't read custom-config file."
    print app.log_message
    pass

  return True

'''
CONTANTES
avaliar "modulo: logging"
'''
DEBUG_LEVEL0 = 0
DEBUG_LEVEL1 = 1 # mostra algumas mensagens na console
DEBUG_INTERATIVO = 9 # ipdb ativado: "ipdb.set_trace()"

'''
Gitlab status and merge_status
constantes para comparação com o webhook
'''
GL_STATE = {
   'CLOSED':'closed',
   'OPENED':'opened',
   'REOPENED':'reopened'
   }

GL_STATUS = {
   'merge_request':'merge_request',
   'cannot_be_merged':'cannot_be_merged',
   'can_be_merged':'can_be_merged',
   'unchecked':'unchecked'
   }

'''
Inicia aplicação
'''
def __app_init():
    global app
    app = Flask(__name__)
    app.setup = {} # global de configuracao
    if not getConfig(): # obtem dados de configuracao inicial
       print app.log_message #"ERROR: trying to read dist-config file."

    if app.setup['production'] == 'False': # para devel ou testes
       if app.setup['DEBUG'] == 'True':
          app.debug = True

    return app

app = __app_init()

@app.route('/',methods=['GET', 'POST'])
def index():

  if request.method == 'GET':
    return 'Aplicacao para webhook! \n Use adequadamente!'

  elif request.method == 'POST':

    # abtem dados do webhook gitlab
    webhook_data = json.loads(request.data)
    app.setup['webhook_host_url'] = request.host_url

    if app.debug: print webhook_data

    # abre conexao com servidor gitlab
    try:
      app.gitlab = gitlab.Gitlab(app.setup['gitlab_host'])
      if not hasattr(app, 'gitlab'): raise
    except:
      app.log_message = "ERROR: trying to set gitlab url."
      if app.debug: print app.log_message
      return '{"status": "'+app.log_message+'"}'

    # autentica no servidor gitlab
    try:
      ok = app.gitlab.login(app.setup['gitlab_webhook_user'], app.setup['gitlab_webhook_pass'])
      if not ok: raise
    except:
      app.log_message = "ERROR: trying to set gitlab user/pass; or gitlab_host error."
      if app.debug: print app.log_message
      return '{"status": "'+app.log_message+'"}'

    # avalia webhook iniciado pelo gitlab
    try:
      app.log_message = "not a merge request"
      if webhook_data['object_kind'] or webhook_data['object_attributes']:
        if webhook_data['object_kind'] != GL_STATUS['merge_request']:
          raise

        if webhook_data['object_attributes']:
          if webhook_data['object_attributes']['target_branch'] != app.setup['gitlab_target_branch']:
            app.log_message = "target branch not allowed"
            raise

          if webhook_data['object_attributes']['state'] == GL_STATE['REOPENED']:
            app.log_message = "reopen not allowed for a merge request"
            raise # não trata reopened, pois esse modo não inclui novos commits

          if webhook_data['object_attributes']['state'] == GL_STATE['OPENED']:
            if webhook_data['object_attributes']['merge_status'] == GL_STATUS['cannot_be_merged']:
              app.log_message = "cannot be merged"

              app.gitlab.addcommenttomergerequest(webhook_data['object_attributes']['target_project_id'], \
                        webhook_data['object_attributes']['id'], \
                        '***merge request* não aceito**. Verique *branch* e solicite novamente!')
              raise # caso nao possa ser feito merge via gitlab "merge request invalido"

            if webhook_data['object_attributes']['merge_status'] == GL_STATUS['unchecked']:
              app.log_message = "merge request "+webhook_data['object_attributes']['state']+\
                               " - "+webhook_data['object_attributes']['merge_status']
              # raise
          else:
            app.log_message = "merge request "+webhook_data['object_attributes']['state']+\
                             " - "+webhook_data['object_attributes']['merge_status']
            raise

    except: # array IndexError: ou caso nao seja "merge_request"
        status = '{"status": "ERROR", "message": "'+app.log_message+'"}'
        if app.debug: print 'Aplicacao webhook para "Merge Request"! \n Use adequadamente!'
        if app.debug: print "ERROR: "+app.log_message
        return status

    # processa o webhook para "merge request"
    status = '{"status": "nOK"}'
    app.log_message = '{"type": "WARNING", "message": "processing"}'
    if webhook_data['object_attributes']['state'] == GL_STATE['OPENED'] and \
       (webhook_data['object_attributes']['merge_status'] == GL_STATUS['can_be_merged'] or \
       webhook_data['object_attributes']['merge_status'] == GL_STATUS['unchecked']):
      if app.debug: print "\nProcessing merge request to build PDF...\n"
      if app.debug: print app.log_message

      # simples adição de comentário ao merge request
      if app.debug:  app.gitlab.addcommenttomergerequest( \
                                          webhook_data['object_attributes']['target_project_id'], \
                                          webhook_data['object_attributes']['id'], \
                                          'Processando *merge request* para gerar PDF...[*'+ \
                                          webhook_data['object_attributes']['merge_status']+'*]')

      # obtem do repositório a branch a converter para PDF
      try:
          # instancia BranchDownloadZip
          artigo_downloadzip = artigo.BranchDownloadZip(
                                          app.setup['gitlab_url'],
                                          app.setup['gitlab_webhook_user'],
                                          app.setup['gitlab_webhook_pass'],
                                          app.setup['path_tmp'],
                                          app.gitlab, app.logger, app.debug)

          artigoDownload_zip_OK = artigo_downloadzip.branchDownload_zip(
                                webhook_data['object_attributes']['target_project_id'],
                                webhook_data['object_attributes']['id'],
                                webhook_data['object_attributes']['source_branch'])
          artigoDownload_unzip_OK = True

      except WebhookError as erro:
          artigoDownload_unzip_OK = False
          app.logger.warning(erro.logging())
          return 'artigo BranchDownloadZip! Erro: %s.'%erro+'\n'

      if artigoDownload_unzip_OK:

        # realisar verificação de metadados de autor e referencias bibliograficas
        # dados para parser de artigo
        # diretorio e nome de artigo == branch (do merge request)
        repo_name = str.split(app.setup['gitlab_url'], '/')
        repo_name = str.split(app.setup['gitlab_url'], '/')[len(repo_name)-1]
        zip_member_artigo_dir = repo_name+'.git/'+webhook_data['object_attributes']['source_branch']+'/'
        zip_member_artigo_name = zip_member_artigo_dir+webhook_data['object_attributes']['source_branch']+'.md'

        branch_info = app.gitlab.getrepositorybranch(webhook_data['object_attributes']['target_project_id'], webhook_data['object_attributes']['source_branch'])
        path_zip_extract = '%s/%s'%(app.setup['path_tmp'], branch_info['commit']['id'])

        app.artigo_branch_id = branch_info['commit']['id']
        app.artigo_path = path_zip_extract +'/'+ zip_member_artigo_dir
        app.artigo_name = webhook_data['object_attributes']['source_branch']

        if app.debug: print "\nRealisando verificação de metadados de autor e referencias bibliograficas do artigo...\n"

        metadados_msg = 'O ***PDF*** não foi gerado pois foram encontrados problemas no artigo. <br />Na estrutura base há grupos de dados (metadados) que contêm atributos para facilitar a formatação do artigo. Esta estrutura está disponível em <http://www-git/documentos/artigos/blob/master/estrutura-para-criar-artigos-tecnicos/Estrutura_e_metodo_padrao_para_criar_artigos.md#estrutura-padr-o-para-criar-artigos>. Foi percebida a ausência do(s) grupo(s) de dado(s) a seguir:  \n'
        has_dados_autor = True
        artigo_verifica_metadados = artigo.VerificaMetadados(app.artigo_path+app.artigo_name+'.md')
        if not artigo_verifica_metadados.hasDadosAutor():
          has_dados_autor = False
          metadados_msg += '- **Metadados de autor**: Grupo de dados a ser usado para identificar o artigo  \n'

        has_dados_referencias = True
        if not artigo_verifica_metadados.hasDadosReferencias():
          has_dados_referencias = False
          metadados_msg += '- **Metadados de referências**: Grupo de dados a ser usado em citações e referências bibliográficas. Detalhes no uso de citações em: <http://www-git/documentos/artigos/blob/master/crie-conteudo-nao-leiaute/crie-conteudo-nao-leiaute.md#cita-es-de-autores-refer-ncias-bibliogr-ficas>  \n'

        if (not has_dados_autor) or (not has_dados_referencias):
          status = '{"status": "notOK"}'
          app.gitlab.addcommenttomergerequest(webhook_data['object_attributes']['target_project_id'], \
                                              webhook_data['object_attributes']['id'], \
                                              metadados_msg)

        # realisar verificação de topicos base do artigo
        if app.debug: print "\nRealisando verificação de topicos base do artigo...\n"

        topicos_base_msg = 'O ***PDF*** não foi gerado pois foram encontrados problemas no artigo. <br />Uma estrutura base facilita ao leitor se localizar na leitura dos artigos. Neste sentido, foi definida uma estrutura base para os artigos que está disponível em <http://www-git/documentos/artigos/blob/master/estrutura-para-criar-artigos-tecnicos/Estrutura_e_metodo_padrao_para_criar_artigos.md#estrutura-padr-o-para-criar-artigos>. Foi percebida a ausência do(s) tópico(s) a seguir:  \n'
        has_topicos_base = True
        artigo_verifica_topicosbase = artigo.VerificaTopicosBase(app.artigo_path+app.artigo_name+'.md')
        if not artigo_verifica_topicosbase.hasIntroducao():
          has_topicos_base = False
          topicos_base_msg += '- **Introdução**: Descreve e contextualiza o conteúdo que o artigo irá abordar atraindo a sua leitura  \n'
        if not artigo_verifica_topicosbase.hasDesafios():
          has_topicos_base = False
          topicos_base_msg += '- **Desafios**: Descreve desafios e/ou problemas que o artigo irá abordar e buscar resolver  \n'
        if not artigo_verifica_topicosbase.hasBeneficios():
          has_topicos_base = False
          topicos_base_msg += '- **Benefícios e/ou recomendações**: Descreve os principais ganhos propostos pelo artigo, como melhoria de indicadores, processo de trabalho, etc  \n'
        if not artigo_verifica_topicosbase.hasConclusao():
          has_topicos_base = False
          topicos_base_msg += '- **Conclusão**: Apresenta o fechamento do artigo  \n'
        if not artigo_verifica_topicosbase.hasReferencias():
          has_topicos_base = False
          topicos_base_msg += '- **Referências**: Lista de referências bibliográficas, matérias na intranet, documentos ou ferramentas internas etc  \n'
        if not has_topicos_base:
          status = '{"status": "notOK"}'
          app.gitlab.addcommenttomergerequest(webhook_data['object_attributes']['target_project_id'], \
                                              webhook_data['object_attributes']['id'], \
                                              topicos_base_msg)

        if (has_topicos_base) and (has_dados_autor) and (has_dados_referencias):
            # realisar a conversao de artigo para PDF
            if app.debug: print "\nRealisando a conversao de artigo para PDF...\n"
            try:
                artigo_parser = artigo.PandocParser(app.setup['path_template'],
                                                    app.setup['path_tmp'],
                                                    app.setup['webhook_host_url'],
                                                    app.setup['gitlab_url_download'],
                                                    app.gitlab, app.logger,
                                                    app.debug)

                if artigo_parser.pandocParser(webhook_data['object_attributes']['target_project_id'],
                                              webhook_data['object_attributes']['id'],
                                              app.artigo_branch_id,
                                              app.artigo_path, app.artigo_name):
                  status = '{"status": "OK"}'
                else:
                  status = '{"status": "notOK"}'

            except WebhookError as erro:
                app.logger.warning(erro.logging())
                return 'artigo PandocParser! Erro em parser: "%s".'%erro+'\n'

      else:
        status = '{"status": "notOK"}'

    return status

# trata erro http/500, mesmo quando em modo debug=true
@app.errorhandler(500)
def internal_error(error):

    return '{"status": "500 error"}'

@app.route('/about',methods=['GET'])
def about():

    webhook_version = 'VERSION'
    try:
       f = open(os.path.dirname(os.path.abspath(__file__))+'/VERSION')
       webhook_version = f.readline()
       f.close()
    except IOError as e:
       webhook_version = 'VERSION undefined'

    try:
       f = open(os.path.dirname(os.path.abspath(__file__))+'/CHANGELOG')
       webhook_version_changelog = f.read()
       if len(webhook_version_changelog) == 0:
           webhook_version_changelog = 'CHANGELog undefined'
       f.close()
    except IOError as e:
       webhook_version_changelog = 'CHANGELog undefined'

    try:
       pandoc_version=subprocess.Popen(["pandoc", "--version"], \
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
       pandoc_version=pandoc_version.communicate()[0]
    except OSError as e:
       pandoc_version = u'Pandoc não encontrado - erro [%s]' % e

    try:
       pandocciteproc_version=subprocess.Popen(["pandoc-citeproc", "--version"], \
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    except OSError as e:
       pandocciteproc_version = u'Pandoc-citeproc não encontrado - erro [%s]' % e

    return render_template('about.html', webhook_version=webhook_version, \
                                         webhook_version_changelog=webhook_version_changelog, \
                                         pandoc_version=pandoc_version, \
                                         pandocciteproc_version=pandocciteproc_version, \
                                         enviroment_production=app.setup['production'], \
                                         gitlab_host=app.setup['gitlab_host'], \
                                         gitlab_url=app.setup['gitlab_url'] )

'''
Inicia aplicação em modo interativo (ex: python webhook.py)
'''
if __name__ == '__main__':
   if app.setup['production'] == 'False': # para devel ou testes
     if app.setup['DEBUG'] == 'True':
       app.debug = True

     app.run(host=app.setup['DEBUG_HOST'], port=app.setup['DEBUG_PORT'])
   else:
     app.run(host='0.0.0.0', port=5000)
