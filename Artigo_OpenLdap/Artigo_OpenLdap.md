---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 29 de agosto de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Openldap - Serviço de autenticação centralizada baseada em código aberto
abstract: Este artigo apresenta uma visão concisa da utilização de sistemas de autenticação centralizada baseada na ferramenta de código aberto Openldap. Busca ilustrar de forma breve um quadro comparativo entre as principais abordagens de implementação e seus respectivos modelos de replicação. Além disso, visa contextualizar os desafios e benefícios que poderão ser obitidos com a adoção desses modelos na Dataprev.
author:
- affiliation: DSAA
  name: Anderson Levindo Pinto
responsibility:
- affiliation: DSAA
  name: Claudio Yuassa Tokoro
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Suporte de TIC - DEST'
tags:
- Tech0xA 
- OpenLDAP
- Replicação
- Alta Disponibilidade
- Cluster
- Tunning
...


Desafios
========


Contextualizar as diferenças básicas entre as abordagens de implementação dos modelos estático e dinámico do Openldap e das habilidades necessárias para sustentá-lo em um ambiente produtivo.


Benefícios e/ou recomendações
=============================


Este artigo tem como propósito fundamental ser tratado como uma referência rápida e básica no emprego da ferramenta Openldap como um sistema de autenticação centralizada. Busca ilustrar como as diferentes variações de implementação podem proporcionar diferentes níveis de qualidade na integração com outras ferramentas ulitizadas pela Dataprev.

O objetivo deste trabalho é contextualizar o leitor quanto aos principais elementos que compõe um serviço de autenciação centralizada, suas abordagens de implementação em um contexto organizacional, assim como os tipos de replicação disponíveis para manter um sistema distribuído capaz de atender uma demanda crescente por autenticar e autorizar o acesso à recursos corporativos.


Introdução
==========


LDAP, Lightweight Directory Access Protocol - Protocolo Leve de Acesso a Diretórios, é um protocolo de aplicação aberto, livre de fornecedor e padrão de indústria. Em sintese, é um conjunto de regras que controla a comunicação entre serviços de diretório e seus clientes sobre uma rede de Protocolo da Internet (IP). Foi criado a partir de em um subconjunto mais simples dos padrões contidos dentro do padrão X.500, e por isso, às vezes é referenciado como X.500-lite.

Segundo [@BUTCHER], o LDAP foi originalmente projetado para ser um protocolo de rede com capacidade de prover uma alternativa de acesso a serviços de diretório existentes, mas como a idéia do LDAP e as tecnologias evolvidas evoluiram, o termo tornou-se sinônimo de "Arquitetura de diretório".

>>*"Serviços de Diretório desempenham papel importante no desenvolvimento de aplicações intranet e Internet permitindo o compartilhamento de informações sobre recursos de rede, tais como usuários, sistemas, serviços e etc. Como exemplos, serviços de diretório podem fornecer qualquer conjunto de registros organizado, geralmente com uma estrutura hierárquica, como um diretório de e-mail corporativo. Da mesma forma que uma lista telefônica (diretório de telefones)  que nada mais é do que uma lista de assinantes com um endereço e um número de telefone. Um diretório LDAP geralmente segue o modelo X.500 que, em linhas gerais, é uma árvore de nós, cada um consistindo de um conjunto de atributos com seus respectivos valores. O LDAP foi criado como uma alternativa ao muito mais incômodo Directory Access Protocol (DAP)"[@ADMINGUIDE].*

O LDAP é especificado em uma série de publicações de Sequência de Padronização do Internet Engineering Task Force (IETF) chamadas Request for Comments (RFCs), usando a linguagem de descrição ASN.1. A última especificação é a Versão 3, publicada como RFC 4511. Por exemplo, aqui está uma pesquisa LDAP traduzida em Português puro: "Procure no diretório de e-mails da companhia por todas as pessoas localizadas em Belém cujos nomes contêm "João" que possuem um endereço de e-mail. Por favor, retorne seus nomes completos, e-mail, título e descrição."

Uma das utilizações mais comum do LDAP é fornecer um "logon único" de usuários e sistemas. Nesse processo, uma credencial é submetida à um serviço de rede, tal como uma aplicação web. Dada a validade dessa credencial, o usuário ou o sistema pode receber o direito de acesso a muitos outros sistemas compartilhados de uma só vez. Caso em que um sistema valida e autoriza o acesso aos demais recursos da rede.

![Autenticação usuário LDAP](imagens/Fig_authentific_portal_Via_LDAP.png)


Objetos e esquemas LDAP
=======================


Em linhas gerais, um objeto no serviço LDAP, pode ser definida como um conjunto organizado de atributos que possuem seus valores multivalorados ou não, obrigatórios ou não, e  que obedecem uma regra definida por um ou mais equemas. Ainda, segundo [@GIL] cada entrada de objeto (registro) no LDAP obedece uma regra de unicidade onde garante-se a não existência de dois ou mais objetos com mesmo identificador, ora denominado DN (Distinguished Name). 

Segundo [@SANGAILA], a forma de armazenamento dos dados em um servidor de Diretório segue a hierarquia dos objetos a que pertence a entrada, onde o DN deve sempre indicar todos os ramos da árvore LDAP, desde a base até a parte final, a identificação do objeto propriamente dito. Ainda, o DN deve ser único em todo o Diretório.


A figura abaixo ilustra alguns dos tipos de registros encontrados no serviço LDAP, assim como alguns dos seus respectivos atributos.

![Exemplo de Conta LDAP](imagens/Fig_ldap_Account_example.png)


Operações básicas da transação via LDAP
=======================================


O serviço LDAP foi concebido para ser um serviço de diretório capaz de armazenar e retornar consultas sobre informações. Em linhas gerais, é um serviço mais otimizado para reponder a consultas do que escrevê-las em banco.  -E um serviço projetado para executar várias transações, dentre as quais a mais comum é a pesquisa por informações. Abaixo segue uma lista das operações mais básicas desse serviço:


Principais transações
---------------------


- Bind: autentica e especifica a versão do protocolo LDAP
- Search: procura ou recupera entradas dos diretórios
- Compare: testa se uma entrada tem determinado valor como atributo
- Add: adiciona uma nova entrada
- Delete: apaga uma entrada
- Modify: modifica uma entrada
- Modify DN: move ou renomeia uma entrada
- Start TLS: protege a conexão com a Transport Layer Security (TLS)
- Abandon: aborta uma requisição prévia
- Extended Operation: operação genérica para definir outras operações
- Unbind – fecha a conexão. (Não entenda esta operação como se fosse o inverso de Bind)


Abordagem de implementação
==========================


O Openldap pode ser implementado para operar de forma estática ou dinâmica. Em sintese, as duas formas de operação se diferenciam, entre outras coisas, pelo nível de intervenção que cada uma exige para ser mantido dentro de um contexto produtivo. 

A forma estática prima pela necessidade de interrupção do serviço todas as vezes que se fizerem necessárias alterações estruturantes^[Termo utilizado para referir-se aos ajustes nos arquivos de configuração e de esquema do LDAP]. Nesse modelo de operação, para cada ajuste na base de configuração do serviço, uma interrupção é executada. O serviço é reiniciado (efetivação) ^[Fase em que o serviço LDAP re-lê e valida suas configurações] tantas vezes quantas forem as subsequentes modificações.

Já a forma de operação dinâmica dispensa a necessidade de reiniciação do serviço, as alterações são realizadas "à quente". Ainda, o processo de replicação/atualização das bases transcorre dentro do contexto pre-definido (ativação por tempo ou evento). O "overhead" administrativo é reduzido drasticamente, pois quase inexiste a necessidade de intervenção maunal. Nesse sentido, o downtime do serviço é reduzido invariavelmente. 

Em linhas gerais, existem prós e contras para cada abordagem acima descrita, enquanto uma apresenta necessidade escalar de manutenção (operação estática - uma a uma), outra não (operação dinâmica - um para todos). Os requisitos de negócio (disponibilidade do serviço e SLA) pesam na escolha por uma abordagem ou outra.


Modelos de Implementação
========================


Essa ferramenta de código aberto pode ser adotada seguindo dois paradigmas de implementação: o primeiro, adota a organização da árvore de diretórios seguindo o padrão X.500 que tem como base a regionalização (localização) do dado, enquanto que o segundo adota o estilo de organização baseado no conceito de domínios de Internet.

Segundo [@TRIGO1], A implementação baseada no pardrão X.500 estrutrua a árvore de diretórios em níveis, sendo o primeiro uma referência à estado ou país ("c" - country); o segundo, um estado ou cidade ("st" - state), e um terceiro referenciando uma organização ("o" - organizational). Na incidencia de uma filial em outro estado, cria-se um ramo (estrutura apartada) para ela. Em um quarto nível, criam-se os departamentos ("ou" - organizational unit), e por último, os recursos, pessoas, etc ("cn" - common name). Para ilustrar esse estilo, é apresentado a figura abaixo.


![Estrutura de um Diretório/Tipo localização](imagens/Fig_Estrut_LDAP_Tipo_Localidade.jpg)


Entretanto, a implemetação baseada no conceito de domínios de Internet, emprega o estilo de nomeação de domínios registrados nos servidores DNS. Nessa abordagem, cada diretório possui um atributo identificador "dc - domain component", onde uma cadeia de diretórios "dc" formam o que denomina-se "nome de domínio". Uma das grandes vantagens de se adotar esse estilo é a capacidade de se utilizar o serviço LDAP a partir de um nome de domínio existente, dando um caracter de unicidade de identidade do seu sistema de autenticação, além disso, torna-se possível o seu acesso por internos e parceiros de qualquer lugar do mundo. Para ilustrar esse estilo, é apresentado a figura abaixo.


![Estrutura de um Diretório/Domínio de Internet](imagens/Fig_Estrut_LDAP_DNS.jpg)


Modelos de Replicação
=====================


O serviço de autenticação Openldap pode ser empregado tendo como premissa vários requisitos, sendo um dos mais importantes a ser definido, o tipo de replicação de dados desejada para o ambiente: para esse, tem-se diponível os modelos de replicação simples (SMR - Single Master Replication), replicação multiplicada (MMR - Multi Master Replication) e replicação diferenciada (DMR - Delta Master Replication):

- SMR - Single Master Replication: é disponibilizado um servidor Mestre responsável por efetivar todas as transações (alterações/inserções) no banco de dados LDAP. Outro fator importante a frisar, é que esse modelo tem sempre um relacionamento de 1 servidor Mestre para vários (N) servidores escravos, não há um limite a ser estabelecido para aos escravos. Esse modelo é capaz de prover balanceamento de carga no processo de autenticação de usuários e sistemas, mas não oferece uma tolerância à falhas no caso de um incidente com o seu único servidor Master. Fica claro e evidente que seu principal problema é o ponto único de falhas.

- MMR - Multi Master Replication: o mais importante dessa abordagem é que quebra-se o paradigma da unicidade de servidores Masters. Passa a ser possível o emprego de um conjunto de servidores de escrita e/ou de leitura. Com esse modelo, o relacionamento torna-se "N" Masters para "N" slaves. Outra caracteristica marcante desse modelo, é que passa a ser possível replicar as informações de forma bi-direcional (Master para Slaves e/ou Masters para Masters). Do ponto de vista do negócio, passa-se a ter um sistema mais tolerante à falhas, capaz de reduzir tanto o "downtime" do serviço quanto da eliminação do ponto único de falhas. Esse modelo traz uma nomenclatura diferente para o os servidores Masters e Slaves. Eles, agora, são referenciados como servidores Provider (Master) e Consumer (slave).

- DMR - Delta Master Replication: segue basicamente as mesmas premissas do modelo SMR, entretanto este apresenta uma aproximação ao modelo MMR: a existência de mais de um servidor Master. Seu funcionamento se dá pelo apontamento de um único nó Master por vez. Em suma, nesse modelo, só um dos servidores pode exercer o papel de responsável pela escrita de dados, os outros Masters efetuam o papel de contingêncai. Outra questão importante, é que na ocorrência de uma indisponibilidade com o "atual" servidor Master, todos os outros servidores precisaram apontar para o novo Master. O que na grande maioria das vezes, manobra-se manualmente o sevidor Master de contingência para o Master principal.

Em resumo, fica evidente que o cenário desejado e/ou esperado é muito importante para se definir o modelo de replicação a ser implementado. O planejamento nesse caso é fundamental, pois se esse serviço for para substanciar um negócio com elevados níveis de criticidade, a adoção do modelo errado poderá gerar muitos infortúnios e desgastes à organização. De maneira geral, espera-se que qualquer serviço seja Confiável, Integro e Disponível (CID)^[Acrônimo utiizado para represntar a triade da Segurança da Informação].


Quadro comparativo entre os Modelos
===================================


Para que haja sucesso na adoção da ferramenta Openldap, deve-se entender o cenário proposto e os requisitos a serem atendidos. Requisitos como disponibilidade do serviço, tempo médio entre falhas (MTBF), tempo médio entre reparo (MTTR) devem ser considerados na avaliação do modelo de replicação a ser implementado.


+===============+===============================+===============================+
|**Modelo**     |**Balanceamento de carga**     |**Tolerância à falhas**        |
+===============+===============================+===============================+
|**SMR**        |Somente leitura de dados       |Ponto único de falhas escrita  |
|**MMR**        |Leitura e escrita de dados     |Leitura e escrita de dados     |
|**DMR**        |Somente leitura de dados       |Manual para escrita de dados   |
+===============+===============================+===============================+


Conclusão
=========


Uma informação muito importante apresentada é que o conhecimento prévio do ambiente (cenário tecnológico) que comportará o serviço LDAP é extremamente importante. A escolha do modelo a ser adotado precisa contemplar o nível de serviço mínimo exigido pela organização, assim como a quantificação e qualificação da equipe que o sustentará. Dependendo do modelo, o foco de problemas pode ser distribuído ou concentrado.

Em resumo, este artigo fez uma rápida introdução ao serviço de autenticação centralizada baseado em código aberto. Abordou os conceitos básicos sobre modelo de operação estático e dinâmico, implementação baseada em regionalização e padrão Internet/DNS. Tratou das questos relacionadas à replicação de dados, suas facilidades e recursos disponibilizados. Traçou um quadro comparativo sobe os requisitos de tolerância de falhas, balanceamento de carga e alta disponibilidade.


Referências
===========

---
remark: metadados com alguns dados para listar referências bibliográficas. Use quantos identificadores (ID) necessitar para listar as diferentes referências usadas no artigo
references:
- id: ADMINGUIDE
  title: "OpenLDAP Sofware 2.4 Administrator's Guide, Replication"
  author:
  - family:  Openldap.org
    given: 
  container-title: Guia de Referencia do Administardor
  URL: 'http://www.openldap.org/doc/admin24/replication.html'
  accessed:
    day: 29
    month: ago.
    year: 2014
  publisher: Admin Guide
  type: webpage

- id: TRIGO1
  title: "Openldap, Uma abordagem integrada"
  author: 
  - family: Clodonil Honório.
    given: Trigo
  publisher: Novatec Editora, Ltda.
  type: book
  issued:
    year: 2007

- id: GIL
  title: "Openldap Extreme"
  author:
  - family: Anahuac de Paula.
    given: Gil
  publisher: Brasport Livros e Multimídia, Ltda.
  type: book
  issued:
    year: 2012

- id: SANGAILA
  title: "Autenticação centralizada com Openldap"
  author:
  - family: Sangaila.
    given: Marcos
  publisher: Novatec Editora, Ltda.
  page: 23
  type: book
  issued:
    year: 2008

- id: BUTCHER
  title: "Mastering OpenLDAP - Configuring, Securing, and Integrating Directory Services"
  author:
  - family: Butcher.
    given: Matt
  publisher: Packt Publishing Ltd.
  type: book
  issued:
    year: 2007

...
