# coding: utf-8

def topicosBase(file_name):

    introducao_found = False
    introducao_header = False

    with open(file_name) as file:
        while True:
            line = file.readline()
            if not line:
               break

            if (line.find('Introdução') <> -1) or (line.find('# Introdução') <> -1):
                introducao_header = True

            if introducao_header:
               line = file.readline()
               if not line:
                  break

               if line.find('===') == 0:
                  introducao_found = True

    file.close()

    if introducao_found:
       print "**Introducao**: encontrado"
    else: 
       print u"Topico **Introducao** não encontrado"

