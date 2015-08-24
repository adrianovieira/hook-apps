# coding: utf-8
import os, subprocess
import gitlab
import logging
from webhookerror import WebhookError

'''
Class: PandocParser
description: realizar a conversão do artigo para PDF
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
raising Exception: evite propagar uma "Exception" genérica, ao contrário,
propague "Exceptions" específicas que mais se adeque à exceção em questão
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>.
Propague-a com pelo menos quatro parâmetros,
  raise <built-in exceptions>('<mensagem>', '<app>', '<pacote/modulo>', '<metodo>' [, outros [,...]])
sintaxe:
exemplo:
  raise AttributeError('all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')

@params:
  <app>: ponteiro para objeto app do Flask
  <template_path>: caminho para o template "markdown-template"
'''
class PandocParser:

    def __init__(self, _template_path, _download_path,
                       _webhook_host_url, _gitlab_url_download,
                       _gitlab, _logger, _debug=False, _debug_level=0):
        if not isinstance(_gitlab, gitlab.Gitlab):
            if _debug:
                _logger.debug('PandocParser: argument gitlab object needed', 'APP_WEBHOOK', 'PCT_artigo', 'PandocParser')
            raise AttributeError('PandocParser: argument gitlab object needed', 'APP_WEBHOOK', 'PCT_artigo', 'PandocParser')

        self._logger = _logger
        self._gitlab = _gitlab
        self._debug = _debug
        self._debug_level = _debug_level
        self._template_path = _template_path
        self._download_path = _download_path
        self._webhook_host_url = _webhook_host_url
        self._gitlab_url_download = _gitlab_url_download
        self._target_project_id = ''
        self._mergerequest_id = ''
        self._artigo_path = ''
        self._artigo_name = ''

        # end __init__

    '''
    pandocParser: realizar a conversão do artigo para PDF

    @params:
      target_project_id: <string> ID do projeto (necessário)
      mergerequest_id: <string> ID do merge request (necessário)
      artigo_path: <string> path para o artigo (necessário)
      artigo_name: <string> nome do artigo (necessário)
    '''
    def pandocParser(self, _target_project_id, _mergerequest_id,
                           _artigo_branch_id,
                           _artigo_path, _artigo_name):

        result = False
        _has_dados_parser = True

        if self._debug:
            self._logger.debug('APP_Artigo_PandocParser: \n artigo-path: %s\n artigo-nome: %s', _artigo_path, _artigo_name)

        if not self._target_project_id:
            if _target_project_id: self._target_project_id = _target_project_id
            else: _has_dados_parser = False

        if not self._mergerequest_id:
            if _mergerequest_id: self._mergerequest_id = _mergerequest_id
            else: _has_dados_parser = False

        if not self._artigo_path:
            if _artigo_path: self._artigo_path =  _artigo_path
            else: _has_dados_parser = False

        if not self._artigo_name:
            if _artigo_name: self._artigo_name = _artigo_name
            else: _has_dados_parser = False

        if not _has_dados_parser:
            if self._debug:
                self._logger.debug('pandocParser: all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')
            raise AttributeError('pandocParser: all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')

        _log_message = u'Iniciada conversão do artigo **%s** para ***PDF***!' % self._artigo_name
        if self._debug and self._debug_level <= logging.INFO:
            self._logger.info("projID: %s | MR: %s | Msg: %s" % (self._target_project_id, self._mergerequest_id, _log_message))

        # insere comentário no merge request
        try:
            ok = self._gitlab.addcommenttomergerequest(self._target_project_id,
                                            self._mergerequest_id, _log_message)
            if not ok:
                _log_message = 'projID: %s | MR: %s | Msg: %s' % \
                        (self._target_project_id, self._mergerequest_id, \
                         'Erro ao tentar comentar no merge request')
                self._logger.error(_log_message)
                raise EnvironmentError('pandocParser: %s'%_log_message, 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')
        except Exception as erro:
            raise EnvironmentError(erro)

        # DIRETORIOS TEMPORARIOS E DIRETORIO DE TEMPLATE PANDOC-PARSER
        root_dir = os.popen("pwd").read()[:-1]
        try:
            path_ok = os.chdir(self._artigo_path)
        except Exception as erro:
            self._logger.error(erro)
            raise WebhookError(erro)

        parse_result=subprocess.Popen(["make", "-f", self._template_path+"/makefile", "pdf",
                                "artigo="+self._artigo_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT).communicate()[0]
        os.chdir(root_dir)
        if "[ OK ]" in parse_result:
            download_path = self._download_path+"/"+_artigo_branch_id+"/"
            download = os.popen("mkdir -p "+download_path).read()
            download = os.popen("cp "+self._artigo_path+"/"+self._artigo_name+'.pdf'+" "
                                     +download_path)

            link = self._artigo_name+'.pdf'
            #_link = app.setup['webhook_host_url']+'/'+app.setup['gitlab_url_download']+'/'+_artigo_branch_id+'/'+self._artigo_name+'.pdf'
            link = self._webhook_host_url+'/'+self._gitlab_url_download+'/'+_artigo_branch_id+'/'+self._artigo_name+'.pdf'
            print link
            _log_message = 'O artigo (%s) foi convertido para ***[PDF (clique aqui)](%s)***!' % (self._artigo_name, link)
            result = True
        else:
            _log_message = 'Ocorreu erro ( ***make*** ) na conversao do arquivo (%s) para ***PDF***!'\
                              % self._artigo_name
            _log_message = _log_message + '<br /> | O ***PDF*** não foi gerado pois foram encontrados problemas no artigo.  '
            _log_message = _log_message + '<br /> | Ocorreu erro ( ***pandoc*** ) na conversao do arquivo (%s) para ***PDF***!  ' % self._artigo_name
            _log_message = _log_message + '<br /> | ```<erro>'+parse_result+'</erro>```'
            if "Erro 83" in parse_result or "pandoc-citeproc" in parse_result:
                _log_message = _log_message + '<br /> | Acesse o **item 10** da [FAQ - Perguntas e respostas frequentes ](http://www-git/documentos/artigos/wikis/faq) para detalhes.'
            else:
                _log_message = _log_message + '<br /> | Temos algumas respostas na [FAQ - Perguntas e respostas frequentes](http://www-git/documentos/artigos/wikis/faq).'

            if self._debug: self._logger.error(parse_result)

        # parser finalizado e comentários serão adicionados ao MR
        self._gitlab.addcommenttomergerequest(self._target_project_id,
                                              self._mergerequest_id,
                                              _log_message)

        return result
        # end pandocParser

#end class PandocParser
