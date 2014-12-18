# coding: utf-8

'''
Class: VerificaMetadados
description: realizar a verificação de artigos produzidos observando existência de metadados de autor e referências bibliográficas
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
class VerificaMetadados:

    def __init__(self, __file_name=''):
        self.__has_dados_autor= False
        self.__has_dados_referencias = False
        if len(__file_name) > 0:
           self.__file_name = __file_name
        else:
           self.__file_name = ''

    def hasDadosAutor(self):
        return self.__has_dados_autor
    def hasDadosReferencias(self):
        return self.__has_dados_referencias


    # @params: file_name = nome de arquivo markdown a ser verificado
    def verificaMetadados(self, file_name=''):

        self.__has_dados_autor= False
        self.__has_dados_referencias = False

        if (len(file_name) = 0) and (len(self.__file_name) > 0):
           file_name = self.__file_name

        with open(file_name) as file:
            while True:  # loop para ler conteudo do arquivo
                line = file.readline()
                if not line:
                   break

                #  verifica metadados de autor
                if (line.find('author:') == 0) or (line.find('abstract:') == 0):
                   self.__has_dados_autor = True

                #  verifica metadados de referencias
                if (line.find('references:') == 0) or (line.find('- id:') == 0):
                   self.__has_dados_referencias = True

        file.close()

