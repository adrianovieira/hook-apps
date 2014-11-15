# coding: utf-8

'''
description: realizar a verificação de artigos produzidos observando sua estrutura de tópicos base definida
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
Estrutura base:  
- Introdução: Descreve e contextualiza o conteúdo que o artigo irá abordar atraindo a sua leitura
- Desafios: Descreve desafios e/ou problemas que o artigo irá abordar e buscar resolver;
- Benefícios e/ou recomendações: Descreve os principais ganhos propostos pelo artigo, como melhoria de indicadores, processo de trabalho, etc;
- Conclusão: Apresenta o fechamento do artigo;
- Referências: Lista de referências bibliográficas, matérias na intranet, documentos ou ferramentas internas etc.

@params: file_name = nome de arquivo markdown a ser verificado
'''
def topicosBase(file_name):

    introducao_found = False
    desafios_found = False
    beneficios_found = False
    conclusao_found = False
    referencias_found = False

    with open(file_name) as file:
        while True:
            line = file.readline()
            if not line:
               break

            #  verifica tópico "Introdução"
            if (line.find('Introdução') <> -1) or (line.find('# Introdução') <> -1):
                if (line.find('# Introdução') == 0):
                   introducao_found = True
                else:
                   line = file.readline()
                   if not line:
                      break
                   if line.find('===') == 0:
                      introducao_found = True

            #  verifica tópico "Desafios"
            if (line.find('Desafios') <> -1) or (line.find('# Desafios') <> -1):
                if (line.find('# Desafios') == 0):
                   desafios_found = True
                else:
                   line = file.readline()
                   if not line:
                      break
                   if line.find('===') == 0:
                      desafios_found = True

            #  verifica tópico "Benefícios"
            if (line.find('Benefícios') <> -1) or (line.find('# Benefícios') <> -1):
                if (line.find('# Benefícios') == 0):
                   beneficios_found = True
                else:
                   line = file.readline()
                   if not line:
                      break
                   if line.find('===') == 0:
                      beneficios_found = True

            #  verifica tópico "Conclusão"
            if (line.find('Conclusão') <> -1) or (line.find('# Conclusão') <> -1):
                if (line.find('# Conclusão') == 0):
                   conclusao_found = True
                else:
                   line = file.readline()
                   if not line:
                      break
                   if line.find('===') == 0:
                      conclusao_found = True

            #  verifica tópico "Referências"
            if (line.find('Referências') <> -1) or (line.find('# Referências') <> -1):
                if (line.find('# Referências') == 0):
                   referencias_found = True
                else:
                   line = file.readline()
                   if not line:
                      break
                   if line.find('===') == 0:
                      referencias_found = True

    file.close()

    if introducao_found:
       print "**Introducao**: encontrado"
    else: 
       print "Topico **Introducao** não encontrado"

    if desafios_found:
       print "**Desafios**: encontrado"
    else: 
       print "Topico **Desafios** não encontrado"

    if beneficios_found:
       print "**Benefícios**: encontrado"
    else: 
       print "Topico **Benefícios** não encontrado"

    if conclusao_found:
       print "**Conclusão**: encontrado"
    else: 
       print "Topico **Conclusão** não encontrado"

    if referencias_found:
       print "**Referências**: encontrado"
    else: 
       print "Topico **Referências** não encontrado"

