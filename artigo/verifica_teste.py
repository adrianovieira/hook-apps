# coding: utf-8

'''
Class: VerificaTeste
description: realizar testes referentes à classe Verifica
author: Adriano dos Santos Vieira <adriano.vieira@dataprev.gov.br>
character encoding: UTF-8
Estrutura base:  
- Introdução: Descreve e contextualiza o conteúdo que o artigo irá abordar atraindo a sua leitura
- Desafios: Descreve desafios e/ou problemas que o artigo irá abordar e buscar resolver;
- Benefícios e/ou recomendações: Descreve os principais ganhos propostos pelo artigo, como melhoria de indicadores, processo de trabalho, etc;
- Conclusão: Apresenta o fechamento do artigo;
- Referências: Lista de referências bibliográficas, matérias na intranet, documentos ou ferramentas internas etc.

'''
class VerificaTeste:
    def topicosBaseTeste(self):
        artigo_verifica = Verifica('estrutura.md')
        artigo_verifica.topicosBase('estrutura.md')

        if artigo_verifica.hasIntroducao():
               print "**Introducao**: encontrado"
        else: 
               print "Topico **Introducao** não encontrado"

        if artigo_verifica.hasDesafios():
               print "**Desafios**: encontrado"
        else: 
               print "Topico **Desafios** não encontrado"

        if artigo_verifica.hasBeneficios():
               print "**Benefícios**: encontrado"
        else: 
               print "Topico **Benefícios** não encontrado"

        if artigo_verifica.hasConclusao():
               print "**Conclusão**: encontrado"
        else: 
               print "Topico **Conclusão** não encontrado"

        if artigo_verifica.hasReferencias():
               print "**Referências**: encontrado"
        else: 
               print "Topico **Referências** não encontrado"

