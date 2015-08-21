# coding: utf-8
import os, subprocess
import gitlab
import logging

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
  [debug]: habilitar/desabilitar (True/False) modo de depuração
'''
class PandocParser:

    def __init__(self, app):
        if not isinstance(app.gitlab, gitlab.Gitlab):
            if app.debug:
                app.logger.debug('PandocParser: argument gitlab object needed', 'APP_WEBHOOK', 'PCT_artigo', 'PandocParser')
            raise AttributeError('PandocParser: argument gitlab object needed', 'APP_WEBHOOK', 'PCT_artigo', 'PandocParser')

        self.__app = app
        self.__debug = app.debug
        self.__debug_level = app.setup['DEBUG_LEVEL']
        self.__target_project_id = ''
        self.__mergerequest_id = ''
        self.__app_artigo_path = ''
        self.__app_artigo_name = ''

        # end __init__

    '''
    pandocParser: realizar a conversão do artigo para PDF

    @params:
      target_project_id: <string> ID do projeto (necessário)
      mergerequest_id: <string> ID do merge request (necessário)
      app_artigo_path: <string> path para o artigo (necessário)
      app_artigo_name: <string> nome do artigo (necessário)
    '''
    def pandocParser(self, __target_project_id='', __mergerequest_id='',\
                     __app_artigo_path='', __app_artigo_name=''):

        __result = False
        __has_dados_parser = True

        if self.__debug:
            self.__app.logger.debug('APP_Artigo_PandocParser: \n artigo-path: %s\n artigo-nome: %s', __app_artigo_path, __app_artigo_name)

        if not self.__target_project_id:
            if __target_project_id: self.__target_project_id = __target_project_id
            else: __has_dados_parser = False

        if not self.__mergerequest_id:
            if __mergerequest_id: self.__mergerequest_id = __mergerequest_id
            else: __has_dados_parser = False

        if not self.__app_artigo_path:
            if __app_artigo_path: self.__app_artigo_path =  __app_artigo_path
            else: __has_dados_parser = False

        if not self.__app_artigo_name:
            if __app_artigo_name: self.__app_artigo_name = __app_artigo_name
            else: __has_dados_parser = False

        if not __has_dados_parser:
            if self.__debug:
                self.__app.logger.debug('pandocParser: all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')
            raise AttributeError('pandocParser: all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')

        __log_message = u'Iniciada conversão do artigo **%s** para ***PDF***!' % self.__app_artigo_name
        if self.__debug and self.__debug_level <= logging.INFO:
            self.__app.logger.info("projID: %s | MR: %s | Msg: %s" % (self.__target_project_id, self.__mergerequest_id, __log_message))

        # insere comentário no merge request
        try:
            ok = self.__app.gitlab.addcommenttomergerequest(self.__target_project_id,
                                            self.__mergerequest_id, __log_message)
            if not ok:
                if self.__debug:
                    __log_message = u'projID: %s | MR: %s | Msg: %s' % \
                            (self.__target_project_id, self.__mergerequest_id, \
                             u'Erro ao tentar comentar no MR')
                    self.__app.logger.error(__log_message)
                    raise EnvironmentError('pandocParser: %s'%__log_message, 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')
        except Exception as erro:
            if self.__debug:
                self.__app.logger.error(erro.args)

        return __result
        # end pandocParser

#end class PandocParser
