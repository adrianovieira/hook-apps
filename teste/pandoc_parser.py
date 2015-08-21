#!/usr/bin/python
# coding: utf-8

from flask import Flask, request, json
import logging

import artigo
import pandoc

import gitlab

app = Flask(__name__)
app.debug = True
app.setup={}
app.setup['DEBUG_LEVEL'] = logging.ERROR
app.setup['path_template'] = ''
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
    #print json.dumps(artigo_parser_data)

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

    artigo_path='/home/users/adriano.vieira/devel/dev-gitlab-hook/webhook/artigo/'
    artigo_name='estrutura.md'

    try:
        artigo_parser = pandoc.PandocParser(app)
        artigo_parser.pandocParser(project_id, mergerequest_id,
                                    artigo_path, artigo_name)
    except Exception as e:
        #app.logger.warning(e)
        return 'artigo PandocParser! Erro em parser: "%s".'%e+'\n'

    return 'artigo PandocParser! Com sucesso!!!\n'

@app.route('/')
def index():

    app.logger.info('Olá, webhook')

    #raise NotImplementedError('GET ainda não implementado.')

    return 'Hello World!\n'

if __name__ == '__main__':
    app.run('0.0.0.0')
