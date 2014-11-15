# coding: utf-8

def topicosBase(file_name):

    introducao_found = False
    introducao_header = False

    desafios_found = False
    desafios_header = False

    with open(file_name) as file:
        while True:
            line = file.readline()
            if not line:
               break

            #  verifica tópico "Introdução"
            if (line.find('Introdução') <> -1) or (line.find('# Introdução') <> -1):
                introducao_header = True
            if introducao_header:
               line = file.readline()
               if not line:
                  break
               if line.find('===') == 0:
                  introducao_found = True

            #  verifica tópico "Desafios"
            if (line.find('Desafios') <> -1) or (line.find('# Desafios') <> -1):
                desafios_header = True
            if desafios_header:
               line = file.readline()
               if not line:
                  break
               if line.find('===') == 0:
                  desafios_found = True

    file.close()

    if introducao_found:
       print "**Introducao**: encontrado"
    else: 
       print u"Topico **Introducao** não encontrado"

    if desafios_found:
       print "**Desafios**: encontrado"
    else: 
       print u"Topico **Desafios** não encontrado"

