---
remark: metadados para a ser usado pelo parser de conversão para pdf ou odt
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Alta Disponibilidade SQL Server – Log Shipping
abstract: 'resumo'
author:
- affiliation: DEAT/DPJS
  name: Patrícia de Oliveira Pinto
responsibility:
- affiliation: DEAT/DPJS
  name: Ana Flavia Ribeiro de Araujo
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Arquitetura Técnica - DEAT'
tags:
- Alta disponibilidade
- Arquitetura
- Banco de Dados
- Resiliência
- Tech0xA
...

​1. Introdução
=============

A importância de se prevenir quedas em ambientes de produção, evitando paradas e descontentamentos dos mais variados tipos de usuários, faz com que, cada vez mais, se invista em recursos de alta disponibilidade visando garantir a contingência e continuidade do negócio (PCN).

Para que o PCN seja atendido faz-se necessária a definição de alternativas eficazes para que exista transparência no acesso aos dados por parte dos sistemas existentes na empresa e em caso de problema no servidor, permitindo que o trabalho prossiga regularmente.

A alta disponibilidade está relacionada com ambientes críticos, de modo que a operação de uma empresa não seja prejudicada em caso de falhas, permitindo continuidade do negócio. Uma solução de alta disponibilidade mascara os efeitos de uma falha de hardware ou software e mantém a disponibilidade dos aplicativos, de modo a minimizar o tempo de inatividade percebido pelos usuários.

Uma das soluções de alta disponibilidade nativas do SGBD MSSQL Server é a replicação de dados através de Log Shipping, no qual focaremos neste documento. Este, além de prover alta disponibilidade, também pode ser utilizado para manter uma cópia fiel do ambiente de produção, visando realização de consultas e geração de relatórios que muitas vezes sobrecarregam o servidor principal.

Desafios
===========

Benefícios e/ou recomendações
==========================


​3. Log Shipping
===============

Através do Log Shipping, uma base de dados é mantida atualizada no servidor secundário e servirá de contingência caso haja problemas no servidor principal. Em caso de problemas no servidor primário, somente será possível a realização de um failover manual para que a base replicada se torne a instância principal.

As remessas de logs de transação gerados a partir do servidor principal são configuradas através de jobs do SQL Server Agent, permitindo que se definam agendamentos tanto para o backup dos logs, quanto para o restore na base secundária.

No momento em que são gerados os backups de log, é possível habilitar a compactação dos arquivos, pensando na redução de seu tamanho físico, para que haja diminuição do tráfego na rede no momento em que estes forem enviados ao servidor secundário. Neste caso, é importante lembrar que haverá aumento na utilização de CPU do servidor principal durante o processo de compactação dos arquivos. Qualquer versão do SQL Server poderá descompactar esses arquivos, porém, se o secundário se tornar principal, não será possível compactar os logs de transação caso a versão utilizada não seja compatível com esta funcionalidade. Caso isto aconteça, dever-se-á acrescentar espaço em disco para os novos backups (tendo em vista que estes não estarão mais compactados).

A proposta de adoção da tecnologia de Log Shipping pode ainda ser associada à existência de uma base para geração de consultas para relatórios, por exemplo, isolando estes processamentos do ambiente de produção, com o objetivo de evitar possíveis problemas de desempenho. Além disso, ainda sobre sua finalidade, é comum combinar a utilização de Log Shipping com outras opções de alta disponibilidade, tais como Clustering e Database Mirrorring, de modo que exista mais de uma base atualizada, garantindo contingência em um ambiente de produção.

3.1 Estrutura do Log Shipping
-----------------------------

A tecnologia de Log Shipping é composta basicamente por três elementos:

- Servidor primário; 
- Servidor secundário (pode existir mais de um); 
- Servidor monitor (opcional). 

O servidor primário é responsável por enviar os logs para um ou mais servidores. Nele é armazenada toda a configuração do Log Shipping. Qualquer modificação na configuração do Log Shipping deve ser feita na base de dados primária, bem como a sua exclusão.

O servidor secundário tem a função de receber os logs de transação e aplicar sobre a base secundária, através de arquivos restaurados automaticamente pelos Jobs configurados a partir do servidor principal. Esta base mantém a consistência e similaridade com a base primária, pois os logs são enviados de forma ordenada, mantendo o LSN\* (Log Sequence Number) no momento da restauração.

O servidor secundário nunca poderá ser atualizado a não ser pelas aplicações de log. Os bancos, durante a configuração do Log Shipping, deverão, obrigatoriamente, que ser configurados com a opção StandBy ou Recovery Mode. Na opção StandBy é possível a realização de consultas e, na Recovery Mode, não é possível acessar a base replicada.

O servidor monitor é utilizado para armazenar detalhes sobre a utilização do Log Shipping entre os servidores primário e secundários. As informações incluem:

- Quando foi realizado o último backup dos log de transação no banco primário. 
- Quando foi realizada a última cópia e restore dos arquivos de backup no servidor secundário. 
- Informações sobre qualquer alerta de falha de backup. 

\* LSN – Cada registro em um log de transação no SQL Server é identificado por uma numeração, que mantém uma ordem para que possa realizar restaurações point-in-time (em um ponto específico definido), que são usadas para recuperar uma base até um determinado horário.

3.2 Funcionamento do Log Shipping
---------------------------------

O funcionamento do Log Shipping consiste de três etapas básicas e fundamentais:

1. Backup dos logs de transação no servidor primário. 
2. Cópia destes arquivos de log para o servidor secundário. 
3. Restauração dos logs na instância secundária. 

![estrutura e funcionamento do Log Shipping](imagens/log-shipping-estrutura.jpg)

Este processo ocorre através da ação de três jobs criados após a configuração da estrutura de Log Shipping na instância primária que são executados pelo SQL Server Agent. São eles:

- Backup Job  - Nomeada como “Log Shipping Backup”, é responsável por gerar backups dos arquivos de log, registrar histórico no servidor local e no monitor, e apagar os arquivos obsoletos e informações históricas. Por padrão, o intervalo para a execução deste job é de 15 minutos porém pode ser alterado conforme necessidade. A periodicidade de exclusão dos arquivos de log já aplicados também pode ser configurada.
- Copy Job – Nomeada de “Log Shipping Copy” e criada no servidor secundário, esta job copia os arquivos de backup do servidor primário para um destino configurável no servidor secundário e o servidor monitor.
- Restore Job – job “Log Shipping Restore” é criada e executada no(s) banco de dados secundário(s) com função de restore dos arquivos de log que foram copiados na execução da job especificada acima. Ele grava o histórico no servidor local e monitor server, e apaga arquivos e históricos antigos. O job de restore pode ter seu intervalo de execução alterado, pelo administrador de banco de dados, de acordo com políticas definidas e necessidades específicas.
- Alert Job - “Log Shipping Alert” criado no servidor monitor, levanta alertas dos bancos primário e secundários quando um backup ou operação de restore não completar com sucesso e em um intervalo especificado. 

​4. Pontos de atenção
====================

Para a implementação do Log Shipping é importante estar atento com relação a recursos físicos para garantir que a sequência das etapas funcione de forma satisfatória. Abaixo alguns itens que são de boa prática observar:

- Rede – deve-se verificar a disponibilidade da rede  para o processo de backup dos arquivos de log do servidor primário para a área compartilhada, e desta para o servidor secundário. O tempo de cópia não deve exceder o intervalo do job de backup, evitando falhas no arquivamento dos logs;
- Performance do servidor – monitorar os servidores principal e secundário, desde a geração dos backups dos logs de transação, até a restauração dos mesmos no ambiente de contingência, é trivial para que não se tenha problemas com relação ao intervalo de execução dos backups, correndo risco de resultar em falhas;
- Disco – Deve-se ter em mente que é fundamental reservar espaço em disco para que não haja falhas no processo de backup e cópia destes arquivos para o destino. Configure adequadamente o tempo de retenção dos logs obsoletos para que o próprio Log Shipping apague estes arquivos de tempos em tempos.

  É essencial que os discos contenham o mesmo espaço em disco nos servidores primário e secundários para que não haja falha na restauração do arquivo de log no servidor secundário. Qualquer acréscimo de espaço em disco no servidor primário deve ser replicado para o servidor secundário;
- Localização do servidor de monitoramento – Apesar de não ser obrigatório, para segurança, é importante que se mantenha este servidor opcional fora do ambiente onde residam o principal e secundário. Assim se assegura preservar o histórico de backups, restores e alertas. 

​5. Configuração
===============

Para o funcionamento do Log Shipping os servidores e instâncias devem possuir algumas características:

- A edição do SQL Server deve suportar o Log Shipping;
- Os servidores envolvidos na montagem do Log Shipping devem possuir a mesma configuração com relação a case sensitive;
- As bases de dados utilizados devem usar a opção de recovery model setado para FULL ou BULK\_LOGGED, pois dessa maneira os logs das alterações serão gerados para que seja viável a restauração na base secundária;
- Para habilitar o Log Shipping é necessário que o usuário do banco possua a server role SYSADMIN em ambas as instâncias;
- Com relação às permissões em diretórios da rede, para a execução da job de backup e de restore, é necessário permissão de leitura/escrita nos diretórios correspondentes. Por padrão, são usadas as contas dos serviços do SQL Server e do SQL Server Agent na execução das jobs e, sendo assim, estas permissões devem ser delegadas a estas contas de domínio.
- As instâncias SQL devem se enxergar, isto é, devem estar no mesmo domínio de rede para que possa haver a configuração do Log Shipping.

5.1 Integridade e Confiabilidade
--------------------------------

São recomendadas algumas boas práticas no intuito de auxiliar a integridade e confiabilidade da configuração do Log Shipping:

- No caso de interrupções no processo de restore por falha de qualquer natureza, garanta que os backups dos logs de transação sejam preservados até que o problema seja identificado e corrigido;
- Os backups dos logs de transação podem ser utilizados para uma restauração até um determinado instante anterior a um erro grave que ocorreu no BD, caso seja necessário;
- No caso de uma base com extrema utilização para escritas, as transações podem gerar logs muito grandes, o que deve ser considerado quando for definido o tamanho do espaço em disco necessário para os arquivos de backup;
- O tamanho dos arquivos de backup, a velocidade da rede e o intervalo de tempo para as restaurações fazem parte do planejamento de uma solução de Log Shipping. Testes devem ser feitos para que a configuração seja adequadamente implementada;
- Em uma base onde existe a solução de Log Shipping configurada, não se deve gerar backups de log sem utilizar os jobs de backup já implementados. Se ocorrer um backup de log sem passar pelo Job, haverá quebra de log sequence number (LSN) e será necessário reconfigurar o Log Shipping;
- Se houver necessidade da existência do servidor de monitoramento, este deve ser adicionado durante a configuração inicial. Não será possível adicioná-lo após o término da configuração. 

​6. Conclusão
============

Alta disponibilidade é assunto obrigatório quando falamos em servidores corporativos de banco de dados. Em qualquer empresa é de vital importância que algumas aplicações não parem de funcionar. A queda de uma aplicação causa prejuízos que podem ser de receita, perda de SLA, aumento de custo (quando um sistema é substituído por um processo manual)  e até mesmo na imagem da empresa, entre outros.

As diversas opções de alta disponibilidade da Microsoft visam atender qualquer cenário, não importa o tamanho da empresa, tamanho do banco ou tipo de aplicação. Como estas soluções são nativas do MSSQL Server, são soluções de baixo custo.

O Log Shipping é uma tecnologia de alta disponibilidade que aplica logs transacionais em uma cópia do banco de dados com certa periodicidade, garantindo uma cópia atualizada do banco de dados na rede. Embora o tempo de atraso entre a aplicação destes logs no servidor secundário possa resultar em um banco de dados desatualizado no destino, pode-se utilizar a base secundária para leitura dos dados e recuperação caso ocorra um erro humano na base principal.

​7. Referências
==============

---
references:
- id: R1
  title: "Soluções de alta disponibilidade"
  URL: 'http://msdn.microsoft.com/pt-br/library/ms190202.aspx'
  accessed:
    month: 05
    year: 2014
  publisher: Microsoft
  type: webpage

- id: R2
  title: "About Log Shipping"
  author:
  - family: Saks
    given: Kenneth
  URL: 'http://technet.microsoft.com/en-us/library/ms187103.aspx'
  accessed:
    month: 05
    year: 2014
  publisher: Microsoft
  type: webpage
  
- id: R3
  title: "Configure Log Shipping"
  author:
  - family: Saks
    given: Kenneth
  URL: 'http://technet.microsoft.com/en-us/library/ms190640.aspx'
  accessed:
    month: 05
    year: 2014
  publisher: Microsoft
  type: webpage
---