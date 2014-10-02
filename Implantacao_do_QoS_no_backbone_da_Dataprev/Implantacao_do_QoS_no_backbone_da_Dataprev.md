---
remark: implantação do QoS no *backbone* da Dataprev
date: 26 de setembro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Implantação do QoS no *backbone* da Dataprev
abstract: Este artigo descreve de forma macro o funcionamento do QoS *(Quality of Service)* e como está configurado no *backbone* da Dataprev.
author:
- affiliation: DSIG
  name: José Augusto Pereira de Souza Tovar
responsibility:
- affiliation: DSIG
  name: Rodrigo Morgado da Silva
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Suporte de TIC - DEST'
tags:
- QoS
- *'Quality of Service'*
- *'Network'*
- Rede
- Latência
- Jitter
- Confiabilidade
- Largura de Banda
- *'backbone'*
...

# Introdução

Tradicionalmente, as redes IP oferecem um serviço de entrega sem distinção sobre o tráfego. Todo o tráfego é tratado da mesma forma. Porém alguns serviços são mais dependentes de alguns requisitos de rede para o seu funcionamento adequado. A aplicação de técnicas de melhoria de QoS visa tratar esse problema.

#Desafios

Os principais desafios da implementação do QoS *(Quality of Service)* no *backbone* da Dataprev foram identificar quais aplicações deveriam ser tratadas e qual tratamento deveria ser dado para essas aplicações.

#Benefícios e/ou recomendações


Alguns dos benefícios da implantação de políticas de QoS são : 

- Permite um maior controle sobre os recursos da rede e o gerenciamento da mesma sob a perspectiva do negócio.
- Garante que aplicações críticas e urgentes tenham todos os recursos necessários para o seu melhor funcionamento em detrimento a aplicações menos importantes.
- Reduz custos usando os recursos da rede eficientemente, postergando ou reduzindo a necessidade de expansões e upgrades.


#Breve explicação sobre o QoS


O objetivo do QoS é prover um melhor e mais previsível serviço de rede controlando largura de banda, confiabilidade, jitter e latência. 

- A confiabilidade é uma característica importante ao fluxo de dados, a falta dela significa que pacotes de dados estão sendo perdidos. 

- A latência é o tempo que o pacote leva da origem ao destino. Diferentes aplicações toleram diferentes latências. Telefonia por IP,  videoconferências e login remoto são aplicações que requerem latência mínima enquanto e-mail e transferências de arquivos toleram uma maior latência

- Jitter é a variação da latência.  Aplicações de áudio e vídeo em tempo real não toleram altos valores de jitter.

- A largura de banda, como o próprio nome já diz, é quanto uma aplicação tem disponível para utilizar. Aplicações de vídeo necessitam de uma largura de banda maior para funcionar enquanto um e-mail necessita de pouca banda para funcionar.

Abaixo uma tabela com algumas aplicações e os requisitos de QoS necessários
    
![Tabela QoS](imagens/Tabela_QoS.PNG) 

Assim QoS é um conjunto de políticas que busca garantir os requisitos de rede para que as aplicações apropriadamente.

#Técnicas para melhoria de QoS


##Política de Filas

###FIFO *(First-in First-out)*
Armazena os pacotes em uma fila única de acordo com a ordem de chegada na fila, até que o envio de dados seja disponibilizado nas interfaces de Roteadores e switches. É de simples e fácil configuração, porém dependendo da característica do fluxo de dados pode causar jitter e aumento da latência.


###Fair-queue
Esse algoritmo busca oferecer uma alocação mais equitativa de banda entre os fluxos de dados, proporcionando uma ordenação dos fluxos em sessões e alocando uma fração da banda para cada sessão.

###Weighted Fair Queue *(WFQ)* 
Os pacotes são automaticamente alocados a uma classe *(voz, e-mail, etc.)*, e em seguida, após serem classificados de acordo com sua precedência, recursos, e indicadores, os mesmos são enviado à rede de destino. Este algoritmo proporciona uma justa distribuição de banda na rede, melhorando o seu desempenho e tem a capacidade de fazer com que fluxos que estejam enfrentando congestionamento, por exemplo, possam ser atendidos com uma menor frequência em relação aos outros.

###CBWFQ e LLQ
Class-based weighed fair queuing é uma política baseada na WFQ que permite ao usuário classificar os pacotes do fluxo de dado utilizando protocolos, ACLs *(Access control lists)* ou interfaces dos equipamentos de rede. Cada pacote que satisfaça um critério de classificação é colocado numa fila referente aquela classe. A fila LLQ *(Low Latency Queue)* é uma fila de prioridade com baixa latência, como o próprio nome já diz. Essa fila é usada para os fluxos de dados que são sensíveis a alta latência.

##Mecanismos de Descarte

###RED *(Random Early Detection)* 
É um mecanismo de gerenciamento de fila que detecta o congestionamento antes do *overflow* da fila de forma a evitar o descarte excessivo de pacotes e mantendo o *throughput* da rede enquanto minimiza a latência das filas.

###WRED *(Weighted Random Early Detection)* 
O WRED *(Weighted Random Early Detection)* utiliza os conceitos do RED porém permite que diferentes perfis de REDs sejam usados numa mesma fila. O tráfego que deve preferencialmente ser descartado pode ser marcado de forma diferente do restante do tráfego da fila. 

##Classificação dos Pacotes
Para classificar e assim possibilitar o tratamento dos pacotes de um fluxo de dados foi definido um campo no cabeçalho IPv4 para Classificação de QoS. 

###IP Precedence
Inicialmente foi definido um campo de 8 bits no cabeçalho IP chamado ToS *(Type of Service)* para classificação do pacote de dados. O IP Precedence utiliza os 3 primeiros bits desse campo para marcar o pacote e permitir a sua classificação e priorização.

###DSCP *(Differentiated Services Code Point)*
Na RFC 2474 o campo ToS foi renomeado para DS *(Differentiated Services)* e os 6 primeiros dígitos desse campo são chamados de DSCP e também são utilizados para classificação e priorização.


# QoS no *backbone* da Dataprev
Na configuração do QoS no *backbone* da Dataprev diversas técnicas foram utilizadas e nos próximos tópicos teremos a explanação sobre o funcionamento.

## Detalhamento da solução de QoS
Para configurar a solução os roteadores de *backbone* foram segmentados em : interfaces de LAN e interfaces de WAN. As interfaces de LAN são as interfaces que ligam os roteadores aos Datacenters, estações de usuários e a Rede de Acesso *(Ex.: Agências do INSS e Unidades da Dataprev)* e as interfaces de WAN são as que interligam os Centros de Processamento da Dataprev.

A figura abaixo mostra o ambiente da Dataprev : 

![diagrama](imagens/diagrama.PNG)

Neste contexto, as interfaces LAN são responsáveis pela classificação e marcação de tráfego
(ou confiar na marcação, em alguns casos). As interfaces de WAN são ligadas a circuitos contratados de operadoras e, por estarem mais susceptíveis a congestionamento devido à largura de banda contratada e à demanda de tráfego, deverão realizar políticas diferenciadas de filas *(LLQ/CBWFQ)* para classes específicas que necessitam de latência mínima, banda garantida e/ou banda máxima.

Com a ativação do mls qos de forma global, as interfaces de LAN passam a desmarcar o byte
ToS, diferentemente das interfaces de WAN que confiam na marcação por padrão. Para que as
interfaces de LAN passem a confiar nas marcações de DSCP, por exemplo, será necessário inserir o comando *mls qos trust dscp* na configuração da interface LAN.

###Datacenter
O tráfego entrante no roteador vindo do Datacenter deverá ser classificado e marcado. Como os
projetos anteriores adotaram uma solução com IPP *(ip-precedence)*, a configuração será realizada com DSCP mantendo compatibilidade com o IPP ao utilizar apenas a marcação dos 3 primeiros bits do campo ToS do cabeçalho IP. A policy-map Traffic-IN aplicada na entrada da interface G5/2 é
responsável pela classificação e marcação de tráfego vindo o Datacenter.  

A proposta inicial de classificação/marcação do tráfego vindo do Datacenter/CPRJ foi:

- DSCP cs5 *(equivalente a IPP 5 - Classe Tempo Real)* – Rede de voz/video e SNMP do servidores degerência;
- DSCP cs4 *(equivalente a IPP 4 - Classe Corporativa Prioritária)* – Telnet, LDAP, TACACS CNIS, Prisma, SABI e SAA;
- DSCP cs3 *(equivalente a IPP 3)* – Portal CNIS, SIPPS, HIPNet, w3b2 *(SALWEB e GFIPWEB)*, www1, www2, www3 e www5;  
- Marcação confiável de DSCPs cs5, cs4 e cs3 – Servidores de gerência e monitoração;  
- DSCP 0 *(equivalente a IPP 0)* – Todo tráfego restante.

###Rede de estações do CPRJ

O tráfego entrante no CV03 vindo da rede de estações do CPRJ deverá ser classificado e
marcado. A mesma policy-map Traffic-IN aplicada na entrada da interface G6/1 é responsável pela
classificação e marcação de tráfego vindo da rede de estações.


- DSCP cs4 – Telnet;
- Marcação confiável de DSCPs cs5, cs4 e cs3;
- Estações de gerência do DERE *(10.0.130.0/27 e 10.0.131.0/27);
- DSCP 0 – Todo tráfego restante.

####Configurações nas interfaces de LAN provenientes ao Datacenter

**Essa policy-map marca os pacotes que chegam ao roteador com as marcações respectivas a cada classe**

policy-map Traffic-IN  
&nbsp;&nbsp;class tempo-real-IN  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs5  
&nbsp;&nbsp;class corp-prioritaria-IN  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs4  
&nbsp;&nbsp;class corporativa-IN  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs3  
&nbsp;&nbsp;class trusted-hosts-5  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs5  
&nbsp;&nbsp;class trusted-hosts-4  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs4  
&nbsp;&nbsp;class trusted-hosts-3  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs3  
&nbsp;&nbsp;class transferencias-IN  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp cs2  
&nbsp;&nbsp;class class-default  
&nbsp;&nbsp;&nbsp;&nbsp;set dscp default  

**Essas class-maps são utilizadas para inspecionar os pacotes para aplicação de políticas de QoS**  
class-map match-any trusted-hosts-4  
&nbsp;&nbsp;match access-group name trusted-hosts-4  
class-map match-any transferencias-IN  
&nbsp;&nbsp;match access-group name transferencias  
class-map match-any trusted-hosts-5  
&nbsp;&nbsp;match access-group name trusted-hosts-5  
class-map match-any trusted-hosts-3  
&nbsp;&nbsp;  match access-group name trusted-hosts-3  
class-map match-any corporativa-IN  
&nbsp;&nbsp;  match access-group name corporativa  
class-map match-any corp-prioritaria-IN  
&nbsp;&nbsp;  match access-group name corp-prioritaria  
class-map match-any tempo-real-IN  
&nbsp;&nbsp;  match access-group name tempo-real  

**Essas ACLs *(Access Control List)* definem quais endereços de rede serão marcados em cada classe.**
ip access-list extended corp-prioritaria  
&nbsp;&nbsp;permit tcp any any eq telnet  
 &nbsp;&nbsp;permit tcp any eq telnet any  
 &nbsp;&nbsp;permit tcp host *(ip do CNIS)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark Prisma  
 &nbsp;&nbsp;permit tcp any *(ip do Prisma)* eq *(porta do serviço)*  
 &nbsp;&nbsp;remark SABI  
 &nbsp;&nbsp;permit tcp any *(ip do SABI)* eq *(porta do serviço)*  
 &nbsp;&nbsp;remark SAA  
 &nbsp;&nbsp;permit tcp host *(ip do SAA)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark Trafego SNMP dos servidores de gerencia    
 &nbsp;&nbsp;permit udp *(ip do servidor)* any eq snmp  
 &nbsp;&nbsp;remark Tacacs  
 &nbsp;&nbsp;permit tcp any eq tacacs any  
 &nbsp;&nbsp;permit tcp any any eq tacacs  
 &nbsp;&nbsp;remark LDAP  
 &nbsp;&nbsp;permit tcp any eq 636 any  
 &nbsp;&nbsp;permit tcp any eq 389 any  
 &nbsp;&nbsp;permit tcp any any eq 636  
 &nbsp;&nbsp;permit tcp any any eq 389  
ip access-list extended corporativa  
 &nbsp;&nbsp;remark SIPPS  
 &nbsp;&nbsp;permit tcp host *(ip do SIPPS)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark HIPNet  
 &nbsp;&nbsp;permit tcp host *(ip do HIPNET )* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark w3b2 - SALWEB e GFIPWEB  
 &nbsp;&nbsp;permit tcp host *(ip do SALWEB e GFIPWEB )* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www1  
 &nbsp;&nbsp;permit tcp host *(ip do www1)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www2  
 &nbsp;&nbsp;permit tcp host *(ip do www2)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www3  
 &nbsp;&nbsp;permit tcp host *(ip do www3)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www5  
 &nbsp;&nbsp;permit tcp host *(ip do www5)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark w3b2 - SALWEB e GFIPWEB  
 &nbsp;&nbsp;permit tcp host *(ip do SALWEB e GFIPWEB)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark Treinamento Portal CNIS  
 &nbsp;&nbsp;permit tcp host *(ip do Treinamento Portal CNIS)* any  
 &nbsp;&nbsp;remark Portal CNIS  
 &nbsp;&nbsp;permit tcp host *(ip do Portal CNIS)* eq *(porta do serviço)* any  
ip access-list extended transferencias  
 &nbsp;&nbsp;remark p312p000.mte  
 &nbsp;&nbsp;permit ip any host *(ip do servidor)*   
ip access-list extended tempo-real  
 &nbsp;&nbsp;remark Rede de voz e video  
 &nbsp;&nbsp;permit ip *(rede de voz e vídeo do CV)* any  
 &nbsp;&nbsp;remark Rede de voz e video da Alvaro Rodrigues  
 &nbsp;&nbsp;permit ip *(rede de voz e vídeo da AR)* any     
ip access-list extended trusted-hosts-3  
 &nbsp;&nbsp;remark Servidores de gerencia  
 &nbsp;&nbsp;permit ip *(ip do servidor)* any precedence flash  
 &nbsp;&nbsp;remark Estacoes de gerencia DERE  
 &nbsp;&nbsp;permit ip *(ip do servidor)* any precedence flash  
ip access-list extended trusted-hosts-4  
 &nbsp;&nbsp;remark Servidores de gerencia  
 &nbsp;&nbsp;permit ip *(ip do servidor)* any precedence flash-override  
 &nbsp;&nbsp;remark Estacoes de gerencia DERE  
 &nbsp;&nbsp;permit ip *(ip do servidor)* any precedence flash-override  
ip access-list extended trusted-hosts-5  
 &nbsp;&nbsp;remark Servidores de gerencia  
 &nbsp;&nbsp;permit ip *(ip do servidor)* any precedence critical  
 &nbsp;&nbsp;remark Estacoes de gerencia DERE  
 &nbsp;&nbsp;permit ip *(ip do servidor)* any precedence critical  

###Rede de Acesso
O tráfego entrante no roteador proveniente rede de acesso tem a marcação confiável
como é feito nativamente por uma interface de WAN. Como ainda não existe a necessidade de realizar políticas diferenciadas de filas *(LLQ/CBWFQ)* por se tratar de uma ligação local de 1Gbps então utilizou-se uma interface LAN. 

###Interfaces de WAN
Conforme mencionado anteriormente, as interfaces de WAN deverão realizar políticas
diferenciadas de filas *(LLQ/CBWFQ)* para o tráfego de saída. Além disso, a política de filas deverá ser aplicada e limitada ao valor contratado pela operadora. Caso contrário, o tráfego escoará pela interface WAN na taxa da própria interface *(1Gbps)* e o descarte/shaping ocorrerá na operadora, tornando as configurações de QoS ineficientes.  

Para isso optou-se em implementar regras de QoS-hierárquico onde a policy de 1º nível será
responsável por limitar o escoamento de tráfego à taxa contratada e a policy de 2º nível será aplicada sobre esta última com as regras da LLQ/CBWFQ.  

A CBWFQ *(Class-Based Weighted Fair Queueing)* será responsável por garantir uma banda
mínima para cada classe. Com a adição de uma fila PQ *(strict Priority Queueing)* à CBWFQ teremos uma fila LLQ *(Low Latency Queueing)*, onde a classe mapeada para a PQ terá latência mínima e banda garantida, e as demais classes terão banda garantida, cada uma com um valor pré-definido.
Em uma situação de congestionamento, a fila PQ descarta o tráfego excedente ao valor pré-determinado, diferentemente das demais classes da CBWFQ que são capazes de dividir a banda das
classes ociosas proporcionalmente ao valor definido para cada classe. Naturalmente, em uma situação de não-congestionamento, nenhum tráfego será descartado.  

Os percentuais definidos para cada classe são estimativas e poderão ser alterados conforme
necessidade.  

A classe control mapeia os pacotes de protocolos de roteamento *(OSPF, BGP, etc.)* que por
padrão recebem marcação cs6 *(ou IPP 6)* e também terá uma banda garantida.

As classes corporativa, shape-SP e class-default terão implemantação de WRED *(Weighted
Random Early Detection)*, que descarta pacotes aleatóriamente a uma determinada ocupação das filas de cada classe minimizando os efeitos de congestionamentos.

####Configurações nas interfaces de WAN

**Esta policy-map limita o tráfego na interface ao valor contratado**  
policy-map intelig-sp  
&nbsp;&nbsp; class class-default    
&nbsp;&nbsp;&nbsp;&nbsp;   shape average 300000000  
&nbsp;&nbsp;&nbsp;service-policy llq-sp

**Esta policy-map define a banda de cada classe e configura latência minima para a LLQ**  
policy-map llq-sp  
&nbsp;&nbsp;  class tempo-real  
&nbsp;&nbsp;    &nbsp;&nbsp;priority percent 10  
  &nbsp;&nbsp;class corp-prioritaria  
  &nbsp;&nbsp;&nbsp;&nbsp;  bandwidth percent 25  
  &nbsp;&nbsp;class corporativa  
  &nbsp;&nbsp;&nbsp;&nbsp;  bandwidth percent 20  
  &nbsp;&nbsp;&nbsp;&nbsp;random-detect  
  &nbsp;&nbsp;&nbsp;&nbsp;random-detect precedence 3 1000 4000 10  
   &nbsp;&nbsp;class control  
    &nbsp;&nbsp; &nbsp;&nbsp; bandwidth percent 1  
  &nbsp;&nbsp; class transferencias  
   &nbsp;&nbsp; &nbsp;&nbsp;  bandwidth percent 9  
     &nbsp;&nbsp; &nbsp;&nbsp;queue-limit 1000 packets  
     &nbsp;&nbsp; &nbsp;&nbsp;random-detect  
     &nbsp;&nbsp; &nbsp;&nbsp;random-detect precedence 2 250 1000 10  
   &nbsp;&nbsp;class class-default  
     &nbsp;&nbsp; &nbsp;&nbsp;random-detect  
     &nbsp;&nbsp; &nbsp;&nbsp;random-detect precedence 0 1000 4000 10  
     &nbsp;&nbsp; &nbsp;&nbsp;bandwidth percent 35  


**Essas class-maps são utilizadas para inspecionar os pacotes para aplicação de políticas de QoS**  
&nbsp;&nbsp; class-map match-any transferencias  
  &nbsp;&nbsp; &nbsp;&nbsp; match ip precedence 2     
&nbsp;&nbsp; class-map match-any corporativa-IN  
  &nbsp;&nbsp; &nbsp;&nbsp; match access-group name corporativa  
&nbsp;&nbsp; class-map match-any corp-prioritaria  
  &nbsp;&nbsp; &nbsp;&nbsp; match ip precedence 4     
&nbsp;&nbsp; class-map match-any tempo-real  
&nbsp;&nbsp; &nbsp;&nbsp;   match ip precedence 5   
&nbsp;&nbsp; class-map match-any control  
  &nbsp;&nbsp; &nbsp;&nbsp; match ip precedence 6    
&nbsp;&nbsp; class-map match-any corporativa  
  &nbsp;&nbsp; &nbsp;&nbsp; match ip precedence 3   
   

**Essas ACLs *(Access Control List)* definem quais endereços de rede serão marcados em cada classe.**  
ip access-list extended corp-prioritaria  
&nbsp;&nbsp;permit tcp any any eq telnet  
 &nbsp;&nbsp;permit tcp any eq telnet any  
 &nbsp;&nbsp;permit tcp host *(ip do CNIS)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark Prisma  
 &nbsp;&nbsp;permit tcp any *(ip do Prisma)* eq *(porta do serviço)*  
 &nbsp;&nbsp;remark SABI  
 &nbsp;&nbsp;permit tcp any *(ip do SABI)* eq *(porta do serviço)*  
 &nbsp;&nbsp;remark SAA  
 &nbsp;&nbsp;permit tcp host *(ip do SAA)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark Trafego SNMP dos servidores de gerencia    
 &nbsp;&nbsp;permit udp *(ip do servidor)* any eq snmp  
 &nbsp;&nbsp;remark Tacacs  
 &nbsp;&nbsp;permit tcp any eq tacacs any  
 &nbsp;&nbsp;permit tcp any any eq tacacs  
 &nbsp;&nbsp;remark LDAP  
 &nbsp;&nbsp;permit tcp any eq 636 any  
 &nbsp;&nbsp;permit tcp any eq 389 any  
 &nbsp;&nbsp;permit tcp any any eq 636  
 &nbsp;&nbsp;permit tcp any any eq 389  
ip access-list extended corporativa  
 &nbsp;&nbsp;remark SIPPS  
 &nbsp;&nbsp;permit tcp host *(ip do SIPPS)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark HIPNet  
 &nbsp;&nbsp;permit tcp host *(ip do HIPNET )* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark w3b2 - SALWEB e GFIPWEB  
 &nbsp;&nbsp;permit tcp host *(ip do SALWEB e GFIPWEB )* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www1  
 &nbsp;&nbsp;permit tcp host *(ip do www1)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www2  
 &nbsp;&nbsp;permit tcp host *(ip do www2)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www3  
 &nbsp;&nbsp;permit tcp host *(ip do www3)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark www5  
 &nbsp;&nbsp;permit tcp host *(ip do www5)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark w3b2 - SALWEB e GFIPWEB  
 &nbsp;&nbsp;permit tcp host *(ip do SALWEB e GFIPWEB)* eq *(porta do serviço)* any  
 &nbsp;&nbsp;remark Treinamento Portal CNIS  
 &nbsp;&nbsp;permit tcp host *(ip do Treinamento Portal CNIS)* any  
 &nbsp;&nbsp;remark Portal CNIS  
 &nbsp;&nbsp;permit tcp host *(ip do Portal CNIS)* eq *(porta do serviço)* any  
ip access-list extended tempo-real  
 &nbsp;&nbsp;remark Rede de voz e video  
 &nbsp;&nbsp;permit ip *(rede de voz e vídeo do CV)* any  
 &nbsp;&nbsp;remark Rede de voz e video da Alvaro Rodrigues  
 &nbsp;&nbsp;permit ip *(rede de voz e vídeo da AR)* any   
ip access-list extended transferencias  
 &nbsp;&nbsp;remark p312p000.mte  
 &nbsp;&nbsp;permit ip any host *(ip do servidor)*  


Conclusão
=========

Nos dias de hoje com a crescente demanda de serviços oferecidos nas redes IP, cresce também a necessidade de garantia dos requisitos necessários para cada tipo de aplicação. Nesse aspecto o QoS torna-se um fator importante para o suporte a estas aplicações

O QoS auxilia os administradores de redes a manterem os níveis de serviço solicitados pelos usuários, além de representar uma economia quanto aos aspectos de operação e manutenção da própria rede. Entretanto, a diversidade das aplicações envolvidas torna difícil estabelecer um padrão de QoS.

É necessário um profundo conhecimento da rede IP para que o projeto de QoS seja bem elaborado e implantado. Esse processo é contínuo. A cada dia novas aplicações são construídas e novos requisitos são solicitados e a rede tem que adaptar-se a essas mudanças.

Referências
===========
---
KUROSE, J. F., Ross, K. W.; Redes de Computadores e a Internet - Uma abordagem top-down. Pearson Addison Wesley. 3ª Ed., 2006.

COMER, D. Interligação em rede com TCP/IP: Vol. 1, princípios, protocolos e arquitetura. Campus,3ª Ed. 2006

FOROUZAN, Behrouz A., Comunicação de dados e Redes de computadores, Ed. Mc Graw Hill, 4ª edição, 2008.
 
EVANS, John. Deploying IP and MPLS QOS for multiservice networks :theory and practice.Elsevier, c2007.


