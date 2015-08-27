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

        self._config = self._loadWebhookConfig()

        raise WebhookError('Módulo WebhookConfig ainda não implementado', 'WebhookConfig', 'config')

        return True

        # end __init__

    '''
    _loadWebhookConfig: obtem dados de configuracao do ambiente da aplicação

    dados a serem obtidos dos arquivos:
        - 'webhook-dist.cfg' - padrão para o "webhook" (obrigatório)
        - 'webhook.cfg' - personalizado para o ambiente de trabalho/produção (opcional)
    '''
    def _loadWebhookConfig(self):
        config_parser = ConfigParser.ConfigParser()
        arquivo_nome_webhook_dist_cfg = self._application_path+'/webhook-dist.cfg'

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

        raise WebhookError('Método _loadWebhookConfig ainda não finalizado', 'WebhookConfig', 'config')

        # se não gerou exceção retorna dados de configuração
        return config
        # end getWebhookConfig

# end WebhookConfig
