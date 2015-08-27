# -*- coding: utf-8 -*-
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
                       _logger, _debug=False, _debug_level=0):

        if not isinstance(_logger, logging.Logger):
            if _debug:
                logging.debug('WebhookConfig: argument logger object needed')
            raise WebhookError('WebhookConfig: argument logger object needed', 'WebhookConfig', 'config')

        self._logger = _logger
        self._debug = _debug
        self._debug_level = _debug_level
        self._application_path = _application_path

        self._config = self._loadWebhookConfig()

        # end __init__

    '''
    getWebhookConfig: obter dados de configuracao do ambiente da aplicação

    dados a serem obtidos dos arquivos:
        - 'webhook-dist.cfg' - padrão para o "webhook" (obrigatório)
        - 'webhook.cfg' - personalizado para o ambiente de trabalho/produção (opcional)
    '''
    def getWebhookConfig(self):
        return self._config
        # end getWebhookConfig

    '''
    _loadWebhookConfig: carregar dados de configuracao do ambiente da aplicação

    dados a serem obtidos dos arquivos:
        - 'webhook-dist.cfg' - padrão para o "webhook" (obrigatório)
        - 'webhook.cfg' - personalizado para o ambiente de trabalho/produção (opcional)
    '''
    def _loadWebhookConfig(self):
        config_parser = ConfigParser.ConfigParser()
        arquivo_nome_webhook_dist_cfg = self._application_path+'/webhook-dist.cfg'
        arquivo_nome_webhook_custom_cfg = self._application_path+'/webhook.cfg'

        '''
        obtem dados de configuracao padrao
        '''
        try:
            ok = config_parser.read(arquivo_nome_webhook_dist_cfg)
            if not ok: raise
        except:
            _log_message = 'Erro ao tentar ler o arquivo de configurações padrão (%s)'\
                            % arquivo_nome_webhook_dist_cfg
            self._logger.error(_log_message)
            raise WebhookError(_log_message, 'WebhookConfig', 'config')

        config = {}
        config['production'] = config_parser.get('enviroment', 'production')
        config['gitlab_host'] = config_parser.get('enviroment', 'gitlab_host')
        config['gitlab_url'] = config_parser.get('enviroment', 'gitlab_url')
        config['gitlab_url_download'] = config_parser.get('enviroment', 'gitlab_url_download')
        config['gitlab_target_branch'] = config_parser.get('enviroment', 'gitlab_target_branch')
        config['gitlab_webhook_user'] = config_parser.get('enviroment', 'gitlab_webhook_user')
        config['gitlab_webhook_pass'] = config_parser.get('enviroment', 'gitlab_webhook_pass')
        config['path_template'] = config_parser.get('enviroment', 'path_template')
        config['path_tmp'] = config_parser.get('enviroment', 'path_tmp')
        config['pandoc'] = config_parser.get('enviroment', 'pandoc')
        config['make'] = config_parser.get('enviroment', 'make')
        config['DEBUG'] = config_parser.get('enviroment', 'DEBUG')
        config['DEBUG_LEVEL'] = config_parser.get('enviroment', 'DEBUG_LEVEL')
        config['DEBUG_HOST'] = config_parser.get('enviroment', 'DEBUG_HOST')
        config['DEBUG_PORT'] = int(config_parser.get('enviroment', 'DEBUG_PORT'))

        '''
        obtem dados de configuracao personalizados
        '''
        try:
            ok = config_parser.read(arquivo_nome_webhook_custom_cfg)
            if not ok: raise

            if config_parser.get('enviroment', 'production'):
              config['production'] = config_parser.get('enviroment', 'production')
            if config_parser.get('enviroment', 'gitlab_host'):
              config['gitlab_host'] = config_parser.get('enviroment', 'gitlab_host')
            if config_parser.get('enviroment', 'gitlab_webhook_user'):
              config['gitlab_webhook_user'] = config_parser.get('enviroment', 'gitlab_webhook_user')
            if config_parser.get('enviroment', 'gitlab_webhook_pass'):
              config['gitlab_webhook_pass'] = config_parser.get('enviroment', 'gitlab_webhook_pass')
            if config_parser.get('enviroment', 'gitlab_url'):
              config['gitlab_url'] = config_parser.get('enviroment', 'gitlab_url')
            if config_parser.get('enviroment', 'gitlab_url_download'):
              config['gitlab_url_download'] = config_parser.get('enviroment', 'gitlab_url_download')
            if config_parser.get('enviroment', 'gitlab_target_branch'):
              config['gitlab_target_branch'] = config_parser.get('enviroment', 'gitlab_target_branch')
            if config_parser.get('enviroment', 'path_template'):
              config['path_template'] = config_parser.get('enviroment', 'path_template')
            if config_parser.get('enviroment', 'path_tmp'):
              config['path_tmp'] = config_parser.get('enviroment', 'path_tmp')
            if config_parser.get('enviroment', 'pandoc'):
              config['pandoc'] = config_parser.get('enviroment', 'pandoc')
            if config_parser.get('enviroment', 'make'):
              config['make'] = config_parser.get('enviroment', 'make')
            if config_parser.get('enviroment', 'DEBUG'):
              config['DEBUG'] = config_parser.get('enviroment', 'DEBUG')
            if config_parser.get('enviroment', 'DEBUG_LEVEL'):
              config['DEBUG_LEVEL'] = config_parser.get('enviroment', 'DEBUG_LEVEL')
            if config_parser.get('enviroment', 'DEBUG_HOST'):
              config['DEBUG_HOST'] = config_parser.get('enviroment', 'DEBUG_HOST')
            if config_parser.get('enviroment', 'DEBUG_PORT'):
              config['DEBUG_PORT'] = int(config_parser.get('enviroment', 'DEBUG_PORT'))

        except:
            _log_message = 'Arquivo de configurações personalizadas (%s) não encontrado'\
                            % arquivo_nome_webhook_custom_cfg
            self._logger.warning(_log_message)
            pass

        # se não gerou exceção retorna dados de configuração obtidos
        return config
        # end _loadWebhookConfig

# end WebhookConfig
