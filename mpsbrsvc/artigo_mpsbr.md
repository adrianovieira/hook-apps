---
date: 22 de setembro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: O **MPS.BR** e sua importância para a empresa.
abstract: Apresentar o modelo **MPS.BR** e como ele pode colaborar com a melhoria dos processos de software em nossas empresas.
author:
- affiliation: DIMC
  name: Daniel Gomes
- affiliation: DIMC
  name: Frederico Henrique Lima
- affiliation: DIMC
  name: Leandro Pissurno Candido da Silva
responsibility:
- affiliation: SUPS
  name: Anderson Gourlart
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
tags:
- Tech0xA
- Markdown
- Pandoc
- Artigos
- Git
- SCM
- Template
- Padrões
- Textos
- Produtividade
- Escritório
...

Introdução
==========
Muitas vezes é subestimado a importâncias dos processos^[Processo (<http://http://pt.wikipedia.org/wiki/Processo>)] dentro das organizações, descrevendo-os como um mero instrumento burocrático, criado com o intuito de controlar e que cada profissional está fazendo, limitando o talento dos profissionais de TI, levando-os gradualmente à perda da capacidade de criar e inovar em situações de adversidades.<br/>
Na verdade, processos existem porque representam a experiência acumulada de décadas de trabalho, organizadas por empresas e profissionais que compilaram as melhores práticas para lidar mais pró-ativamente com os riscos inerentes à execução dos mais variados serviços de TI, incorporando mecanismos de controle que reduzem o nível de erros dos profissionais, levando-os de forma mais segura à finalização dos trabalhos.<br/>
Os processos possibilitam que os serviços de TI sejam impessoais, ou seja, independente de quem executará os trabalhos, serão realizados as mesmas atividades, avaliados os mesmos parâmetros, produzidos os mesmos artefatos, gerenciados pelo mesmo conjunto de indicadores. Com este nível de padronização dos trabalhos, os projetos tornam-se mais previsíveis, possibilitando que riscos sejam monitorados e mitigados com alto grau de precisão e controle.<br/>
Sem um processo formalmente estabelecido, os profissionais buscariam caminhos diferentes para realizar as mesmas atividades, trazendo mais variáveis e incertezas no projeto, aumentando-os consideravelmente os riscos de insucesso. Nestas condições, a simples troca de um profissional pode desestabilizar toda uma cadeia de serviços de TI, demonstrando a fragilidade de todo o modelo operacional que a organização está submetida.<br/>
Os processo foram modelados para conduzirem os profissionais ao caminho mais controlado e seguro, possibilitando que qualquer membro da organização, com perfil e treinamento adequado, possam atender continuamente os projetos e manter os níveis de serviços dentro de uma variabilidade aceitável.<br/>
Os processos não podem ser estáticos e devem ser gradualmente aprimorados pela organização, à medida que a condução de novos projetos revelem deficiências operacionais que deveriam ser minimizadas, evitando gerar fontes de instabilidade e incertezas futuras.
Uma empresa busca a definição de processos corporativos, de forma a garantir que toda sua estrutura operacional esteja baseada num único modelo de trabalho, não em ilhas isoladas de organização. A adoção de padrões corporativos garante que uma determinada inovação ou aperfeiçoamento metodológico seja aplicado em todas unidades operacionais, viabilizando a melhoria contínua a longo prazo.<br/>
Portanto, a formalização de processos dentro das estruturas de TI devem ser encarados como uma estratégia para gerenciamento de serviços cada vez mais segmentada e complexa. Não é por acaso que a busca pela adequação por modelos como MPS-BR, focam explicitamente na melhoria dos processos que, muitas vezes, são atropelados pela correria do dia a dia.<br/>
Este artigo visa prover um overview sobre o Modelo de Referência MPS para Serviços e mostrar a importância da certificação principalmente para empresas que prestam serviços de tecnologia da informação para órgãos governamentais como é o caso da Dataprev.

Desafios
========
De acordo com o **Diário Oficial da União**[D.O.U (<http://www.jusbrasil.com.br/diarios/DOU/>)] do dia 03/08/2007 o TCU (Tribunal de Contas da União) recomendou à Secretaria de Logística e Tecnologia da Informação (SLTI) a adoção do modelo MPS.BR, como sendo requisitos mínimos sobre a licitação e a contratação de serviços de TI.<br/>
Um dos fatos que voltou a atenção para esse modelo específico foi que ele é um dos modelos que já contam com investimento público brasileiro.<br/>
Esta recomendação comprova a importância que o modelo e a certificação MPS.BR vem ganhando junto ao mercado, desde a sua criação, em 2004, pela Softex.<br/>
Como exemplos de de licitações que usam o modelo como critério de pontuação técnica temos as do Departamento de Engenharia e Construção do Ministério da Defesa, do Departamento de Estradas de Rodagem de Minas Gerais (DER/MG) e do Tribunal de Contas do DF.<br/>
Entre as companhias vinculadas as diversas esferas do governo que possuem a certificação MPS.BR podemos citar a Prodemge (Companhia de T.I. do Estado de Minas Gerais), Prodabel (Empresa de Informática e Informação do Município de Belo Horizonte, Prodam (Empresa de Tecnologia da Informação e Comunicação do Mun. SP) dentre outras.<br/>
Dessa forma nota-se a importância da adoção do modelo MPS.BR Serviços para a melhoria dos processos da DIT e por consequência a conformidade com licitações que envolvem tecnologia da informação visando novos contratos a serem firmados com a Dataprev.

Benefícios e/ou recomendações
=============================
Para se alcançar níveis mais altos de maturidade no **CMMI**^[@WikipediaCMMI] é necessário muito tempo e esforço juntamente com um alto custo. O custo para realizar o processo de certificação no CMMI será gasto algo em torno de US$1.000.000,00 enquanto uma certificação **MPS.BR**^[@WikipediaMPSBR] custa em média de R$70.000,00. Além disso pode-se citar outros benefícios como:<br/>
- Melhoria de processos mais gradual.<br/>
- Com mais níveis que o CMMI o MPS.BR torna as melhorias mais fáceis de serem alcançadas.<br/>
- Totalmente compatível com o CMMI e normas internacionais ISO.<br/>
- Muitas licitações governamentais já exigem níveis de maturidade MPS.BR.<br/>

O Modelo de Referência MPS.BR para Serviços (MR-MPS-SV)
=======================================================

Com base na necessidade de um modelo de maturidade que fosse especificamente focado em empresas prestadoras de serviços, o Modelo de referência para Serviços foi criado para propiciar a melhoria nos processo em empresas prestadoras de serviços de TI aonde a qualidade é um fator de sucesso e por isso a adoção de um modelo baseado em padrões internacionalmente reconhecidos é essencial.<br/>
Ele vem para apoiar a melhoria dos processos de serviços como também para oferecer uma avaliação que certifique que a empresa tem adesão a melhores práticas de gestão dos processos para o cliente.<br/>
Baseado nas práticas ITIL, na Norma Internacional ISO/IEC 20000 e no modelo CMMI-SVC e serve para melhorar tanto os processos de serviços quanto o desempenho nos negócios das organizações públicas e privadas de qualquer porte.

### Conceitos ###

**Serviço**<br/>
“Um produto que é intangível e não armazenável” (CMMI-SVC 2010)<br/>
“Uma forma de entregar valor aos clientes, facilitando os resultados que os clientes desejam atingir sem ter a propriedade de custos e riscos específicos” (ITILv2011)<br/>
“Meio de entregar valor para o cliente por meio da facilitação de resultados que o cliente deseja atingir” (ISO/IEC 20000-1:2011)<br/>
**Serviço de TI**<br/>
“Um serviço fornecido por um provedor de serviços de TI. Um serviço de TI é constituído por uma combinação de tecnologia da informação, pessoas e processos.” (ITILv2011)<br/>
**Provedor de Serviços de TI**<br/>
“Um provedor de serviços que provê serviços de TI para clientes internos ou externos” (ITILv2011)<br/>
**Componente do Serviço**<br/>
“É uma parte do serviço final ou algo usado no seu desenvolvimento (por exemplo um subproduto, um processo, uma ferramenta) que faz parte da entrega. Os componentes são integrados em sucessivos níveis para compor o serviço final” (CMMI-SVC 2010)<br/>
“Unidade de serviço que, quando combinada com outras unidades, irá entregar um serviço completo.” (ISO/IEC 20000-1:2011)<br/>
**Gerenciamento de Serviços**<br/>
“Um conjunto de capacidades organizacionais especializadas para prover valor aos clientes na forma de serviços.” (ITILv2011)<br/>
“Conjunto de capacidades e processos para dirigir e controlar as atividades e recursos do provedor para o projeto, transição, entrega e melhoria dos serviços para atender aos requisitos dos serviços.” (ISO/IEC 20000-1:2011)<br/>
**Provedor de Serviços**<br/>
“Uma organização que provê serviços para um ou mais clientes internos ou externos.” (ITILv2011)<br/>
“Organização ou parte de uma organização que gerencia ou entrega serviços ao cliente” (ISO/IEC 20000-1:2011)<br/>
**Sistema de Gerenciamento de Serviços**<br/>
“Uma combinação integrada e interdependente dos recursos e componentes que satisfazem os requisitos do serviço.” (CMMI-SVC 2010)<br/>
“Sistema de gerenciamento para dirigir e controlar as atividades de gerenciamento de serviços de um provedor de serviços.” (ISO/IEC 20000-1:2011)<br/>
**Gerenciamento de Serviços de TI (GSTI)**<br/>
“A implementação e o gerenciamento de serviços de TI de qualidade que atendem às necessidades do negócio. O gerenciamento de serviços de TI é executado por provedores de serviços de TI por meio de uma combinação adequada de pessoas, processos e tecnologia da informação” (ITILv2011)<br/>
**Acordo de Nível de Serviço (ANS)**<br/>
“Um acordo documentado entre o provedor de serviços e o cliente que identifica os serviços e as metas dos serviços” (ISO/IEC 20000-1:2011)<br/>
“Um acordo entre um provedor de serviços de TI e um ciente. Um SLA descreve o serviço de TI, documenta as metas de nível de serviço e especifica as responsabilidades do provedor de serviços de TI e do cliente. Um único SLA pode cobrir diversos serviços de TI ou diversos clientes.” (ITILv2011)<br/>
**Incidente**<br/>
“A indicação de uma interferência real ou potencial na execução normal de um serviço” (ISO/IEC 20000-1:2011)<br/>
“Uma interrupção não planejada ou a redução da qualidade de um serviço de TI. A falha de um item de configuração que ainda não afetou o serviço também é um incidente.” (ITILv2011)<br/>
**Problema**<br/>
“A causa de um ou mais incidentes. A causa normalmente não é conhecida no momento do registro do problema e o processo de gerenciamento de problema é responsável pela investigação posterior.” (ITILv2011)<br/>
“Causa raiz de um ou mais incidentes.” (ISO/IEC 20000-1:2011)<br/>
**Orçamento e Contabilização de Serviços**<br/>
“A gestão orçamentária e contábil dos elementos envolvidos na prestação de serviços“(ISO/IEC 20000-1:2011)<br/>
**Relato de Serviços**<br/>
“Geração de informações sobre os serviços prestados conforme as necessidades dos envolvidos” (ISO/IEC 20000-1:2011)<br/>
**Requisito de Serviço**<br/>
“Uma condição ou capacidade exigida para solucionar um problema ou atingir um objetivo” (ISO/IEC 20000-1:2011)<br/>
“Um projeto é um empreendimento temporário conduzido para gerar um produto, serviço ou resultado específico.”<br/>
**Operação**<br/>
Uma operação é uma função organizacional que realiza a execução contínua de atividades que produzem o mesmo produto ou fornecem o mesmo serviço repetidamente.” (PMBOK 5ª edição 2012)<br/>
**Capacidade do processo**<br/>
Uma caracterização da habilidade do processo atingir aos objetivos de negócio atuais ou futuros.<br/>
**Atributo de processo (AP)**<br/>
Uma característica mensurável da capacidade do processo aplicável a qualquer processo<br/>
Cada Atributo de Processo tem um ou vários Resultados do Atributo de Processo (RAP)<br/>
**Resultados esperados dos atributos do processo (RAP)**<br/>
- Um resultado observável do sucesso do alcance do propósito do processo<br/>


#### Estrutura do Modelo ####

![Estrutura do modelo](/imagens/estrutura_modelo.jpg "Estrutura do Modelo")

**ISO/IEC 12207**<br/>
- Estabelece uma arquitetura comum para os processos do ciclo de vida do software

**CMMI-DEV**<br/>
- Todos os requisitos das áreas de processo do CMMI-DEV estão presentes no MPS.BR
- O MPS.BR contém mais áreas de processo, logo é mais completo.

**ISO/IEC 15504**<br/>
- Norma para avaliação e melhoria de processos de software

**Modelo de Referência (MR-MPS)**<br/>
- Contém os requisitos que os processos das organizações devem atender para estar em conformidade com o modelo
- Descrito pelo Guia Geral

**Método de Avaliação (MA-MPS)**<br/>
- Orienta a execução de uma avaliação de conformidade ao modelo
- Descrito pelo Guia de Avaliação

**Modelo de Negócio (MN-MPS)**<br/>
- Descreve regras de negócio para a implementação do modelo

**Documentos Complementares**<br/>
**Guia de Aquisição**<br/>
- Contém boas práticas para aquisição de software e serviços correlatos

**Guia de Implementação**<br/>
- Sugere formas de implementar cada um dos níveis do MR-MPS


##### Relacionamento entre Atributos de Processo (AP) & Resultados esperados dos Atributos de Processo (RAP) #####

| Atributo de Processo                                        | Mede o quanto...                                                                                                                                                                                                     | Exemplos de resultados esperados                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AP1.1 - O processo é executado|o processo atinge seu propósito.                                                                                                                                                                                     | RAP 1 - O processo atinge seus resultados definidos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AP2.1 - O processo é gerenciado| a execução do processo é gerenciada.                                                                                                                                                                                 | RAP 2 - Existe uma política organizacional estabelecida e mantida para o processo;</br>RAP 3 - A execução do processo é planejada;</br>RAP 4 - (Para o nível G)¹. A execução do processo é monitorada e ajustes são realizados;</br>RAP 4 - (A partir do nível F). Medidas são planejadas e coletadas para monitoração da execução do processo e ajustes são realizados;</br>RAP 5 - As informações e os recursos necessários para a execução do processo são identificados e disponibilizados;</br>RAP 6 - (Até o nível F)² As responsabilidades e a autoridade para executar o processo são definidas, atribuídas e comunicadas;</br>RAP 6 - (A partir do nível E) Os papéis requeridos, responsabilidades e autoridade para execução do processo definido são atribuídos e comunicados;</br>RAP 7 - As pessoas que executam o processo são competentes em termos de formação, treinamento e experiência;</br>RAP 8 - A comunicação entre as partes interessadas no processo é planejada e executada de forma a garantir o seu envolvimento;</br>RAP 9 - (Até o nível F)³ Os resultados do processo são revistos com a gerência de alto nível para fornecer visibilidade sobre a sua situação na organização;</br>RAP 9 - (A partir do nível E) Métodos adequados para monitorar a eficácia e adequação do processo são determinados e os resultados do processo são revistos com a gerência de alto nível para fornecer visibilidade sobre a sua situação na organização;</br>RAP 10 - (Para o nível G)⁴ O processo planejado para o trabalho é executado.<br/>RAP 10 - (A partir do nível F) A aderência dos processos executados às descrições de processo, padrões e procedimentos é avaliada objetivamente e são tratadas as não conformidades.|
| AP2.2 - Os produtos de trabalho do processo são gerenciados | os produtos de trabalho produzidos pelo processo são gerenciados apropriadamente.                                                                                                                                    | RAP 11 - Os requisitos dos produtos de trabalho do processo são identificados;</br> RAP 12 - Requisitos para documentação e controle dos produtos de trabalho são estabelecidos;</br> RAP 13 - Os produtos de trabalho são colocados em níveis apropriados de controle;</br> RAP 14 - Os produtos de trabalho são avaliados objetivamente com relação aos padrões, procedimentos e requisitos aplicáveis e são tratadas as não conformidades.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| AP3.1 - O processo é definido| um processo padrão é mantido para apoiar a implementação do processo  definido.                                                                                                                                      | RAP 15 - Um processo padrão é descrito, incluindo diretrizes para sua adaptação;</br> RAP 16 - A sequência e interação do processo padrão com outros processos são determinadas;</br> RAP 17 - Os papéis e competências requeridos para executar o processo são identificados como parte do processo padrão;</br> RAP 18 - A infra-estrutura e o ambiente de trabalho requeridos para executar o processo são identificados como parte do processo padrão.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| AP 3.2 - O processo está implementado| o processo padrão é efetivamente implementado como um processo definido para atingir seus resultados.                                                                                                                | RAP 19 - Um processo definido é implementado baseado nas diretrizes para seleção e/ou adaptação do processo padrão;</br> RAP 20 - A infraestrutura e o ambiente de trabalho requeridos para executar o processo definido são disponibilizados, gerenciados e mantidos;</br> RAP 21 - Dados apropriados são coletados e analisados, constituindo uma base para o entendimento do comportamento do processo, para demonstrar a adequação e a eficácia do processo, e avaliar onde pode ser feita a melhoria contínua do processo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AP 4.1 - O processo é medido| os resultados de medição usados para assegurar que a execução do processo atinge os seus objetivos de desempenho e apoia o alcance dos objetivos de negócios definidos.                                              | RAP 22 - As necessidades de informação dos usuários dos processos, requeridas para apoiar objetivos de negócio relevantes da organização, são identificadas;</br> RAP 23 - Objetivos de medição organizacionais dos processos e/ou subprocessos são derivados das necessidades de informação dos usuários do processo;</br> RAP 24 - Objetivos quantitativos organizacionais de qualidade e de desempenho dos processos e/ou subprocessos são definidos para apoiar os objetivos de negócio;</br> RAP 25 - Os processos e/ou subprocessos que serão objeto de análise de desempenho são selecionados a partir do conjunto de processos padrão da organização e das necessidades de informação dos usuários dos processos;</br> RAP 26 - Medidas, bem como a frequência de realização de suas medições, são identificadas e definidas de acordo com os objetivos de medição do processo/subprocesso e os objetivos quantitativos de qualidade e de desempenho do processo;</br> RAP 27 - Resultados das medições são coletados, analisados, utilizando técnicas estatísticas e outras técnicas quantitativas apropriadas, e são comunicados para monitorar o alcance dos objetivos quantitativos de qualidade e de desempenho do processo/subprocesso;</br> RAP 28 - Resultados de medição são utilizados para caracterizar o desempenho do processo/subprocesso. RAP 29 - Modelos de desempenho do processo são estabelecidos e mantidos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| AP 4.2 - O processo é controlado| o processo é controlado estatisticamente para produzir um processo estável, capaz e previsível dentro de limites estabelecidos.                                                                                      | RAP 30 - Técnicas de análise e de controle para a gerência quantitativa dos processos/subprocessos são identificadas e aplicadas quando necessário;</br> RAP 31 - Limites de controle de variação são estabelecidos para o desempenho normal do processo;</br> RAP 32 - Dados de medição são analisados com relação a causas especiais de variação;</br> RAP 33 - Ações corretivas e preventivas são realizadas para tratar causas especiais, ou de outros tipos, de variação;</br> RAP 34 - Limites de controle são restabelecidos, quando necessário, seguindo as ações corretivas, de forma que os processos continuem estáveis, capazes e previsíveis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| AP5.1 - O processo é objeto de melhorias e inovações| as mudanças no processo são identificadas a partir da análise de defeitos, problemas, causas comuns de variação do desempenho e da investigação de enfoques inovadores para a definição e implementação do processo. | RAP 35 - Objetivos de negócio da organização são mantidos com base no entendimento das estratégias de negócio e resultados de desempenho do processo;</br> RAP 36 - Objetivos de melhoria do processo são definidos com base no entendimento do desempenho do processo, de forma a verificar que os objetivos de negócio relevantes são atingíveis;</br> RAP 37 - Dados que influenciam o desempenho do processo são identificados, classificados e selecionados para análise de causas;</br> RAP 38 - Dados selecionados são analisados para identificar causas raiz e propor soluções aceitáveis para evitar ocorrências futuras de resultados similares ou incorporar melhores práticas no processo;</br> RAP 39 - Dados adequados são analisados para identificar causas comuns de variação no desempenho do processo;</br> RAP 40 - Dados adequados são analisados para identificar oportunidades para aplicar melhores práticas e inovações com impacto no alcance dos objetivos de negócio;</br> RAP 41 - Oportunidades de melhoria derivadas de novas tecnologias e conceitos de processo são identificadas, avaliadas e selecionadas com base no impacto no alcance dos objetivos de negócio;</br> RAP 42 - Uma estratégia de implementação para as melhorias selecionadas é estabelecida para alcançar os objetivos de melhoria do processo e para resolver problemas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| AP5.2 - O processo é otimizado continuamente| as mudanças na definição, gerência e desempenho do processo têm impacto efetivo para o alcance dos objetivos relevantes de melhoria do processo.                                                                     | RAP 43 - O impacto de todas as mudanças propostas é avaliado com relação aos objetivos do processo definido e do processo padrão;</br> RAP 44 - A implementação de todas as mudanças acordadas é gerenciada para assegurar que qualquer alteração no desempenho do processo seja entendida e que sejam tomadas as ações pertinentes;</br> RAP 45 - As ações implementadas para resolução de problemas e melhoria no processo são acompanhadas, com uso de técnicas estatísticas e outras técnicas quantitativas, para verificar se as mudanças no processo corrigiram o problema e melhoraram o seu desempenho;</br> RAP 46 - Dados da análise de causas e de resolução são armazenados para uso em situações similares.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

¹ O RAP 4 tem exigências diferentes para o nível G e para os níveis posteriores.<br/>
² O RAP 6 tem exigências diferentes para os Níveis G e F e para o níveis posteriores.<br/>
³ O RAP 9 tem exigências diferentes para os Níveis G e F e para os níveis posteriores.<br/>
⁴ O RAP 10 tem exigências diferentes para o Nivel G e para os níveis posteriores.<br/>


#### Níveis de Maturidade ####
Estabelecem patamares de evolução dos processos, caracterizando estágios de melhoria dos processos.
Cada um dos níveis possui um perfil de processos que indica onde a organização deve concentrar esforços.
**O progresso se dá alcançando**
- O propósito de cada processo do nível.
- Os resultados esperados destes processos.
- Os RAP de cada Atributo de Processo do nível.

| Níveis MR-MPS   |      Equivalência no CMMI      |
|----------|:-------------:|
| A. Em otimização |  Nível 5: Em otimização |
| B. Gerenciado Quantitativamente |    Nível 4: Ger. Quantitativamente   |
| C. Definido | Nível 3: Definido |
| D. Largamento Definido |   |
| E. Parcialmente Definido |       |
| F. Gerenciado | Nível 2: Gerenciado |
| G. Parcialmente Gerenciado |   |

Nível G - Parcialmente Gerenciado
---------------------------------
O nível de maturidade G é composto pelos processos Entrega de Serviços, Gerência de Incidentes, Gerência de Nível de Serviço, Gerência de Requisitos e Gerência de Trabalhos. Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1 e AP 2.1.

| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1 e 2.1 |  Entrega de Serviços - ETS |
| AP 1.1 e 2.1 |  Gerência de Incidentes – GIN |
| AP 1.1 e 2.1 |  Gerência de Nível de Serviço - GNS |
| AP 1.1 e 2.1 |  Gerência de Requisitos – GRE |
| AP 1.1 e 2.1 |  Gerência de Trabalhos – GTR |

Atributos de processo:

* AP 1.1 – O processo é executado

* AP 2.1 – O processo é gerenciado

Nível F - Gerenciado
---------------------------------
O nível de maturidade F é composto pelos processos do nível de maturidade anterior (G) acrescidos dos processos Aquisição, Gerência de Configuração, Garantia da Qualidade, Gerência de Problemas, Gerência de Portfólio de Trabalhos e Medição. Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1, AP 2.1 e AP 2.2.

| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1, 2.1 e 2.2 |  Aquisição – AQU |
| AP 1.1, 2.1 e 2.2 |  Gerência de Configuração – GCO |
| AP 1.1, 2.1 e 2.2 |  Garantia da Qualidade – GQA |
| AP 1.1, 2.1 e 2.2 |  Gerência de Problemas – GPL |
| AP 1.1, 2.1 e 2.2 |  Gerência de Portfólio de Trabalhos – GPT |
| AP 1.1, 2.1 e 2.2 |  Medição – MED |

Atributos de processo acrescentados:

* AP 2.2 – Os produtos de trabalho do processo são gerenciados. 

Obs.: O processo "Aquisição – AQU" pode ser excluído, desde que não executado pela organização

Nível E - Parcialmente Definido
---------------------------------
O nível de maturidade E é composto pelos processos dos níveis de maturidade anteriores (G e F), acrescidos dos processos Avaliação e Melhoria do Processo Organizacional, Definição do Processo Organizacional, Gerência de Mudanças, e Gerência de Recursos Humanos. O processo Gerência de Trabalhos sofre sua primeira evolução, retratando seu novo propósito: gerenciar o trabalho com base no processo definido para o trabalho e nos planos integrados. Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1, AP 2.1, AP 2.2, AP 3.1 e AP 3.2.

| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Avaliação e Melhoria do Processo Organizacional – AMP |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Definição do Processo Organizacional – DFP |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Mudanças – GMU |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Recursos Humanos – GRH |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Trabalhos – GTR (evolução) |

Atributos de processo acrescentados: 

* AP 3.1 – O processo é definido 
* AP 3.2 – O processo é implementado 
 
Obs.: O processo de Ger. de Recursos Humanos acrescenta requisitos relativos a Aquisição de Pessoal e Ger. de Conhecimento

Nível D - Largamente Definido
---------------------------------
O nível de maturidade D é composto pelos processos dos níveis de maturidade anteriores (G ao E), acrescidos dos processos Desenvolvimento do Sistema de Serviços9 e Orçamento e Contabilização para Serviços. Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1, AP 2.1, AP 2.2, AP 3.1 e AP 3.2.

| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Desenvolvimento do Sistema de Serviços – DSS |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Orçamento e Contabilização de Serviços – OCS |

Nenhum atributo de processo acrescentado

Nível C - Definido
---------------------------------
O nível de maturidade C é composto pelos processos dos níveis de maturidade anteriores (G ao D), acrescidos dos processos Gerência de Capacidade, Gerência da Continuidade e Disponibilidade dos Serviços, Gerência de Decisões, Gerência de Liberação, Gerência da Segurança da Informação, Gerência de Riscos e Relato de Serviços. Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1, AP 2.1, AP 2.2, AP 3.1 e AP 3.2.

| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Capacidade – GCA |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência da Continuidade e Disponibilidade dos Serviços – GCD |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Decisões – GDE |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Liberação – GLI |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência de Riscos – GRI |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Gerência da Segurança da Informação - GSI |
| AP 1.1, 2.1, 2.2, 3.1 e 3.2 |  Relato de Serviços – RLS |

Nenhum atributo de processo acrescentado

Nível B - Gerenciado Quantitativamente
---------------------------------
Este nível de maturidade é composto pelos processos dos níveis de maturidade anteriores (G ao C). Neste nível o processo de Gerência de Trabalhos sofre sua segunda evolução, sendo acrescentados novos resultados para atender aos objetivos de gerenciamento quantitativo. Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1, AP 2.1, AP 2.2, AP 3.1 e AP 3.2 e os RAP 22 a RAP 25 do AP 4.1. A implementação dos processos selecionados para análise de desempenho deve satisfazer integralmente os atributos de processo AP 4.1 e AP 4.2.


| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1, 2.1, 2.2, 3.1, 3.2, 4.1 e 4.2 |  Gerência de Trabalhos – GTR (evolução) |

Atributos de Processo acrescentados:

* AP 4.1- O processo é medido
* AP 4.2 - O processo é controlado Obs.: estes Atributos de Processo equivalem, no CMMI, à área de processo "Desempenho dos Processos da Organização"

Nível A - Em Otimização
---------------------------------
Este nível de maturidade é composto pelos processos dos níveis de maturidade anteriores (G ao B). Neste nível a implementação dos processos deve satisfazer os atributos de processo AP 1.1, AP 2.1, AP 2.2, AP 3.1, AP 3.2 e os RAP 22 a RAP 25 do AP 4.1. A implementação dos processos selecionados para análise de desempenho deve satisfazer integralmente os atributos de processo AP 4.1 e AP 4.2. Os atributos de processo AP 5.1 e AP 5.2 devem ser integralmente satisfeitos pela implementação de pelo menos um dos processos selecionados para análise de desempenho.
Este nível não possui processos específicos.

| AP's   |      Processos      |
|----------|:-------------:|
| AP 1.1, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1 e 5.2 |  Nenhum processo acrescentado |

Atributos de Processo acrescentados:

* AP 5.1- O processo é objeto de melhorias e inovações
* AP 5.2 – O processo é otimizado continuamente Obs.: Estes dois atributos de processo tratam do conteúdo dos processos "Implantação de inovações na organização" e "Análise e resolução de causas", do CMMI.

Descrição detalhada dos processos
================================= 
Nessa seção os processos são descritos em termos de propósito e resultados esperados. Os processos estão descritos ordenados pelo nível de maturidade de forma crescente, sendo que cada nível inclui os processos do nível anterior.


Nível G – Parcialmente Gerenciado
---------------------------------

**Processo: Entrega de Serviços – ETS** <br />
Propósito: Entregar os serviços em conformidade com os acordos de serviços.<br />
Resultados esperados: 

* Uma estratégia para entrega e operação de serviços é estabelecida e mantida;
* A disponibilidade dos elementos necessários para a prestação do serviço é confirmada;
* O sistema de serviços é colocado em operação para entregar os serviços acordados;
* A manutenção do sistema de serviços é realizada para garantir a continuidade da entrega dos serviços.

**Processo: Gerência de Incidentes – GIN** <br />
Propósito: Restaurar os serviços acordados e cumprir as solicitações de serviços dentro de um Acordo de Nível de Serviço (ANS).<br />
Resultados esperados: 

* Uma estratégia para o gerenciamento de incidentes e solicitação de serviços é estabelecida e mantida;
* Um sistema de gerenciamento e controle de incidentes e solicitação de serviços é estabelecido e mantido;
* Incidentes e solicitações de serviços são registrados e classificados;
* Incidentes e solicitações de serviços são priorizados e analisados;
* Incidentes e solicitações de serviços são resolvidos e encerrados;
* Incidentes e solicitações de serviços que não progrediram conforme os acordos de nível de serviço são escalonados,conforme pertinente;
* Informações a respeito da situação ou progresso de um incidente relatado ou solicitação de serviço são comunicadas às partes interessadas.

**Processo: Gerência de Nível de Serviço – GNS** <br />
Propósito: Garantir que os objetivos dos acordos de nível de serviço para cada cliente sejam atendidos.<br />
Resultados esperados: 

* Serviços e dependências são identificadas;
* Objetivos de nível de serviço e soluções características para serviços são definidas em um Acordo de Nível de Serviço (ANS);
* Os serviços são monitorados e comparados com os Acordos de Nível de Serviço (ANS);
* O desempenho do nível do serviço em relação aos objetivos do nível de serviço é comunicado às partes interessadas;
* Alterações nos requisitos de serviço são refletidas no Acordo de Nível de Serviço (ANS).

**Processo: Gerência de Requisitos – GRE** <br />
Propósito: Gerenciar os requisitos de trabalho e dos componentes de trabalho e identificar inconsistências entre os requisitos, os planos de trabalho e os produtos de trabalho.<br />
Resultados esperados: 

* O entendimento dos requisitos é obtido junto aos fornecedores internos ou externos de requisitos;
* Os requisitos são avaliados com base em critérios objetivos e um comprometimento da equipe técnica com estes requisitos é obtido;
* A rastreabilidade bidirecional entre os requisitos e os produtos de trabalho é estabelecida e mantida;
* Revisões em planos e produtos derivados do trabalho são realizadas visando identificar e corrigir inconsistências em relação aos requisitos;
* Mudanças nos requisitos são gerenciadas ao longo do trabalho.

**Processo: Gerência de Trabalhos – GTR** <br />
Propósito: Estabelecer e manter planos que definem as atividades, recursos e responsabilidades do trabalho a ser realizado, bem como prover informações sobre o seu andamento que permitam a realização de correções quando houver desvios significativos em seu desempenho. O propósito deste processo evolui à medida que a organização cresce em maturidade. Assim, a partir do nível E, alguns resultados evoluem e outros são incorporados, de forma que a gerência de trabalhos passe a ser realizada com base no processo definido para o trabalho e nos planos integrados. No nível B, a gerência de trabalhos passa a ter um enfoque quantitativo, refletindo a alta maturidade que se espera da organização. Novamente, alguns resultados evoluem e outros são incorporados.<br />
Resultados esperados: 

* O escopo do trabalho é definido;
* As tarefas e os produtos derivados do trabalho são dimensionados utilizando métodos apropriados;
* O modelo e as fases do ciclo de vida do trabalho são definidos;
* (Até o nível F) O esforço e o custo para a execução das tarefas e dos produtos de trabalho são estimados com base em dados históricos ou referências técnicas;
* (A partir do nível E) O planejamento e as estimativas das tarefas do trabalho são feitos baseados no repositório de estimativas e no conjunto de ativos de processo organizacional;
* O orçamento e o cronograma do trabalho, incluindo a definição de marcos e pontos de controle, são estabelecidos e mantidos;
* Os riscos do trabalho são identificados e o seu impacto, probabilidade de ocorrência e prioridade de tratamento são determinados e documentados;
* Os recursos humanos para o trabalho são planejados considerando o perfil e o conhecimento necessários para executá-lo;
* (Até o nível F) Os recursos e o ambiente de trabalho necessários para executar o trabalho são planejados;
* (A partir do nível E) Os recursos e o ambiente de trabalho necessários para executar os trabalhos são planejados a partir dos ambientes padrão de trabalho da organização;
* Os dados relevantes do trabalho são identificados e planejados quanto à forma de coleta, armazenamento e distribuição. Um mecanismo é estabelecido para acessá-los, incluindo, se pertinente, questões de privacidade e segurança;
* Um plano geral para a execução do trabalho é estabelecido com a integração de planos específicos;
* A viabilidade de atingir as metas do trabalho é explicitamente avaliada considerando restrições e recursos disponíveis. Se necessário, ajustes são realizados;
* O Plano do Trabalho é revisado com todos os interessados e o compromisso com ele é obtido e mantido;
* O escopo, as tarefas, as estimativas, o orçamento e o cronograma do trabalho são monitorados em relação ao planejado;
* Os recursos materiais e humanos bem como os dados relevantes do trabalho são monitorados em relação ao planejado;
* Os riscos são monitorados em relação ao planejado;
* O envolvimento das partes interessadas no trabalho é planejado, monitorado e mantido;
* Revisões são realizadas em marcos do trabalho e conforme estabelecido no planejamento;
* Registros de problemas identificados e o resultado da análise de questões pertinentes, incluindo dependências críticas, são estabelecidos e tratados com as partes interessadas;
* Ações para corrigir desvios em relação ao planejado e para prevenir a repetição dos problemas identificados são estabelecidas, implementadas e acompanhadas até a sua conclusão;
* (A partir do nível E) Equipes envolvidas no trabalho são estabelecidas e mantidas a partir das regras e diretrizes para estruturação, formação e atuação;
* (A partir do nível E) Experiências relacionadas aos processos contribuem para os ativos de processo organizacional;
* (A partir do nível E) Um processo definido para o trabalho é estabelecido de acordo com a estratégia para adaptação do processo da organização;
* (A partir do nível B) Os objetivos de qualidade e de desempenho do processo definido para o trabalho são estabelecidos e mantidos;
* (A partir do nível B) O processo definido para o trabalho que o possibilita atender seus objetivos de qualidade e de desempenho é composto com base em técnicas estatísticas e outras técnicas quantitativas;
* (A partir do nível B) Subprocessos e atributos críticos para avaliar o desempenho e que estão relacionados ao alcance dos objetivos de qualidade e de desempenho do processo do trabalho são selecionados;
* (A partir do nível B) Medidas e técnicas analíticas são selecionadas para serem utilizadas na gerência quantitativa;
* (A partir do nível B) O desempenho dos subprocessos escolhidos para gerência quantitativa é monitorado usando técnicas estatísticas e outras técnicas quantitativas;
* (A partir do nível B) O trabalho é gerenciado usando técnicas estatísticas e outras técnicas quantitativas para determinar se seus objetivos de qualidade e de desempenho do processo serão atingidos;
* (A partir do nível B) Questões que afetam os objetivos de qualidade e de desempenho do processo do trabalho são alvo de análise de causa raiz.


Nível F – Gerenciado
--------------------

**Processo: Aquisição – AQU** <br />
Propósito: Gerenciar a aquisição de serviços e produtos que satisfaçam às necessidades expressas pelo adquirente.<br />
Resultados esperados: 

* As necessidades de aquisição, as metas, os critérios de aceitação do serviço ou produto, os tipos e a estratégia de aquisição são definidos;
* Os critérios de seleção do fornecedor são estabelecidos e usados para avaliar os potenciais fornecedores;
* O fornecedor é selecionado com base na avaliação das propostas e dos critérios estabelecidos;
* Um acordo que expresse claramente as expectativas, responsabilidades e obrigações de ambas as partes (cliente e fornecedor) é estabelecido e negociado entre elas;
* Um serviço ou produto que satisfaça a necessidade expressa pelo cliente é adquirido baseado na análise dos potenciais candidatos;
* A aquisição é monitorada de forma que as condições especificadas sejam atendidas, tais como custo, cronograma e qualidade, gerando ações corretivas quando necessário;
* O serviço ou produto é entregue e avaliado em relação ao acordado e os resultados são documentados;
* O serviço ou produto adquirido é incorporado ao trabalho, caso pertinente.

**Processo: Gerência de Configuração – GCO** <br />
Propósito: Estabelecer e manter a integridade de todos os produtos de trabalho de um processo ou trabalho e disponibilizá-los a todos os envolvidos.<br />
Resultados esperados: 

* Um Sistema de Gerência de Configuração é estabelecido e mantido;
* Os itens de configuração são identificados com base em critérios estabelecidos;
* Os itens de configuração sujeitos a um controle formal são colocados sob baseline;
* A situação dos itens de configuração e das baselines é registrada ao longo do tempo e disponibilizada;
* Modificações em itens de configuração são controladas;
* O armazenamento, o manuseio e a liberação de itens de configuração e baselines são controlados;
* Auditorias de configuração são realizadas objetivamente para assegurar que as baselines e os itens de configuração estejam íntegros, completos e consistentes;
* As informações de itens de configuração são comunicadas às partes interessadas;

**Processo: Garantia da Qualidade – GQA** <br />
Propósito: Assegurar que os produtos de trabalho e a execução dos processos estejam em conformidade com os planos, procedimentos e padrões estabelecidos.<br />
Resultados esperados: 

* A aderência dos produtos de trabalho aos padrões, procedimentos e requisitos aplicáveis é avaliada objetivamente, antes dos produtos serem entregues e em marcos predefinidos ao longo do ciclo de vida do trabalho;
* A aderência dos processos executados às descrições de processo, padrões e procedimentos é avaliada objetivamente;
* Os problemas e as não-conformidades são identificados, registrados e comunicados;
* Ações corretivas para as não-conformidades são estabelecidas e acompanhadas até as suas efetivas conclusões. Quando necessário, o escalonamento das ações corretivas para níveis superiores é realizado, de forma a garantir sua solução.

**Processo: Gerência de Problemas – GPL** <br />
Propósito: Minimizar a interrupção do serviço por meio da investigação de causa raiz de um ou mais incidentes que impactam nos serviços ou nos acordos de nível de serviço.<br />
Resultados esperados: 

* Problemas são identificados, registrados e classificados;
* Problemas são priorizados e analisados;
* Problemas são resolvidos e encerrados;
* Problemas que não progrediram de acordo com o nível de serviço acordado são escalados, conforme pertinente;
* O efeito de problemas não resolvidos é minimizado, conforme pertinente;
* A situação e o progresso da resolução dos problemas são comunicados às partes interessadas.

**Processo: Gerência de Portfólio de Trabalhos – GPT** <br />
Propósito: Iniciar e manter trabalhos que sejam necessários, suficientes e sustentáveis, de forma a atender os objetivos estratégicos da organização.
Este processo compromete o investimento e os recursos organizacionais adequados e estabelece a autoridade necessária para executar os trabalhos selecionados. Ele executa a qualificação contínua de trabalhos para confirmar que eles justificam a continuidade dos investimentos, ou podem ser redirecionados para justificar.<br />
Resultados esperados: 

* As oportunidades de negócio, as necessidades e os investimentos são identificados, qualificados, priorizados e selecionados em relação aos objetivos estratégicos da organização por meio de critérios objetivos;
* Os recursos e orçamentos para cada trabalho são identificados e alocados;
* A responsabilidade e autoridade pelo gerenciamento dos trabalhos são estabelecidas;
* O portfólio é monitorado em relação aos critérios que foram utilizados para a priorização;
* Ações para corrigir desvios no portfólio e para prevenir a repetição dos problemas identificados são estabelecidas, implementadas e acompanhadas até a sua conclusão;
* Os conflitos sobre recursos entre trabalhos são tratados e resolvidos, de acordo com os critérios utilizados para a priorização;
* Trabalhos que atendem aos acordos e requisitos que levaram à sua aprovação são mantidos, e os que não atendem são redirecionados ou cancelados;
* A situação do portfólio de trabalhos é comunicada para as partes interessadas, com periodicidade definida ou quando o portfólio for alterado.

**Processo: Medição – MED** <br />
Propósito: Coletar, armazenar, analisar e relatar os dados relativos aos serviços desenvolvidos e aos processos implementados na organização e em seus trabalhos, de forma a apoiar os objetivos organizacionais.<br />
Resultados esperados: 

* Objetivos de medição são estabelecidos e mantidos a partir dos objetivos de negócio da organização e das necessidades de informação de processos técnicos e gerenciais;
* Um conjunto adequado de medidas, orientado pelos objetivos de medição, é identificado e definido, priorizado, documentado, revisado e, quando pertinente, atualizado;
* Os procedimentos para a coleta e o armazenamento de medidas são especificados;
* Os procedimentos para a análise das medidas são especificados;
* Os dados requeridos são coletados e analisados;
* Os dados e os resultados das análises são armazenados;
* Os dados e os resultados das análises são comunicados aos interessados e são utilizados para apoiar decisões.


Nivel E – Parcialmente Definido
-------------------------------

**Processo: Avaliação e Melhoria do Processo Organizacional – AMP** <br />
Propósito: Determinar o quanto os processos padrão da organização contribuem para alcançar os objetivos de negócio da organização e para apoiar a organização a planejar, realizar e implantar melhorias contínuas nos processos com base no entendimento de seus pontos fortes e fracos.<br />
Resultados esperados: 

* A descrição das necessidades e os objetivos dos processos da organização são estabelecidos e mantidos;
* As informações e os dados relacionados ao uso dos processos padrão para trabalhos específicos existem e são mantidos;
* Avaliações dos processos padrão da organização são realizadas para identificar seus pontos fortes, pontos fracos e oportunidades de melhoria;
* Registros das avaliações realizadas são mantidos acessíveis;
* Os objetivos de melhoria dos processos são identificados e priorizados;
* Um plano de implementação de melhorias nos processos é definido e executado, e os efeitos desta implementação são monitorados e confirmados com base nos objetivos de melhoria;
* Ativos de processo organizacional são implantados na organização;
* Os processos padrão da organização são utilizados em trabalhos a serem iniciados e, se pertinente, em trabalhos em andamento;
* A implementação dos processos padrão da organização e o uso dos ativos de processo organizacional nos trabalhos são monitorados;
* Experiências relacionadas aos processos são incorporadas aos ativos de processo organizacional.

**Processo: Definição do Processo Organizacional – DFP** <br />
Propósito: Estabelecer e manter um conjunto de ativos de processo organizacional e padrões do ambiente de trabalho usáveis e aplicáveis às necessidades de negócio da organização.<br />
Resultados esperados: 

* Um conjunto definido de processos padrão é estabelecido e mantido, juntamente com a indicação da aplicabilidade de cada processo;
* Uma biblioteca de ativos de processo organizacional é estabelecida e mantida;
* Tarefas, atividades, papéis e produtos de trabalho associados aos processos padrão são identificados e detalhados, juntamente com o desempenho esperado do processo;
* As descrições dos modelos de ciclo de vida a serem utilizados nos trabalhos da organização são estabelecidas e mantidas;
* Uma estratégia para adaptação do processo padrão é desenvolvida considerando as necessidades dos trabalhos;
* O repositório de medidas da organização é estabelecido e mantido;
* Os ambientes padrão de trabalho da organização são estabelecidos e mantidos;
* Regras e diretrizes para a estruturação, formação e atuação de equipes são estabelecidas e mantidas.

**Processo: Gerência de Mudanças – GMU** <br />
Propósito: Assegurar que todas as mudanças que afetam os trabalhos sejam avaliadas, aprovadas, implementadas e revisadas de maneira controlada.<br />
Resultados esperados: 

* As solicitações de mudanças são registradas e classificadas;
* As solicitações de mudanças são avaliadas utilizando critérios definidos;
* As solicitações de mudanças são aprovadas antes das mudanças serem desenvolvidas ou implantadas;
* Um cronograma de mudanças e liberações é estabelecido e comunicado às partes interessadas;
* As mudanças aprovadas são desenvolvidas e testadas;
* Mudanças que não tiveram sucesso são revertidas ou remediadas.

**Processo: Gerência de Recursos Humanos – GRH** <br />
Propósito: Prover a organização e os trabalhos com os recursos humanos necessários e manter suas competências adequadas às necessidades do negócio.<br />
Resultados esperados:

* As necessidades estratégicas da organização e dos trabalhos são revistas para identificar recursos, conhecimentos e habilidades requeridos e, de acordo com a necessidade, planejar como desenvolvê-los ou contratá-los;
* Indivíduos com as habilidades e competências requeridas são identificados e recrutados;
* As necessidades de treinamento que são responsabilidade da organização são identificadas;
* Uma estratégia de treinamento é definida, com o objetivo de atender às necessidades de treinamento dos trabalhos e da organização;
* Um plano tático de treinamento é definido, com o objetivo de implementar a estratégia de treinamento;
* Os treinamentos identificados como sendo responsabilidade da organização são conduzidos e registrados;
* A efetividade do treinamento é avaliada;
* Critérios objetivos para avaliação do desempenho de grupos e indivíduos são definidos e monitorados para prover informações sobre este desempenho e melhorá-lo;
* Uma estratégia apropriada de gerência de conhecimento é planejada, estabelecida e mantida para compartilhar informações na organização;
* Uma rede de especialistas na organização é estabelecida e um mecanismo de apoio à troca de informações entre os especialistas e os trabalhos é implementado;
* O conhecimento é disponibilizado e compartilhado na organização.


Nível D – Largamente Definido
-----------------------------

**Processo: Desenvolvimento do Sistema de Serviços – DSS** <br />
Propósito: Analisar, projetar, desenvolver, integrar, verificar e validar o sistema de serviços, incluindo os componentes, para satisfazer acordos existentes ou previstos.<br />
Resultados esperados: 

* As necessidades, expectativas e restrições das partes envolvidas são coletadas e transformadas em requisitos;
* Os requisitos das partes interessadas são elaborados e refinados para o desenvolvimento do sistema de serviço;
* Os requisitos são analisados, validados e utilizados como base para a definição das funcionalidades e os atributos de qualidade do sistema de serviço;
* As soluções para o sistema de serviço são selecionadas;
* Os projetos para o sistema de serviço e seus componentes são desenvolvidos;
* A infraestrutura e os componentes para apoiar o serviço projetado são especificados;
* Uma especificação do serviço é preparada com os atributos do serviço novo ou alterado;
* As definições das interfaces internas e externas, dos projetos e das mudanças no sistema de serviços são gerenciadas;
* Os serviços novos ou modificados são desenvolvidos para satisfazer os critérios identificados na especificação do serviço;
* O projeto do sistema de serviço é implementado;
* Os componentes do sistema de serviço são reunidos e integrados ao sistema de serviço existente;
* Uma estratégia e um ambiente para verificação e validação são estabelecidos e mantidos;
* A revisão por pares é executada em componentes selecionados do sistema de serviço;
* Os componentes selecionados do sistema de serviço são verificados em relação aos requisitos especificados;
* O sistema de serviços é validado para garantir que ele é adequado para uso no ambiente pretendido e atende as expectativas das partes envolvidas;
* Os requisitos para a transição do serviço são identificados e acordados;
* Os perfis e especializações profissionais novos ou modificados são identificados, acordados, adquiridos e atribuídos;
* As atividades a serem realizadas pelo provedor de serviço ou cliente são identificadas, acordadas e realizadas;
* Alterações nos métodos, procedimentos e medições para o serviço novo ou modificado são identificadas;
* Alterações em autoridades e responsabilidades para o serviço novo ou modificado são identificadas;
* Alterações em contratos e acordos formais com grupos internos e fornecedores, para alinhamento com as mudanças em requisitos, são identificadas e implementadas;
* Alterações nos planos de disponibilidade, continuidade do serviço, capacidade e segurança da informação são identificadas e implementadas;
* Recursos para entrega de um serviço novo ou modificado são identificados e fornecidos;
* O serviço novo ou modificado é instalado e testado conforme a especificação do serviço;
* O serviço novo ou modificado é aceito conforme os critérios de aceite de serviço;
* As informações sobre os produtos de trabalho da transição do serviço novo ou modificado são comunicadas às partes interessadas.

**Processo: Orçamento e Contabilização de Serviços – OCS** <br />
Propósito: Controlar o orçamento e a contabilização dos serviços fornecidos.<br />
Resultados esperados: 

* Custos do fornecimento do serviço são estimados;
* Orçamentos são produzidos utilizando estimativas de custos;
* Desvios do orçamento e custos são controlados;
* Desvios do orçamento são resolvidos;
* Desvios do orçamento e custos são comunicados às partes interessadas.

Nível C – Definido
------------------

**Processo: Gerência de Capacidade – GCA** <br />
Propósito: Assegurar que o provedor de serviços tenha capacidade para atender os requisitos atuais e futuros acordados.<br />
Resultados esperados: 

* A capacidade (atual e futura) e os requisitos de desempenho são identificados e acordados;
* Um plano de capacidade é desenvolvido baseado na capacidade e requisitos de desempenho;
* A capacidade é fornecida para atender aos requisitos atuais de capacidade e desempenho;
* A utilização da capacidade é monitorada, analisada e o desempenho é ajustado;
* A capacidade é preparada para atender a capacidade futura e o desempenho necessário;
* Alterações de capacidade e desempenho são refletidas no plano de capacidade;
* Medidas e técnicas analíticas são selecionadas para serem utilizadas na gestão da capacidade.

**Processo: Gerência da Continuidade e Disponibilidade dos Serviços – GCD** <br />
Propósito: Assegurar que acordos de níveis de serviços sejam cumpridos em circunstâncias previsíveis.<br />
Resultados esperados: 

* Os requisitos de continuidade e disponibilidade são identificados;
* Um plano de continuidade é desenvolvido utilizando os requisitos de continuidade de serviço;
* Um plano de disponibilidade é desenvolvido utilizando os requisitos de disponibilidade de serviço;
* A continuidade do serviço é testada em relação aos requisitos de continuidade para validar o plano, conforme pertinente;
* A disponibilidade do serviço é testada em relação aos requisitos de disponibilidade para validar o plano, conforme pertinente;
* A disponibilidade do serviço é monitorada;
* Causas raiz de indisponibilidade não planejada de serviço são identificadas e analisadas;
* Ações corretivas são executadas para tratar as causas raiz identificadas;
* Alterações nos requisitos de continuidade do serviço são refletidas no plano de continuidade do serviço;
* Alterações nos requisitos de disponibilidade do serviço são refletidas no plano de disponibilidade do serviço;
* Medidas e técnicas analíticas são selecionadas para serem utilizadas na gestão da disponibilidade.

**Processo: Gerência de Decisões – GDE** <br />
Propósito: Analisar possíveis decisões críticas usando um processo formal, com critérios estabelecidos, para avaliação das alternativas identificadas.<br />
Resultados esperados: 

* Guias organizacionais para a gerência de decisões são estabelecidos e mantidos;
* O problema ou questão a ser objeto de um processo formal de tomada de decisão é definido;
* Critérios para avaliação das alternativas de solução são estabelecidos e mantidos em ordem de importância, de forma que os critérios mais importantes exerçam mais influência na avaliação;
* Alternativas de solução aceitáveis para o problema ou questão são identificadas;
* Os métodos de avaliação das alternativas de solução são selecionados de acordo com sua viabilidade de aplicação;
* Soluções alternativas são avaliadas usando os critérios e métodos estabelecidos;
* Decisões são tomadas com base na avaliação das alternativas utilizando os critérios de avaliação estabelecidos.

**Processo: Gerência de Liberação – GLI** <br />
Propósito: Implantar liberações de serviços e componentes de serviços em um ambiente de produção de uma forma controlada.<br />
Resultados esperados:

* Requisitos para liberações de serviços e componentes são estabelecidos e acordados com as partes interessadas;
* Liberações de serviços e componentes de serviços são planejadas;
* As liberações de serviços e componentes são testadas antes da implantação;
* As liberações de serviços e componentes aprovadas são implantadas;
* A integridade de hardware, software e outros componentes do serviço é garantida durante a implantação da liberação;
* Liberações de serviços e componentes que não tiveram sucesso na implantação são revertidas ou remediadas, conforme pertinente;
* Informações da liberação são comunicadas às partes interessadas.

**Processo: Gerência de Riscos – GRI** <br />
Propósito: Identificar, analisar, tratar, monitorar e reduzir continuamente os riscos em nível organizacional e de trabalho. <br />
Resultados esperados: 

* O escopo da gerência de riscos é determinado;
* As origens e as categorias de riscos são determinadas e os parâmetros usados para analisar riscos, categorizá-los e controlar o esforço da gerência de riscos são definidos;
* As estratégias apropriadas para a gerência de riscos são definidas e implementadas;
* Os riscos do trabalho são identificados e documentados, incluindo seu contexto, condições e possíveis consequências para o trabalho e as partes interessadas;
* Os riscos são priorizados, estimados e classificados de acordo com as categorias e os parâmetros definidos;
* Planos para a mitigação de riscos são desenvolvidos;
* Os riscos são analisados e a prioridade de aplicação dos recursos para o monitoramento desses riscos é determinada;
* Os riscos são avaliados e monitorados para determinar mudanças em sua situação e no progresso das atividades para seu tratamento;
* Ações apropriadas são executadas para corrigir ou evitar o impacto do risco, baseadas na sua prioridade, probabilidade, consequência ou outros parâmetros definidos.


**Processo: Gerência da Segurança da Informação – GSI** <br />
Propósito: Gerenciar a segurança da informação em um acordo de nível de segurança dentro de todas as atividades do gerenciamento do serviço.
Resultados esperados: 

* Os requisitos de segurança da informação são identificados e acordados;
* Critérios para avaliação dos riscos de segurança da informação e níveis aceitáveis desses riscos são identificados;
* Riscos de segurança da informação são identificados;
* Riscos de segurança da informação são avaliados;
* Medições e controles de riscos de segurança da informação são definidos;
* Medições e controles de riscos de segurança da informação são implementados;
* Incidentes de segurança são qualificados e registrados;
* Aspectos da segurança da informação são comunicados às partes interessadas;
* O impacto das mudanças na segurança da informação é analisado e relatado.

**Processo: Relatos de Serviços – RLS** <br />
Propósito: Produzir relatórios pontuais e precisos para apoiar uma efetiva comunicação e tomada de decisão.<br />
Resultados esperados: 

* As necessidades de relatórios de serviços são identificadas visando suprir informações para as partes interessadas;
* O conteúdo do relatório de serviço é definido em termos das necessidades e requisitos de relatos de serviços;
* Relatórios de serviços são produzidos de acordo com os requisitos de relatos de serviços;
* Os relatórios de serviços são comunicados às partes interessadas.


Nível B – Gerenciado Quantitativamente
--------------------------------------

Este nível não possui processos específicos.


Nível A – Em Otimização
-----------------------

Este nível não possui processos específicos.

Conclusão
=========

Um dos grandes diferencias presentes na proposta do MPS.BR é o fato de seus custos serem acessíveis às empresas nacionais, principalmente as de pequeno e médio portes, contribuindo para a promoção da melhoria de processos de software de acordo com os padrões de qualidade aceitos internacionalmente.<br/>
O aumento da competitividade no mercado de software e serviços de TI fez que com que as empresas motivassem para a necessidade de obter maior qualidade dos produtos e serviços oferecidos, bem como a satisfação dos clientes com os resultados entregues. E essa qualidade pode ser obitda por meio da implementação de processos seguindo as sugestões dos guias de implementação do
MPS.BR.<br/>
Uma das principais dificuldades frequentemente encontradas na implementação do programa de melhoria, está relacionado à cultura da empresa e de seus colaboradores, pois a implementação de mudanças acaba gerando certo desconforto. Para superar esta dificuldade, é necessário que a empresa convença seus colaboradores da sua importância dentro do processo e apresente os benefícios e melhorias das condições de trabalho.<br/>
A avaliação de maturidade do modelo MPS deve ser realizada por uma equipe composta por membros internos  (representantes da unidade organizacional) e membros externos (avaliador líder, avaliadores adjuntos da Instituição Avaliadora e, opcionalmente, avaliadores em formação indicados pela SOFTEX). A duração da avaliação e a quantidade  (mínima e máxima) de avaliadores são proporcionais à capacidade exigida para cada nível de maturidade. Uma avaliação pode durar de um a cinco dias, e contar com uma equipe de três a nove avaliadores.<br/>
A avaliação tem validade por dois anos. Ao final desses dois anos, a empresa deverá passar por nova avaliação para manter a maturidade adaquirida já avaliada ou evoluir o nível de maturidade.

Referências
===========
[^1]: (texto aparece na nota de rodapé, mas sem efeito final) [@pandocDocConv2014]
[^2]: [@QuickMarkdownExample2013]

---
references:
- id: Governança_de_TI
  title: "Implantando a Governança de TI: da Estratégia à Gestão de Processos e Serviços"
  volume: "4ª Edição"
  publisher: BRASPORT
  history: BRASPORT
  locators: Rio de Janeiro
  extra: Rio de Janeiro
  type: book
  year: 2014
  issue: 4

- id: WikipediaMPSBR
  title: "Melhoria de Processos do Software Brasileiro"
  translator: S.l.
  booktitle: "Wikipedia: A Enciclopédia Livre"
  container-title: Modelo de Maturidade
  URL: 'http://http://pt.wikipedia.org/wiki/Melhoria_de_Processos_do_Software_Brasileiro'
  accessed:
    day: 22
    month: 8
    year: 2014
  publisher: Wikimedia
  type: entry-encyclopedia
  year: 2014

- id: WikipediaCMMI
  title: "Modelo Integrado de Maturidade e de Capacidade"
  translator: S.l.
  container-title: Modelo de Maturidade
  URL: 'http://pt.wikipedia.org/wiki/CMMI'
  accessed:
    day: 24
    month: 8
    year: 2014
  publisher: Wikipedia
  type: webpage
  issued:
    year: 2014
    month: 3
...
