# coding: utf-8

'''
Class: Verifica
description: realizar a verificação de artigos produzidos observando sua estrutura base definida
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
Estrutura base:  
- Introdução: Descreve e contextualiza o conteúdo que o artigo irá abordar atraindo a sua leitura
- Desafios: Descreve desafios e/ou problemas que o artigo irá abordar e buscar resolver;
- Benefícios e/ou recomendações: Descreve os principais ganhos propostos pelo artigo, como melhoria de indicadores, processo de trabalho, etc;
- Conclusão: Apresenta o fechamento do artigo;
- Referências: Lista de referências bibliográficas, matérias na intranet, documentos ou ferramentas internas etc.

@params: (opcional) file_name = nome de arquivo markdown a ser verificado
'''
class Verifica:

    def __init__(self, __file_name=''):
        self.__has_introducao = False
        self.__has_desafios = False
        self.__has_beneficios = False
        self.__has_conclusao = False
        self.__has_referencias = False
        if len(__file_name) > 0:
           self.topicosBase(__file_name)

    def hasIntroducao(self):
        return self.__has_introducao
    def hasDesafios(self):
        return self.__has_desafios
    def hasBeneficios(self):
        return self.__has_beneficios
    def hasConclusao(self):
        return self.__has_conclusao
    def hasReferencias(self):
        return self.__has_referencias


    # @params: file_name = nome de arquivo markdown a ser verificado
    def topicosBase(self, file_name):

        self.__has_introducao = False
        self.__has_desafios = False
        self.__has_beneficios = False
        self.__has_conclusao = False
        self.__has_referencias = False

        with open(file_name) as file:
            while True:  # loop para ler conteudo do arquivo
                line = file.readline()
                if not line:
                   break

                #  verifica tópico "Introdução"
                if (line.find('Introdu') <> -1) or (line.find('# Introdu') <> -1):
                    if (line.find('# Introdu') == 0):
                       self.__has_introducao = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_introducao = True

                #  verifica tópico "Desafios"
                if (line.find('Desafios') <> -1) or (line.find('# Desafios') <> -1):
                    if (line.find('# Desafios') == 0):
                       self.__has_desafios = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_desafios = True

                #  verifica tópico "Benefícios"
                if (line.find('Benef') <> -1) or (line.find('# Benef') <> -1):
                    if (line.find('# Benef') == 0):
                       self.__has_beneficios = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_beneficios = True

                #  verifica tópico "Conclusão"
                if (line.find('Conclus') <> -1) or (line.find('# Conclus') <> -1):
                    if (line.find('# Conclus') == 0):
                       self.__has_conclusao = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_conclusao = True

                #  verifica tópico "Referências"
                if (line.find('Refer') <> -1) or (line.find('# Refer') <> -1):
                    if (line.find('# Refer') == 0):
                       self.__has_referencias = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_referencias = True

        file.close()

