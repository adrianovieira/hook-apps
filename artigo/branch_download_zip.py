# -*- coding: utf-8 -*-
import os, subprocess
import gitlab
import logging
import requests, zipfile, StringIO
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
                       _download_path,
                       _gitlab, _logger, _debug=False, _debug_level=0):

        if not isinstance(_logger, logging.Logger):
            if _debug:
                logging.debug('BranchDownloadZip: argument logger object needed')
            raise WebhookError('BranchDownloadZip: argument logger object needed', 'BranchDownloadZip')
        if not isinstance(_gitlab, gitlab.Gitlab):
            if _debug:
                _logger.debug('BranchDownloadZip: argument gitlab object needed')
            raise WebhookError('BranchDownloadZip: argument gitlab object needed', 'BranchDownloadZip')

        self._logger = _logger
        self._gitlab = _gitlab
        self._debug = _debug
        self._debug_level = _debug_level
        self._gitlab_url = _gitlab_url
        self._gitlab_webhook_user = _gitlab_webhook_user
        self._gitlab_webhook_pass = _gitlab_webhook_pass
        self._download_path = _download_path

        # end __init__

    '''
    branchDownload_zip: obtem "branch" de repositorio de "documentos/artigos"

    @params:
      target_project_id: The ID of a project (required)
      mergerequest_id: ID of merge request (required)
      mergerequest_branch: "branch" do artigo para conversão em PDF (required)
    '''
    def branchDownload_zip(self, _target_project_id, _mergerequest_id, _mergerequest_branch):
        result = False
        _log_message = 'A ***branch* [%s]** e artigo serão obtidos do repositório!'\
                        % _mergerequest_branch

        if self._debug:
            self._logger.debug(_log_message)

        # url para download do repositório como arquivo zip
        zip_file_req_branch_url = self._gitlab_url+'/repository/archive.zip?ref='+_mergerequest_branch
        if self._debug:
            _log_message = _log_message + '\n<br /> | URL para download: '+zip_file_req_branch_url

        # insere comentário no merge request
        if self._debug and self._debug_level <= logging.INFO:
            self._logger.debug(_log_message)
            self._gitlab.addcommenttomergerequest(_target_project_id, _mergerequest_id, _log_message)

        zip_file_req_branch = requests.get(zip_file_req_branch_url, auth=(self._gitlab_webhook_user, self._gitlab_webhook_pass))
        if not zip_file_req_branch.ok or not zip_file_req_branch.headers['content-type'] == 'application/zip':
            # erro de conexão ou se o conteúdo não for aquivo zip
            _log_message = 'O ***PDF*** não foi gerado pois foram encontrados erros ao tentar obter a *branch* do artigo.'
            _log_message = _log_message + '\n<br /> | Erro no download: ***branch* [%s]** não obtida' % _mergerequest_branch
            if self._debug:
                _log_message = _log_message + '\n<br /> | URL para download: '+zip_file_req_branch_url
                _log_message = _log_message + '\n<br /> | request status: [%s (user: %s)]' \
                                % (zip_file_req_branch.status_code, self._gitlab_webhook_user)
                _log_message = _log_message + '\n<br /> | header content-type: [*%s*]' \
                                % (zip_file_req_branch.headers['content-type'])

            self._logger.debug(_log_message)
            self._gitlab.addcommenttomergerequest(_target_project_id, _mergerequest_id, _log_message)

            raise WebhookError(_log_message, 'BranchDownloadZip')

        raise WebhookError(NotImplementedError('branchDownload_zip: método ainda não implementado completamente'), 'BranchDownloadZip')

        result = True

        return result
        # end branchDownload_zip

# end BranchDownloadZip
