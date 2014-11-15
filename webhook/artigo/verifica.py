# coding: utf-8

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
                if (line.find('Introdução') <> -1) or (line.find('# Introdução') <> -1):
                    if (line.find('# Introdução') == 0):
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
                if (line.find('Benefícios') <> -1) or (line.find('# Benefícios') <> -1):
                    if (line.find('# Benefícios') == 0):
                       self.__has_beneficios = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_beneficios = True

                #  verifica tópico "Conclusão"
                if (line.find('Conclusão') <> -1) or (line.find('# Conclusão') <> -1):
                    if (line.find('# Conclusão') == 0):
                       self.__has_conclusao = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_conclusao = True

                #  verifica tópico "Referências"
                if (line.find('Referências') <> -1) or (line.find('# Referências') <> -1):
                    if (line.find('# Referências') == 0):
                       self.__has_referencias = True
                    else:
                       line = file.readline()
                       if not line:
                          break
                       if line.find('===') == 0:
                          self.__has_referencias = True

        file.close()

class VerificaTeste:
    def teste(self):
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

