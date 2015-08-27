# -*- coding: utf-8 -*-
import gitlab
import logging
import ConfigParser

from webhookerror import WebhookError

'''
Class: WebhookConfig
description: tratar dados de configuracao do ambiente
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
  <application_path>: caminho absoluto da aplicação
  <gitlab>: objeto Gitlab para realizar comentário no merge request (MR)
  <logger>: objeto para logging
  [debug]: (opcional, parão=False)
  [debug_level]: (opcional, padrão=0)
'''
class WebhookConfig:

    def __init__(self, _application_path,
                       _gitlab, _logger, _debug=False, _debug_level=0):

        if not isinstance(_logger, logging.Logger):
            if _debug:
                logging.debug('WebhookConfig: argument logger object needed')
            raise WebhookError('WebhookConfig: argument logger object needed', 'WebhookConfig', 'config')
        if not isinstance(_gitlab, gitlab.Gitlab):
            if _debug:
                _logger.debug('WebhookConfig: argument gitlab object needed')
            raise WebhookError('WebhookConfig: argument gitlab object needed', 'WebhookConfig', 'config')

        self._logger = _logger
        self._gitlab = _gitlab
        self._debug = _debug
        self._debug_level = _debug_level
        self._application_path = _application_path
        raise WebhookError('WebhookConfig ainda não implementado', 'WebhookConfig', 'config')

        # end __init__

    '''
    getWebhookConfig: obtem dados de configuracao do ambiente da aplicação

    dados a serem obtidos dos arquivos:
        - 'webhook-dist.cfg' - padrão para o "webhook" (obrigatório)
        - 'webhook.cfg' - personalizado para o ambiente de trabalho/produção (opcional)
    '''
    def getWebhookConfig(self):
        result = False

        raise WebhookError('Método getWebhookConfig ainda não implementado', 'WebhookConfig', 'config')

        # se não gerou exceção retorna com sucesso
        result = True

        return result
        # end getWebhookConfig

# end WebhookConfig
