# coding: utf-8
import os, subprocess
import requests
import gitlab

'''
Class: PandocParser
description: realizar a conversão do artigo para PDF
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
raising Exception: evite propagar uma "Exception" genérica, ao contrário,
propague "Exceptions" específicas que mais se adeque à exceção em questão
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>.
Propague-a com pelo menos quatro parâmetros,
sintaxe:
  raise <built-in exceptions>('<mensagem>', '<app>', '<pacote/modulo>', '<metodo>' [, outros [,...]])
exemplo:
  raise AttributeError('all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')

@params: (opcional) debug = habilitar/desabilitar (True/False) modo de depuração
'''
class PandocParser:

    '''
    PandocParser: realizar a conversão do artigo para PDF

    @params:
      target_project_id: ID do projeto (necessário)
      mergerequest_id: ID do merge request (necessário)
      app_artigo_path: path para o artigo (necessário)
      app_artigo_name: nome do artigo (necessário)
    '''
    def __init__(self, __debug=False):
        self.__debug = __debug

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

        if self.__debug: print 'APP_Artigo_PandocParser:'
        if self.__debug: print __app_artigo_path
        if self.__debug: print __app_artigo_name

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
            raise AttributeError('all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')

        return __result
        # end pandocParser

    '''
    debug: des/habilitar modo de depuração

    @params:
      debug: boolean True/False (habilitar/desabilitar)
    '''
    def debug(__debug):
        self.__debug = __debug
        # end debug
