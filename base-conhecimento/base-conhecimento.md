---
date: 31 de julho de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Criação e Gestão da Base de Conhecimento de Incidentes e Problemas na DATAPREV
abstract: Este artigo, apresenta um resumo das boas práticas utilizadas no trabalho de construção da Metodologia ^[http://www-dtpnet/sites/default/files/Metodologia-Base-Conhecimento%20v2.1.pdf] sobre Gestão de Base de Conhecimento na DATAPREV, focado na resolução de incidentes, e como a base irá contribuir para a melhoria contínua dos serviços prestados.
author:
- affiliation: DEQI/DIMC
  name: Álvaro Nazaré Bonifácio
responsibility:
- affiliation: DEQI/DIMC
name: 
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Qualidade de Infraestrutura de TIC - DEQI'
tags:
- Tech0xA 
- Base Conhecimento 
- Knowledge 
- Management 
- KB 
- Gestão 
- Melhoria 
- Contínua
...

Introdução
==========

A gestão do conhecimento é um tema amplo, que trata da transformação do conhecimento tácito - aquele adquirido através da experiência e que não está formalmente documentado, em conhecimento explícito, aquele que está documentado e ficará disponível para consulta. O processo de construção da Base de Conhecimento na DATAPREV, inicialmente está focado na resolução de incidentes pelas equipes de sustentação e suporte, e também envolverá documentos técnicos que contribuam na disseminação da informação e sua transformação em conhecimento.

Desafios
==========

Disponibilizar uma Base de Conhecimento Unificada para Resolução de Incidentes e Problemas de Infraestrutura e Aplicações na DATAPREV, que possibilite aos analistas a inclusão e recuperação de documentos de conhecimento, de forma rápida e estruturada. A base ainda deverá ser 'viva', onde seus utilizadores poderão qualificar seu conteúdo, disparando fluxos que manterão seus documentos atualizados a partir de revisões, pelas equipes responsáveis.

Benefícios
==========

Um desafio constante enfrentado pela DATAPREV é cumprir seus ANS - Acordos de Nível de Serviço, estabelecidos junto aos clientes, mantendo a disponibilidade dos sistemas e em caso de paradas, sua rápida recuperação. Uma base de conhecimento bem construída, irá contribuir para superarmos tal desafio e dentre os inúmeros benefícios gerados, podemos destacar:

- Simplificar a criação, utilização, atualização e localização de documentos de conhecimento; 
- Garantir a padronização na execução dos serviços de TI;
- Reduzir o tempo de adaptação de novos funcionários;
- Diminuir o trabalho redundante;
- Aumentar a interação entre as equipes e áreas;
- Reduzir o tempo de atendimento a incidentes, principalmente no 1º nível;
- Oferecer métricas de utilização da KB que permitam a melhoria contínua do processo;
- Manter a qualidade da documentação;

Base de Conhecimento - Knowledge Base (KB)
==========

A ITIL V3[@ITIL_V3] (*Information Technology Infrastructure Library* Versão 3) define *Knowledge Base*, como *"um banco de dados que contém informações utilizadas pelo serviços de gerenciamento do conhecimento".* Em complemento, ainda segundo a ITIL, o *Knowledge Management* - KM (Gerenciamento do Conhecimento), é definido como *"um processo responsável por compartilhar perspectivas, ideias, experiências e informações, e por assegurar que esses estarão disponíveis no lugar certo e na hora certa..."* 

O *Gartner Group*[@Gartner] ^[http://www.gartner.com], em seu glossário de TI, define *Knowledge Management* como *"um processo de negócio que formaliza o gerenciamento e o uso do capital intelectual das empresas. Bases de conhecimento promovem colaboração e integração na criação, captura, organização, acesso e uso da informação..."*

Atualmente, a DATAPREV não conta com uma base de conhecimento centralizada, que facilite o acesso as informações geradas pela empresa. A utilização de bases departamentais como sites internos, planilhas e documentos armazenados em estações de trabalho, dificultam o acesso à informação e depreciam esse importante ativo da empresa. 

Base de Conhecimento para Resolução de Incidentes e Problemas
==========

Segundo a  KCS[@KCS] - *Knowledge-Centered Support*^[http://www.serviceinnovation.org/kcs/], temos uma relação de melhores práticas quanto a gestão do conhecimento, que devem ser observadas:

- Criar conteúdo como um produto para solução de problemas;
- Envolver o conteúdo criado em demandas e utilizá-lo;
- Desenvolver a KB de forma coletiva, com as experiências do dia a dia;
- Estimular o aprendizado, colaboração, compartilhamento e melhoria contínua;

Novas iniciativas devem buscar agregar valor ao negócio, e a adesão de seus colaboradores é imprescindível. Para que a isso ocorra, com foco na utilização e colaboração com a Base de Conhecimento, podemos relacionar 10 razões pela qual o Gerenciamento de Conhecimento é necessário:

1. Redução de custos nas atividades de suporte; 
1. Disponibilizar o auto serviço, onde o próprio demandante da solução poderá buscá-la;
1. Evitar retrabalho;
1. Produz oportunidades de aprendizado com experiências de outros profissionais;
1. Responde a questões recorrentes;
1. Facilita a passagem de conhecimento para novos colaboradores;
1. Melhora o tempo de resposta dos analistas;
1. Permite respostas mais consistentes às questões dos clientes;
1. Permite respostas ágeis a questões complexas;
1. Responde e resolve questões de forma rápida.

A captura do conhecimento para resolução de problemas, deve acontecer observando alguns aspectos:

- No momento da ocorrência;
- No contexto do cliente;
- Com informações sobre o ambiente;
- Com conteúdo relevante;
- Transformando o conhecimento tácito em conhecimento explícito;
- Inserção de informações a partir de um formulário ou modelo;
- De forma estruturada facilitando a leitura;
- Pesquisar na base antes de adicionar um novo conteúdo evitando duplicidades;
- Mantenha simples (princípio KISS)^[http://pt.wikipedia.org/wiki/Keep_It_Simple];

Base de conhecimento estruturada:
==========

A estrutura da base de conhecimento deve conter informações relevantes, que tornem a  localização dos documentos de conhecimento rápida e simples:

- Descrição do problema;
- Mensagem de erro;
- Sintomas;
- Palavras-Chave;
- Ambiente;
- Título;
- Resumo;
- Causa;
- Solução;
- Links relacionados à solução;
- Número único de identificação;
- Categorização;
- Data Criação;
- Data Modificação;
- Data Expiração;
- Autor;

Os documentos da Base de Conhecimento devem possuir um ciclo de vida, com estágios e acompanhamento:

- Iniciado (rascunho);
- Em análise (quanto à informação e quanto à forma);
- Publicado;
- Em revisão;
- Duplicado;
- Obsoleto.

O fluxo de vida dos documentos da Base de Conhecimento é alimentado não só pela inclusão de documentos, mas pela sua avaliação e qualificação:

**Avaliar Documento:** Ato de verificar a qualidade técnica do documento, efetuado por um técnico especialista no assunto. Preferencialmente, o passo seguinte será a avaliação do cumprimento de padrões de preenchimento, por outro profissional, com papel de Analista de Conhecimento. 

**Qualificar Documento:** Ato de verificar um documento durante a sua utilização para a execução de um serviço de TI. Desta forma, deve informar se o mesmo está adequado e se existe a necessidade de atuação para sua melhoria (correção, revisão ou documento duplicado).

Competências na base de conhecimento
==========

**Contribuidor:** aquele que escreve documentos e contribui para a Base de Conhecimento. Em geral, todos os colaboradores da empresa poderão atuar como contribuidores, iniciando o fluxo de criação de documento, que será analisado pelo Revisor;

**Revisor:** analisa o documento quanto ao cumprimento dos padrões acordados para criação de documentos, como preenchimentos de campos, utilização de modelos e atribuição de palavras-chave.

**Revisor técnico:** profissional especializado no assunto referente ao conteúdo do documento, que faz a verificação técnica.

**Publicador:** responsável por disponibilizar o documento para uso, publicando-o após o cumprimento das etapas de criação e análise.

**Gerente de Conhecimento:** Monitora e gerencia o funcionamento da Base de Conhecimento, de acordo com os indicadores apresentados.

Métricas
==========

As métricas tem como função coletar informações sobre o funcionamento da Base de Conhecimento e colaborar na aferição de sua qualidade. O processo de verificação deve ser feito periodicamente pelo seu gestor, como um ciclo PDCA ^[PDCA: Plan - Do - Check - Action (http://pt.wikipedia.org/wiki/Ciclo_PDCA)]. Desta forma, as métricas serão utilizadas para garantir que o processo está funcionando de forma eficiente e eficaz, ou ainda quanto a necessidade de alguma ação de melhoria. Um documento muito utilizado e bem qualificado indica que possui clareza e boa assertividade, mas por outro lado demonstra que determinado incidente repetitivo necessita de atenção especial e pode ser encaminhado para a gestão de problemas. Vejamos algumas métricas que poderão auxiliar na avaliação:

- Porcentagem de participação na criação / revisão de documentos.
- Quantidade de vezes que um documento foi utilizado.
- Porcentagem de utilização de documentos na resolução de chamados técnicos.
- Classificação do documento pela qualidade da informação (Muito Bom, Bom, Regular, Ruim, Muito Ruim).
- Quantidade de solicitações de atualização de documentos.
- Quantidade de solicitações de revisão de documentos.


Comunicação e liderança
==========

O patrocínio na gestão da Base de Conhecimento e envolvimento de seus  *steakholders*^[http://pt.wikipedia.org/wiki/Stakeholder] também são fatores importantes para seu sucesso:

- Alinhamento entre objetivos e equipes;
- Criação de estratégia para manutenção da Base de Conhecimento;
- Promoção das equipes de trabalho na formalização do conhecimento;
- Motivação dos colaboradores, reconhecendo e premiando seus esforços, individuais e coletivos;
- Comunicação ampla;
- Engajamento das equipes em fazer o melhor;

Base de Conhecimento para Resolução de Incidentes e Problemas na DATAPREV
==========

A partir da metodologia apresentada pelo DEQI/DIMC, o trabalho de implementação da KB continua com a operacionalização dos fluxos de vida propostos, passando pelos tipos de documentos e responsabilidades de seus usuários. O gerenciamento do conhecimento afeta diretamente a gestão de eventos e incidentes. Para reduzir o impacto nesses processos, as áreas da DIT - Diretoria de Infraestrutura de  TIC^[Tecnologia da Informação e Comunicações], foram acionadas, apontando seus documentos que serão disponibilizados na KB. Também faz parte dos entendimentos, ajustes em cerca de 300 procedimentos técnicos migrados em março/2014 da ConsoleNG[@Console], Wiki-SP e Wiki-DF, por conta de novos padrões adotados ao longo do processo, como utilização de palavras-chave, regras de formação de nomes de documentos e criação de fluxos de aprovação. Para os próximos passos, há previsão de contato e inclusão no processo de criação da KB, das áreas da DRD - Diretoria de Relacionamento, Desenvolvimento e Informações, com verificação e adição de documentos na base de conhecimento.

A ferramenta que manterá a base de conhecimento unificada na DATAPREV, será o CA SDM - *Service Desk Manager*, que é uma ferramenta ITIL *Compliance*, responsável dentre outras funções, pela manutenção do BDGC (Banco de Dados de Gerenciamento da Configuração), pela gestão de alertas e eventos, e ainda disponibiliza o módulo de Base de Conhecimento. Dessa forma, temos a garantia de uma ferramenta integrada, que facilitará o trabalho das equipes de sustentação e suporte, e outras mais que vierem a utilizar seu conteúdo. Além dos procedimentos técnicos para atendimento a incidentes, irão compor a base outros tipos de documentos como procedimentos de instalação, manuais, relatórios com informações técnicas e conhecimento sobre problemas, lições aprendidas, documentos de arquitetura e outros que possam trazer informações relevantes sobre os ambientes de TIC utilizados.

O módulo de Base de Conhecimento do SDM, permite a criação de fluxos de aprovação, onde os documentos criados deverão ser avaliados tecnicamente e também quanto a utilização de padrões, como regras de nomenclatura, utilização de palavras-chave, *templates* e categorização. 	Durante o processo de aprovação, os documentos serão classificados com o status de 'Rascunho'. Após as análises e aprovações definidas nos fluxos, o documento é publicado e fica disponível para consulta, por toda a empresa.

Com a desativação da ConsoleNG - atual ferramenta de gerenciamento de eventos e incidentes, com previsão para desligamento até o final de 2014, espera-se que a Base de Conhecimento no SDM melhore os indicadores apresentados nos gráficos a seguir, por conta de seu funcionamento 'vivo', onde a partir dos fluxos de aprovação que funcionam como 'ciclo de vida', seus utilizadores poderão qualificar os documentos e indicar necessidades de melhoria e até mesmo criação de novos documentos. 

Após a finalização da implantação da KB no SDM e sua utilização pelas equipes de sustentação e suporte, considerando como pré requisito o desligamento da ConsoleNG, relatórios gerados pela ferramenta poderão apoiar as tomadas de decisões, quanto aos casos de atendimentos que apresentam justificativas com necessidade de revisão, visando a redução de escaladas para níveis superiores e consequente diminuição no tempo de atendimento a incidentes, conforme apresentado em indicadores extraídos da própria ConsoleNG no mês 05/2014:


|**Justificativa**	             | CPRJ  | CPDF  | CPSP  |
|:------------------------------ |------:|------:|------:|
|Não existe procedimento         |  7.3% | 28.5% | 19.0% |
|Ação determina Escalada imediata| 41.6% | 43.8% | 18.5% |
|Procedimento não funcionou      | 17.7% |  1.0% |  6.6% |
|Totais                          | 66,6% | 73,3% | 44,1% |


![](imagens/artigo01-rj.png)
<p align='center'>Figura 01 - Justificativas de escaladas CPRJ em 05/2014</p>

![](imagens/artigo01-df.png)
<p align='center'>Figura 02 - Justificativas de escaladas CPDF em 05/2014</p>

![](imagens/artigo01-sp.png)
<p align='center'>Figura 03 - Justificativas de escaladas CPSP em 05/2014</p>

 
Conclusão
==========
A Base de Conhecimento Unificada de Incidentes e Problemas de Infraestrutura será uma ferramenta importante para atuação das áreas solucionadoras quanto para aquelas que necessitam de informações sobre os ambientes de TIC suportados pela DATAPREV. A participação de seus utilizadores na qualificação dos documentos promoverá a colaboração entre as áreas e o amplo conhecimento na empresa. Os indicadores de uso permitirão o acompanhamento da qualidade da informação e sua utilização. Além disso, teremos uma nova cultura em nosso dia a dia, onde o conhecimento será documentado e disponibilizado, com acompanhamento da Gestão do Conhecimento.

 

Referências
===========
[^1]: (texto aparece na nota de rodapÃ©, mas sem efeito final) [@KCS]
[^2]: [@Gartner]

---
references:

- id: Gartner
  title: "Glossário de TI"
  URL: 'http://www.gartner.com/it-glossary/km-knowledge-management'
  accessed:
    day: 23
    month: 7
    year: 2014
  publisher: Gartner
  type: article
  issued:
    year: 2014

- id: KCS
  title: "KCS - Knowledge-Centered Support"
  author:
  - family: Consortium for Service Innovation
    given: KCS
  URL: 'http://www.serviceinnovation.org/kcs/'
  accessed:
    day: 23
    month: 7
    year: 2014
  publisher: KCS
  type: article
  issued:
    year: 2014

- id: ITIL_V3
  title: "ITIL V3 - Service Operations"
  author: 
  - family: (AXELOS)
    given: Randy Steinberg
  publisher: TSO - The Stationery Office
  type: book
  issued:
    year: 2011

- id: DTPNET
  title: "Modelo de Gestão da Base de Conhecimento unificada para problemas de infraestrutura e aplicações"
  author:
  - family: DIMC
    given: Equipe Técnica
  URL: "http://www-dtpnet/sites/default/files/Metodologia-Base-Conhecimento%20v2.0.pdf"
  type: article
  publisher: Dataprev
  issue: 2.0
  issued:
    year: 2014

- id: UM
  title: "ITS Knowledge Management Process Summary"
  author: 
  - family: Callihan
    given: Lisa
  URL: 'http://www.mais.umich.edu/methodology/service-management/knowledge-mgmt-process-summary.pdf'
  type: article
  publisher: University of Michigan
  accessed:
    day: 23
    month: 7
    year: 2014
  issued:
     year: 2013

- id: Console
  title: "Sistema Console NG"
  URL: 'http://www-consoleng/scripts/s2040005.asp'
  accessed:
    day: 24
    month: 7
    year: 2014
  publisher: Dataprev
  type: webpage
  issued:
    year: 2014
---
