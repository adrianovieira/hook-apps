WebHook
=======

***Gitlab***^[http://www.gitlab.com/] *Web Hook* para realizar conversão automatizada de documentos/artigos para PDF.

Pré-requisitos
--------------

Para instalação desse *Web Hook* são consideradas as seguintes premissas tecnológicas:

- Plataforma (*deploy*): ***Linux***
- Serviço Web: HTTP
- Linguagem: Python 2.7.x
- Framework: Flask 0.10 (ou superior)
- Parser PDF: Pandoc 1.12.3 (ou superior)
- Utilitário construtor: GNU Make
- Template Pandoc: <http://www-git/documentos/markdown-template>

### Configuração de servidor

- Memória: 4GB RAM - no mínimo
- Armazenamento: 50GB - sem considerar necessidade do S.O.  
  Esse armazenamento servirá para manter os arquivos a serem convertidos e os arquivos PDF gerados.

### Modo de acesso ao serviço

O acesso a esse webhook se dará via HTTP (porta 80 *full-duplex*). Assim, é necessário haver "apelido" para acesso ao serviço.

Exemplo para a forma de acesso:

- ```http://hook.www-git/artigos-webhook/```  
  Caminho para acesso ao serviço webhook de conversão *Pandoc/markdown*.
- ```http://hook.www-git/artigos-download/```  
  Caminho para acesso aos artigos PDF gerados na conversão.

Estrutura do diretório
----------------------

```texinfo
README.md:                   Visão geral desse Web Hook
INSTALL.md                   Este documento
webhook.py                   A aplicação para Web Hook do repositório
                             *documentos/artigos* no gitlab
webhook-dist.cfg:            Arquivo de configuração padrão (obrigatório)
requirements.txt:            Requisitos padrão para a aplicação
requirements-ipdb.txt:       Requisitos para debug interativo
teste/                       Alguns scripts NodeJS para teste de POST neste hook

```

Instalação
----------

1. Para ambiente de produção veja o manual do ***Flask***  
   [Deployment Options](<http://flask.pocoo.org/docs/deploying/>) ```http://flask.pocoo.org/docs/deploying/```  
   1.1. Caso venha ser uma instalação para contribuir com o desenvolvimento, considere a criação de ambiente virtual.  
      ```virtualenv --help```
1. Instale os requisitos necessários para executar a aplicação  
   Conforme sistema operacional  
   - ```<yum|apt-get|port> install make```  Ferramenta para executar um grupo de scripts de forma automatizada
   - [Pandoc Installing](<http://johnmacfarlane.net/pandoc/installing.html>) ```http://johnmacfarlane.net/pandoc/installing.html```
     - Assegure-se de que as fontes extras a seguir estejam instaladas  
       ```framed``` e ```ulem```.
   - ```pip install -r requirements.txt```  
1. Crie o arquivo ```webhook.cfg``` com os dados específicos do ambiente em que está para ser instalado.  
   Tenha como referência os parâmetros contidos no arquivo ```webhook-dist.cfg```.
1. Configure URL no servidor para ***download*** do PDF gerado
   - raiz: a mesma de ```path_tmp``` em ```webhook.cfg```
     - exemplo se em **webconfig.cfg**:  
       ```path_tmp = /var/tmp/webhook_tmp/download```

       exemplo no *apache*:  
       ```Alias /download /var/tmp/webhook_tmp/download```

   - download será como a seguir:
     ```http://hook.www-git/artigos-download/<link_artigo_PDF>```
1. Configure web hook para o projeto  
   Esse web hook é para conversão automatizada de artigos quando for solicitado ***"merge request"*** via interface do *Gitlab*.
   - acesse e configure o web hook para *merge request* do projeto em <http://www-git/documentos/artigos/hooks>
   - 
   
### Dica: Intalar *Pandoc/Texlive* (CentOS/RHEL)

Centos-7/RHEL-7

```shell
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
rpm -ivh epel-release-7-2.noarch.rpm 
```

Centos-6/RHEL-6

```shell
wget http://mirror.globo.com/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm
```

```
cat > /etc/yum.repos.d/texlive.repo <<EOF
[texlive]
name=texlive
baseurl=http://jnovy.fedorapeople.org/texlive/2012/packages.f17/
enabled=1
gpgcheck=0
EOF
```

```
cat > /etc/yum.repos.d/pandoc.repo <<EOF
[pandoc]
name=pandoc
baseurl=https://petersen.fedorapeople.org/pandoc-standalone/epel-5/x86_64/
enabled=1
gpgcheck=0
EOF
```

INSTALAÇÃO DOS PACOTES

```shell
yum clean all
yum install pandoc-pdf
yum install pandoc-citeproc
yum install texlive
yum install texlive-texlive.infra
yum install texlive-framed
yum install texlive-ulem
yum install texlive-xetex
yum install texlive-xetex-def
yum install texlive-mathspec
yum install texlive-ucs
yum install texlive-pdftex
yum install texlive-xetex-def
yum install texlive-euenc
yum install texlive-xltxtra
yum install texlive-polyglossia
```