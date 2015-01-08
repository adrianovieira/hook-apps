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

# classes e metodos relacionados a verificações em artigos
import artigo

'''
artigoPandocParser: realizara a conversão do artigo para PDF

@params:
  p_target_project_id: The ID of a project (necessário)
  p_mergerequest_id: ID of merge request (necessário)
  p_app_artigo_path: path para o artigo (necessário)
  p_app_artigo_name: nome do artigo (necessário)
'''
def artigoPandocParser(p_target_project_id, p_mergerequest_id,\
                 p_app_artigo_path, p_app_artigo_name):

  result = False

  if app.debug: print 'APP_Artigo:'
  if app.debug: print p_app_artigo_path
  if app.debug: print p_app_artigo_name

  app.log_message = u'O artigo **%s** esta sendo convertido para ***PDF***!' % p_app_artigo_name
  if app.debug: print app.log_message

  # insere comentário no merge request
  app.gitlab.addcommenttomergerequest(p_target_project_id, \
                                      p_mergerequest_id, app.log_message)

  # DIRETORIOS TEMPORARIOS E DIRETORIO DE TEMPLATE PANDOC-PARSER

  root_dir=os.popen("pwd").read()[:-1]
  os.chdir(p_app_artigo_path)
  parse=subprocess.Popen(["make", "-f", app.setup['path_template']+"/makefile", "pdf", \
                    "artigo="+p_app_artigo_name],\
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
  os.chdir(root_dir)

  if parse == '':
      app.log_message = 'Ocorreu erro ( ***make*** ) na conversao do arquivo (%s) para ***PDF***!'\
                        % p_app_artigo_name

  if "[ OK ]" in parse:
    download_path = app.setup['path_tmp']+"/"+app.artigo_branch_id
    download = os.popen("mkdir -p "+download_path).read()
    download = os.popen("cp "+p_app_artigo_path+p_app_artigo_name+'.pdf'+" "\
                             +download_path)
    link = app.setup['webhook_host_url']+'/'+app.setup['gitlab_url_download']+'/'+app.artigo_branch_id+'/'+p_app_artigo_name+'.pdf'
    app.log_message = 'O artigo (%s) foi convertido para ***[PDF](%s) ***!' % (p_app_artigo_name, link)
    result = True
  else:
    app.log_message = u'Ocorreu erro ( ***pandoc*** ) na conversao do arquivo (%s) para ***PDF***!' % p_app_artigo_name
    if app.debug: print parse
    app.gitlab.addcommenttomergerequest(p_target_project_id, \
                                        p_mergerequest_id, parse)

  if app.debug: print app.log_message

  app.gitlab.addcommenttomergerequest(p_target_project_id, \
                                      p_mergerequest_id, app.log_message)

  return result

'''
artigoDownload_zip: obtem "branch" de repositorio de "documentos/artigos"

@params:
  p_target_project_id: The ID of a project (required)
  p_mergerequest_id: ID of merge request (required)
  p_mergerequest_branch: "branch" do artigo para conversão em PDF (required)
'''
def artigoDownload_zip(p_target_project_id, p_mergerequest_id, p_mergerequest_branch):

  result = False

  app.log_message = u"A ***branch* [%s]** e artigo serao obtidos do repositorio!" \
                            % p_mergerequest_branch

  if app.debug: print app.log_message

  # insere comentário no merge request
  if app.debug: app.gitlab.addcommenttomergerequest(p_target_project_id, \
                                      p_mergerequest_id, app.log_message)

  # url para download do repositório como arquivo zip
  zip_file_req_branch_url = app.setup['gitlab_url']+'/repository/archive.zip?ref='\
                                            +p_mergerequest_branch
  app.log_message = "Obtendo **branch** do artigo %s.md" % p_mergerequest_branch
  if app.debug: print app.log_message

  zip_file_req_branch = requests.get(zip_file_req_branch_url)
  if not zip_file_req_branch.ok:
    app.log_message = u"**branch [%s]** não obtida - status: [%s]" \
                      % (p_mergerequest_branch, zip_file_req_branch.status_code)
    if app.debug: print app.log_message

  if zip_file_req_branch.ok:

    # obtem conteúdo do arquivo zip obtido
    zip_content = zipfile.ZipFile(StringIO.StringIO(zip_file_req_branch.content))

    try:
      # diretorio e nome de artigo == branch (do merge request)
      repo_name = str.split(app.setup['gitlab_url'], '/')
      repo_name = str.split(app.setup['gitlab_url'], '/')[len(repo_name)-1]
      zip_member_artigo_dir = repo_name+'.git/'+p_mergerequest_branch+'/'
      zip_member_artigo_name = zip_member_artigo_dir+p_mergerequest_branch+'.md'

      app.log_message = u"***branch*** não contem diretório **[%s]** do artigo" % p_mergerequest_branch
      zip_content.getinfo(zip_member_artigo_dir) # verifica se diretorio de artigo existe

      app.log_message = u"***branch*** não contem arquivo **[%s.md]** do artigo" % p_mergerequest_branch
      zip_content.getinfo(zip_member_artigo_name) # verifica se artigo existe

      app.log_message = u"Extraindo **branch** do artigo %s.md" % p_mergerequest_branch
      if app.debug: print app.log_message

      # obtem informacões da branch
      branch_info = app.gitlab.getrepositorybranch(p_target_project_id, p_mergerequest_branch)

      # local para extrair arquivos (conforme ID do último commit)
      path_zip_extract = app.setup['path_tmp']+'/'+branch_info['commit']['id']
      app.log_message = u"Extraindo **branch** em %s" % path_zip_extract
      if app.debug: print app.log_message

      # extrai o zip para um diretório temporário
      zip_content.extractall(path_zip_extract)

      # dados para parser de artigo
      app.artigo_branch_id = branch_info['commit']['id']
      app.artigo_path = path_zip_extract +'/'+ zip_member_artigo_dir
      app.artigo_name = p_mergerequest_branch

      result = True

    except:
      app.gitlab.addcommenttomergerequest(p_target_project_id, \
                                          p_mergerequest_id, app.log_message)
      if app.debug: print app.log_message


  return result

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
   'can_be_merged':'can_be_merged'
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
       webhook_data['object_attributes']['merge_status'] == GL_STATUS['can_be_merged']:
      if app.debug: print "\nProcessing merge request to build PDF...\n"
      if app.debug: print app.log_message

      # simples adição de comentário ao merge request
      if app.debug:  app.gitlab.addcommenttomergerequest( \
                                          webhook_data['object_attributes']['target_project_id'], \
                                          webhook_data['object_attributes']['id'], \
                                          'Processando *merge request* para gerar PDF...[*'+ \
                                          webhook_data['object_attributes']['merge_status']+'*]')

      # obtem do repositório a branch a converter para PDF
      if artigoDownload_zip(webhook_data['object_attributes']['target_project_id'], \
                     webhook_data['object_attributes']['id'], \
                     webhook_data['object_attributes']['source_branch']):

        # realisar verificação de metadados de autor e referencias bibliograficas
        if app.debug: print "\nRealisando verificação de metadados de autor e referencias bibliograficas do artigo...\n"

        metadados_msg = 'Na estrutura base há grupos de dados (metadados) que contêm atributos para facilitar a formatação do artigo. Esta estrutura está disponível em <http://www-git/documentos/artigos/blob/master/estrutura-para-criar-artigos-tecnicos/Estrutura_e_metodo_padrao_para_criar_artigos.md#estrutura-padr-o-para-criar-artigos>. Foi percebida a ausência do(s) grupo(s) de dado(s) a seguir:  \n' 
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

        topicos_base_msg = 'Uma estrutura base facilita ao leitor se localizar na leitura dos artigos. Neste sentido, foi definida uma estrutura base para os artigos que está disponível em <http://www-git/documentos/artigos/blob/master/estrutura-para-criar-artigos-tecnicos/Estrutura_e_metodo_padrao_para_criar_artigos.md#estrutura-padr-o-para-criar-artigos>. Foi percebida a ausência do(s) tópico(s) a seguir:  \n' 
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
            if artigoPandocParser(webhook_data['object_attributes']['target_project_id'], \
                            webhook_data['object_attributes']['id'], \
                            app.artigo_path, app.artigo_name):
              status = '{"status": "OK"}'
            else:
              status = '{"status": "notOK"}'
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
                                         pandoc_version=pandoc_version, \
                                         pandocciteproc_version=pandocciteproc_version )

'''
Inicia aplicação em modo interativo (ex: python webhook.py)
'''
if __name__ == '__main__':
   if app.setup['production'] == 'False': # para devel ou testes
     if app.setup['DEBUG'] == 'True':
       app.debug = True
       if app.setup['DEBUG'] == 'True' and int(app.setup['DEBUG_LEVEL']) == DEBUG_INTERATIVO:
          import ipdb; ipdb.set_trace() # ativação de debug interativo

     app.run(host=app.setup['DEBUG_HOST'], port=app.setup['DEBUG_PORT'])
   else:
     app.run(host='0.0.0.0', port=5000)

