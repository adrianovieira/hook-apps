#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF-8')

from flask import Flask, request, json
import logging
import gitlab

# Webhook packages
import artigo
from config import WebhookConfig
from webhookerror import WebhookError

app = Flask(__name__)
app.debug = True
app.gitlab = gitlab.Gitlab('http://bsad229625-vbox-gitlab')
application_path = os.path.dirname(os.path.abspath(__file__))
#app.gitlab = gitlab.Gitlab('http://10.122.19.113')
#app.gitlab = gitlab.Gitlab('http://10.122.19.170')
# autentica no servidor gitlab
try:
  ok = app.gitlab.login('root','dataprev')
  if not ok: raise
except:
  __log_message = "ERROR: trying to set gitlab user/pass; or gitlab_host error."
  app.logger.debug(__log_message)

@app.route('/',methods=['POST'])
def index_post():

    try:
        artigo_parser_data = json.loads(request.data)
    except Exception as e:
        app.logger.warning(e)
        return 'config WebhookConfig! Erro na formatação dos dados informados "%s".'%e.message+'\n'

    try:
        config_parser = WebhookConfig(application_path, app.gitlab, app.logger, app.debug)
        setup = config_parser.getWebhookConfig()
        if app.debug: app.logger.debug(setup)

    except WebhookError as erro:
        app.logger.warning(erro.logging())
        return 'config WebhookConfig! Erro em parser: "%s".'%erro+'\n'

    return 'config WebhookConfig! Com sucesso!!!\n'

@app.route('/')
def index():

    app.logger.info('Olá, webhook')

    #raise NotImplementedError('GET ainda não implementado.')

    return 'Hello World!\n'

if __name__ == '__main__':
    app.run('0.0.0.0')

application = app
