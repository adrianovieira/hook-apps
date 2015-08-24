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
import pandoc
from webhookerror import WebhookError

app = Flask(__name__)
app.debug = True
app.setup={}
app.setup['DEBUG_LEVEL'] = logging.ERROR
app.setup['template_path'] = '/opt/share/markdown-template'
app.setup['download_path'] = '/tmp'
app.setup['webhook_host_url'] = 'http://vbox-webhook'
app.setup['gitlab_url_download'] = 'artigos-download'
artigo_branch_id = ''
artigo_path='/var/tmp/artigos/gestao_risco_projeto'
artigo_name='gestao_risco_projeto'
#artigo_path='/var/tmp/artigos/crie-conteudo-nao-leiaute'
#artigo_name='crie-conteudo-nao-leiaute'

#app.logger.setLevel(logging.INFO)

app.gitlab = gitlab.Gitlab('http://bsad229625-vbox-gitlab')
#app.gitlab = gitlab.Gitlab('http://10.122.19.113')
#app.gitlab = gitlab.Gitlab('http://10.122.19.170')
# autentica no servidor gitlab
try:
  ok = app.gitlab.login('root','dataprev')
  if not ok: raise
except:
  __log_message = "ERROR: trying to set gitlab user/pass; or gitlab_host error."
  app.logger.debug(__log_message)

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
#logging.basicConfig(FORMAT)

@app.route('/',methods=['POST'])
def artigo_parser():

    artigo_parser_data = json.loads(request.data)

    try:
        project_id=artigo_parser_data['object_attributes']['target_project_id']
    except Exception as e:
        app.logger.warning(e)
        return 'artigo PandocParser! Falta parâmetro "%s".'%e.message+'\n'

    try:
        mergerequest_id=artigo_parser_data['object_attributes']['iid']
    except Exception as e:
        app.logger.warning(e)
        return 'artigo PandocParser! Falta parâmetro "%s".'%e.message+'\n'

    try:
        artigo_parser = pandoc.PandocParser(app.setup['template_path'],
                                            app.setup['download_path'],
                                            app.setup['webhook_host_url'],
                                            app.setup['gitlab_url_download'],
                                            app.gitlab, app.logger,
                                            app.debug)

        artigo_parser.pandocParser(project_id, mergerequest_id,
                                   artigo_branch_id,
                                   artigo_path, artigo_name)
    except WebhookError as erro:
        app.logger.warning(erro.logging())
        return 'artigo PandocParser! Erro em parser: "%s".'%erro+'\n'

    return 'artigo PandocParser! Com sucesso!!!\n'

@app.route('/')
def index():

    app.logger.info('Olá, webhook')

    #raise NotImplementedError('GET ainda não implementado.')

    return 'Hello World!\n'

if __name__ == '__main__':
    app.run('0.0.0.0')

application = app
