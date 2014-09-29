---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 20 de agosto de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Políticas de Backup Corporativo.
abstract: Artigo sobre as políticas e formas de backup que podem ser usados para controle e segurança no armazenamento das informações de sistemas corporativos. Estes controles são importantes para a confiabilidade das informações que estão sendo armazenadas para possíveis utilizações futuras.
author:
- affiliation: DEQI/DICI
  name: Leandro Brandão Marques
responsibility:
- affiliation: DEQI/DICI
  name: Rogerio de Souza Braz do Canto Cyrillo
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Qualidade de Infraestrutura de TIC'
tags:

- Tech0xA      
- Conceitos de backup 
- As políticas de backup corporativo

---
Introdução
===
Atualmente, os sistemas corporativos requerem soluções de backup cada vez mais velozes, flexíveis e confiáveis, preparadas para atender diversas plataformas.
A necessidade de garantir a integridade e a segurança da informação é tão grande que os profissionais de suporte não podem contar apenas com simples sistemas de armazenamento, necessitando utilizar recursos mais eficientes como os sistemas de backup corporativo, por exemplo. Adotar soluções depende de um correto planejamento tecnológico que deve ser adaptado ao foco do negócio, integrando de forma inteligente a tecnologia utilizada aos novos hardwares e softwares e que ofereçam meios para gerenciar constantemente esses componentes[@Pinheiro2014].
Hoje em dia, existem serviços de backup que são disponibilizados por servidores online, como por exemplo, dropbox, icloud e google docs. O backup online tem a vantagem de permitir o acesso aos dados guardados a partir de qualquer computador com acesso à internet[@Significado2014].

Desafio
===
As grandes organizações possuem suas políticas de armazenamento e restauração de dados, estas políticas seguem padrões definidos de acordo com o tipo de negócio que a empresa está inserida. Estas políticas visam uma rápida recuperação de suas informações no caso de uma iminente falha em sua base de dados e devem ser planejadas e verificadas de tempos em tempos, visando a ter informações rápidas, consistentes em um menor tempo possível.
Planejar uma política de backup não é simplesmente copiar dados de um “computador”, é preciso minimamente atentar para alguns pontos chaves: 

- a segurança das informações que estão sendo armazenadas; 
- o meio que se está usando para o armazenamento; 
- a periodicidade deste armazenamento e; 
- os testes destas cópias de segurança.



Benefícios e/ou recomendações
=== 
Todos os tipos de backup devem ser testados periodicamente para garantir que os dados possam ser lidos através deles. É fato, que, às vezes, os backups executados são por algum motivo ilegíveis. O pior é que muitas vezes isto só é percebido quando os dados são perdidos e devem ser restaurados pelo backup. As razões para isto ocorrer podem variar desde alterações no alinhamento do cabeçote do drive de fita, software de backup mal configurado a um erro do operador. Independente da causa. Sem o teste periódico você não pode garantir que está gerando backups através dos quais poderá restaurar dados no futuro[@Macedo2012].

A Política
===
Podemos sugerir que para termos uma política de backup eficiente temos que levar em consideração pelo menos alguns pontos a seguir:

**1. Quais os dados que serão armazenados?**
Essa é a pergunta inicial a ser respondida. Uma forma de respondê-la é saber quais as informações que são mais importantes dentro da empresa ou de seu equipamento (em caso de usuários domésticos)[@Calvano2012]. Fazendo referência a uma empresa temos os seguintes itens a ser analisados:

- *Informações dos sistemas de gestão da empresa*. Normalmente são mantidos em bases de dados estruturadas e todas elas possuem opções de exportação e/ou backup dos dados. Embora sua empresa utilize sistemas hospedados “na nuvem”, deve existir a opção de exportação dos dados para não correr o risco de depender 100% da eficiência do fornecedor;

- *Informações chamadas de “não estruturadas”*. São as informações que estão tirando o sono dos administradores pelo mundo e hoje possuem até um jargão: Big Data. Big por que são grandes e crescem a passos largos diariamente. São planilhas, arquivos de texto, e-mails, chat´s, imagens, vídeos que hoje fazem parte do dia-a-dia da gestão de qualquer empresa e por isso mesmo precisam ser gerenciados. Nesse caso temos uma complicação, pois esses arquivos tem que estar centralizados para facilitar o backup. Normalmente, utiliza-se um servidor de arquivos para esse fim, onde todos os usuários, salvarão suas informações importantes e estas ficaram armazenadas neste local da rede para serem backupiadas;

**2. Qual a frequência da operação de backup?**
A reposta depende da frequência de alteração das informações em questão, assim vale lembrar, que algumas empresas costumam fazer a operação de backup duas vezes por dia, períodos do meio-dia e à meia-noite, por exemplo. A verdade é que o quanto antes fizermos backup de uma informação, mais fácil será obter uma cópia consistente em caso de necessidade. É importante observar que em certos casos, vale a pena manter um sistema de controle de versão dos arquivos, como fazem as softhouses. 
Pense bem antes de responder essa pergunta! Respondê-la de forma errada pode levar a sérios prejuízos! Como, por exemplo, fazer backup de informações que estão corrompidas ou que estão muito desatualizadas causando retrabalho em caso de um recovery(restauração) dos dados[@Calvano2012].

**3. Quais equipamentos e tecnologias serão utilizados no backup?**
Antigamente, existiam poucas opções aos usuários comuns ou a pequenas empresas, hoje, podemos lançar mão de fitas magnéticas de alta capacidade de armazenamento que são eficientes. Os backups em disco são rápidos e podem crescer a medida da necessidade, como exemplos, os NAS (Network Attached Storage), discos externos como pendrives, HD´s externos e as opções de backup em nuvem como o FatDrive.
Há opções para diversas necessidades e orçamentos, escolha aquela que irá lhe trazer o melhor custo x benefício x segurança. 
Muita atenção no seguinte: - dependendo da tecnologia eleita, talvez você tenha que ter um backup do equipamento de backup. Sugiro comprar Hard Disk´s sobressalentes! Em caso de adquirir soluções de backup, preste atenção se você não ficará “preso” para sempre a um fornecedor específico ou a uma tecnologia proprietária, nunca é demais compreender que isso não é vantagem para você ou para o seu negócio[@Calvano2012].

**4. Qual o volume de dados gerados por cada operação de backup e por quanto tempo meu equipamento irá suportar esse volume?**
Responder corretamente a essa pergunta evitará o investimento desnecessário.  Sistemas de rotinas críticas fazem altos investimentos para evitar falhas, porque eles entendem o quanto custaria caso ficasse tempo demais parado e assim conseguem dimensionar os investimentos. Quanto custaria não ter acesso às informações ou perder seu trabalho? Não há uma fórmula pronta para responder essa pergunta mas um bom modelo seria acompanhar o crescimento dos arquivos de backup no tempo e fazer projeções futuras baseados no compasso desse crescimento[@Calvano2012].

**5. Qual estratégia de backup será a mais adequada?**
A estratégia de backup deve ser elaborada de acordo com a demanda dos dados que serão armazenados e deve ser montada de modo a ter uma facilidade de recuperação de dados em caso de falhas nos sistemas em foco[@Calvano2012]. 

*Apresento algumas sugestões para rotinas de backup:*

*Diferencial* (diários) – segundas às quintas-feiras, realizados a partir das 12hrs. e às 24hrs. com uma semana de retenção;

*Completo* (semanais) – algum dia da semana, realizado em horário pré-agendado de modo, que não hajam sistemas processando informações naquele momento, para que o backup seja feito por completo da base de dados, com um mês de retenção;

*Completo* (mensais) – primeira sexta-feira do mês, em horário pré-agendado, com um ano de retenção;

*Incremental* – serve para adicionar arquivos novos a partir de um backup completo. Deve ser usado para dados que não mudam com o tempo como imagens e vídeos que não são editados mas que novos são acrescentados com o tempo.

**6. Quem avaliará se a política de backup está sendo seguida e qual o procedimento será usado para esta avaliação?**
Quero frisar que não adianta ter uma política de backup perfeita se ela não é auditada. Deve existir um procedimento de checagem para ver se as políticas estão sendo efetivas ou se ajustes devem ser feitos, é necessário que restaurações de teste sejam feitas por essa auditoria. É de suma importância que a auditoria não seja feita pelo responsável pelo backup mas por outra pessoa que tenha condições de avaliá-lo[@Calvano2012].

Conclusão
===
Para se ter uma política de backup segura é necessário que sejam elaboradas rotinas minuciosas para a geração e teste dos mesmos levando-se em consideração fatores importantes no tocante à segurança, testes, armazenamento das mídias e ao pessoal qualificado para operar e analisar as informações geradas pelas ferramentas utilizadas para tal função, tendo condições de tomar atitudes pró-ativas no caso de falhas de geração e restauração dos dados e até mesmo nas auditorias dos processos pré-definidos.


Refêrencias
===

---
remark: referências usadas nesse artigo
references:

- id: Pinheiro2014
  title: "Políticas de backup corporativo"
  author: 
  - family: Pinheiro
  	given: José Mauricio Santos
  URL: 'http://www.uenp.edu.br/index.php/graduacao-uenp/246-administrativo-e-tecnico/nucleo-tecnologia-da-informacao2/seguranca-info/430-politicas-de-backup-corporativo'
  accessed:
    month: 8
    year: 2014
  publisher: Dataprev
  type: article
  issued:
    year: 2014

- id: Macedo2012
  title: "Backup: Conceitos e tipos"
  author:
  - family: Macedo
  	given: Diego 
  URL: 'http://www.diegomacedo.com.br/backup-conceito-e-tipos'
  accessed:
    month: 8
    year: 2014
  publisher: Dataprev
  type: article
  issued:
    year: 2012


- id: Calvano2012
  title: "Backup: Conceitos e tipos"
  author: 
  - family: Calvano
  	given: Italo
  URL: 'http://www.linhadecodigo.com.br/artigo/1171/conceitos-basicos-de-backup.aspx'
  accessed:
    month: 8
    year: 2014
  publisher: Dataprev
  type: article
  issued:
    year: 2012

- id: Significado2014
  title: "Significado de backup"
  URL: 'http://www.significados.com.br/backup'
  accessed:
    month: 8
    year: 2014
  publisher: Dataprev
  type: article
  issued:
    year: 2014

---