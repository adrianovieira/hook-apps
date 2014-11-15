# coding: utf-8

def topicosBase(file_name):

    introducao_found = False
    introducao_header = False

    with open(file_name) as file:
        for index, line in enumerate(file):
            if (line.find('Introducao') <> -1) or (line.find('# Introducao') <> -1):
                introducao_header = True
                print line

            if introducao_header:
               print line[index+1]
               if line[index+1].find('===') == 0:
                  introducao_found = True

    file.close()

    if introducao_found:
       print "**Introducao**"
    else: 
       print u"Topico **Introducao** não encontrado"

