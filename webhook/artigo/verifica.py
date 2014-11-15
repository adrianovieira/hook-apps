# coding: utf-8

def topicosBase(file_name):

    introducao_found = False
    desafios_found = False
    beneficios_found = False

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

