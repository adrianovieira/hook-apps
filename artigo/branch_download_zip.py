# -*- coding: utf-8 -*-
import os, subprocess
import gitlab
import logging
from webhookerror import WebhookError

'''
Class: BranchDownloadZip
description: obtem "branch" de repositorio de "documentos/artigos"
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
raising Exception: evite propagar uma "Exception" genérica, ao contrário,
propague "Exceptions" específicas que mais se adeque à exceção em questão
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>.
  raise <built-in exceptions>('<mensagem>', '<app>', '<pacote/modulo>', '<metodo>' [, outros [,...]])
Propague-a com pelo menos quatro parâmetros,
sintaxe:
exemplo:
  raise WebhookError('all parameters are needed', 'APP_WEBHOOK', 'PCT_artigo', 'pandocParser')

@params:
  <gitlab_url>: URL para de acesso ao repositório no Gitlab
  <gitlab_webhook_user>: usuario para conexao ao gitlab_url
  <gitlab_webhook_pass>: senha para o usuario de conexao ao gitlab_url
  <gitlab>: objeto Gitlab para realizar comentário no merge request (MR)
  <logger>: objeto para logging
  [debug]: (opcional, parão=False)
  [debug_level]: (opcional, padrão=0)
'''
class BranchDownloadZip:

    def __init__(self, _gitlab_url, _gitlab_webhook_user, _gitlab_webhook_pass,
                       _gitlab, _logger, _debug=False, _debug_level=0):

        if not isinstance(_logger, logging.Logger):
            if _debug:
                logging.debug('BranchDownloadZip: argument logger object needed', 'webhook', 'artigo', 'BranchDownloadZip')
            raise WebhookError('BranchDownloadZip: argument logger object needed', 'webhook', 'artigo', 'BranchDownloadZip')
        if not isinstance(_gitlab, gitlab.Gitlab):
            if _debug:
                _logger.debug('BranchDownloadZip: argument gitlab object needed', 'webhook', 'artigo', 'BranchDownloadZip')
            raise WebhookError('BranchDownloadZip: argument gitlab object needed', 'webhook', 'artigo', 'BranchDownloadZip')

        self._logger = _logger
        self._gitlab = _gitlab
        self._debug = _debug
        self._debug_level = _debug_level
        self._gitlab_url = _gitlab_url
        self._gitlab_webhook_user = _gitlab_webhook_user
        self._gitlab_webhook_pass = _gitlab_webhook_pass

        self._target_project_id = ''
        self._mergerequest_id = ''
        self._mergerequest_branch = ''

        # end __init__

    '''
    branchDownload_zip: obtem "branch" de repositorio de "documentos/artigos"

    @params:
      target_project_id: The ID of a project (required)
      mergerequest_id: ID of merge request (required)
      mergerequest_branch: "branch" do artigo para conversão em PDF (required)
    '''
    def branchDownload_zip(_target_project_id, _mergerequest_id, _mergerequest_branch):

        # end branchDownload_zip

# end BranchDownloadZip
