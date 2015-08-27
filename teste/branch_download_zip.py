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
from webhookerror import WebhookError

app = Flask(__name__)
app.debug = True
app.setup={}
app.setup['DEBUG_LEVEL'] = logging.ERROR
app.setup['download_path'] = '/var/tmp/webhook_tmp'
app.setup['_gitlab_url'] = 'http://bsad229625-vbox-gitlab/adriano/artigos'
app.setup['_gitlab_webhook_user'] = 'admin'
app.setup['_gitlab_webhook_pass'] = 'dataprev'
app.gitlab = gitlab.Gitlab('http://bsad229625-vbox-gitlab')

try:
  ok = app.gitlab.login('root','dataprev')
  if not ok: raise
except:
  app.logger.debug("ERROR: trying to set gitlab user/pass; or gitlab_host error.")

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
#logging.basicConfig(FORMAT)

@app.route('/',methods=['POST'])
def index_post():

    try:
        artigo_parser_data = json.loads(request.data)
    except Exception as e:
        app.logger.warning(e)
        return 'artigo BranchDownloadZip! Erro na formatação dos dados informados "%s".'%e.message+'\n'

    try:
        project_id=artigo_parser_data['object_attributes']['target_project_id']
    except Exception as e:
        app.logger.warning(e)
        return 'artigo BranchDownloadZip! Falta parâmetro "%s".'%e.message+'\n'

    try:
        mergerequest_id=artigo_parser_data['object_attributes']['id']
    except Exception as e:
        app.logger.warning(e)
        return 'artigo BranchDownloadZip! Falta parâmetro "%s".'%e.message+'\n'

    try:
        mergerequest_branch=artigo_parser_data['object_attributes']['source_branch']
    except Exception as e:
        app.logger.warning(e)
        return 'artigo BranchDownloadZip! Falta parâmetro "%s".'%e.message+'\n'

    try:
        artigo_downloadzip = artigo.BranchDownloadZip(
                                            app.setup['_gitlab_url'],
                                            app.setup['_gitlab_webhook_user'],
                                            app.setup['_gitlab_webhook_pass'],
                                            app.setup['download_path'],
                                            app.gitlab, app.logger, app.debug)

        artigo_downloadzip.branchDownload_zip(project_id, mergerequest_id, mergerequest_branch)

    except WebhookError as erro:
        app.logger.warning(erro.logging())
        return 'artigo BranchDownloadZip! "%s".'%erro+'\n'

    return 'artigo BranchDownloadZip! Com sucesso!!!\n'

@app.route('/')
def index():

    app.logger.info('Olá, webhook')

    #raise NotImplementedError('GET ainda não implementado.')

    return 'Hello World!\n'

if __name__ == '__main__':
    app.run('0.0.0.0')

application = app
