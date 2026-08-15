---
id: 07_redes-computadores-web-teoria
title: "Módulo 07 — Redes de Computadores e Web"
sidebar_position: 70
---

# Módulo 07 — Redes de Computadores e Web

> **Objetivo:** entender como dados trafegam entre computadores em rede, da camada física até o
> protocolo que faz a Web funcionar (HTTP).
> **Pré-requisitos:** Módulo 06 (Sistemas Operacionais).
> **Tempo de referência:** 6 a 8 horas.
> **Prática correspondente:** [07_redes-computadores-web-pratica.md](07_redes-computadores-web-pratica.md)

---

## 1. Por que isso importa

No módulo 06 você viu que o sistema operacional intermedia o acesso a dispositivos como disco e
tela através de drivers e interrupções — a aplicação nunca fala direto com o hardware. O acesso à
rede segue exatamente essa lógica: o SO oferece uma abstração chamada **socket**, que uma
aplicação usa para mandar e receber dados pela rede, sem precisar saber nada sobre cabos,
sinalização elétrica ou roteamento. Este módulo entende o que acontece depois que esse socket
manda dados para fora da sua máquina, até chegar a outro computador do outro lado do mundo — do
cabo físico até o HTTP que faz a Web funcionar.

## 2. O que é uma rede

Uma rede de computadores é, na essência, um conjunto de dispositivos capazes de trocar dados entre
si através de algum meio físico (cabo, wifi, fibra) seguindo regras combinadas (protocolos). Sem
essas regras combinadas, dois dispositivos poderiam estar fisicamente conectados e ainda assim não
conseguir "se entender" — é como duas pessoas com um cabo de telefone entre elas, mas falando
idiomas diferentes.

## 3. LAN, WAN e Internet

**LAN** (Local Area Network) é uma rede pequena, geograficamente concentrada — sua casa, sua
escola, o escritório onde você trabalha. **WAN** (Wide Area Network) conecta LANs distantes entre
si, atravessando cidades, países ou continentes. A **Internet** é a WAN mais famosa que existe: a
rede de redes, conectando bilhões de LANs ao redor do mundo através de um conjunto comum de
protocolos.

`[TENTE VOCÊ]` O wifi da sua casa conectando seu notebook, celular e smart TV é uma LAN ou uma
WAN? Resposta: LAN — é uma rede pequena e local. Ela só vira parte da WAN/Internet quando seu
roteador se conecta ao provedor de internet, que a liga ao resto do mundo.

## 4. Cliente e servidor

Toda vez que você abre um site, seu computador assume o papel de **cliente**: ele inicia a
conversa, pedindo algo. Do outro lado, um **servidor** espera por esses pedidos e responde. Esse
padrão cliente-servidor se repete em quase tudo que você vai ver neste módulo — não é exclusivo da
Web, é como a maior parte da comunicação em rede é organizada.

## 5. Arquitetura em camadas

Pense em enviar uma encomenda pelos Correios. Você escreve uma carta (o conteúdo), coloca dentro
de um envelope endereçado, a agência local despacha para um centro de distribuição, que roteia
para outro centro, até chegar ao endereço final — onde cada camada de embalagem é removida na
ordem inversa em que foi colocada. Redes de computadores funcionam de forma parecida: cada camada
empacota o que a camada de cima entrega, adiciona sua própria informação de controle (como um
envelope dentro de outro envelope), e entrega para a camada de baixo — do lado de quem recebe,
cada camada desempacota sua parte, na ordem inversa.

### 6. Modelo OSI

O modelo OSI (Open Systems Interconnection) é a referência acadêmica mais completa, com **7
camadas**: Física, Enlace, Rede, Transporte, Sessão, Apresentação e Aplicação. Ele existe pra
padronizar a *conversa* sobre redes — cada camada tem uma responsabilidade bem delimitada, e
"problema de camada 3" (rede/roteamento) é diferente de "problema de camada 7" (aplicação).

### 7. Modelo TCP/IP

Na prática, a Internet não implementa as 7 camadas do OSI separadamente — ela usa uma versão mais
enxuta, de **4 camadas**, que é a que você já viu antes neste módulo:

```
Aplicação  (HTTP — o "conteúdo da carta")           ~ camadas 5-7 do OSI
Transporte (TCP — garante que a entrega seja confiável) ~ camada 4 do OSI
Rede       (IP — o "endereço" de destino)           ~ camada 3 do OSI
Física     (o meio real: cabo, wifi, fibra)         ~ camadas 1-2 do OSI
```

O TCP/IP agrupa em "Aplicação" o que o OSI separa em três camadas (Sessão, Apresentação,
Aplicação), e agrupa em "Física" o que o OSI separa em duas (Física, Enlace). Na prática do dia a
dia — e no resto deste módulo — você vai trabalhar quase sempre com o modelo TCP/IP; o OSI aparece
principalmente como vocabulário compartilhado ("isso é um problema de camada 2" já comunica algo
específico pra quem trabalha com redes).

### 8. Encapsulamento

Cada camada, ao entregar dados pra camada de baixo, "embrulha" esses dados com seu próprio
cabeçalho de controle — exatamente como um envelope dentro de outro envelope.

**Exemplo narrado:** você envia uma mensagem HTTP. A camada de Transporte (TCP) embrulha essa
mensagem com um cabeçalho TCP (contendo, entre outras coisas, a porta de origem/destino),
formando um **segmento**. A camada de Rede (IP) embrulha esse segmento com um cabeçalho IP
(contendo os endereços IP de origem/destino), formando um **pacote**. A camada Física/Enlace
embrulha esse pacote com um cabeçalho Ethernet (contendo endereços MAC), formando um **quadro**,
que finalmente vira sinal elétrico/óptico/de rádio no cabo ou no ar.

### 9. Desencapsulamento

Do lado de quem recebe, o processo acontece ao contrário: o quadro chega, a camada de Enlace
remove o cabeçalho Ethernet e entrega o pacote pra cima; a camada de Rede remove o cabeçalho IP e
entrega o segmento pra cima; a camada de Transporte remove o cabeçalho TCP e entrega a mensagem
HTTP original pra aplicação — como abrir cada envelope, do mais externo pro mais interno.

`[TENTE VOCÊ]` Ao encapsular uma mensagem, qual cabeçalho é adicionado primeiro: o TCP ou o IP?
Resposta: TCP primeiro (a mensagem passa pela camada de Transporte antes de chegar na camada de
Rede) — por isso, ao desencapsular, o cabeçalho IP é removido primeiro, e o TCP por último, bem
perto da aplicação.

## 10. Ethernet

Ethernet é o padrão mais comum da camada de Enlace/Física em redes locais — a tecnologia por trás
da maioria dos cabos de rede e switches que você já viu.

### 11. Endereço MAC

Cada placa de rede vem de fábrica com um endereço fixo, único no mundo, chamado **endereço MAC**
(Media Access Control) — pense nele como o "RG" físico daquele hardware específico, diferente do
endereço IP, que é atribuído pela rede e pode mudar. Um MAC se parece com
`00:1A:2B:3C:4D:5E` (6 pares de dígitos hexadecimais).

### 12. Switch

Um **switch** conecta vários dispositivos numa mesma LAN e decide, quadro por quadro, pra qual
porta física encaminhar cada um — olhando o endereço MAC de destino, não o IP. Diferente de um
hub antigo (que retransmitia tudo pra todas as portas), um switch aprende quais MACs estão em
quais portas e manda o quadro só pra porta certa.

### 13. ARP

Se o switch encaminha por MAC, mas você só sabe o IP do destino (ex: `192.168.1.10`), alguma coisa
precisa traduzir IP → MAC dentro da rede local. Essa é a função do **ARP** (Address Resolution
Protocol) — pense nele como "o DNS da camada de enlace": um dispositivo pergunta em broadcast "quem
tem o IP X?", e o dono desse IP responde com seu MAC.

### 14. Broadcast e Unicast

**Unicast** é uma mensagem endereçada a um único destinatário específico (a maioria do tráfego de
rede é assim). **Broadcast** é uma mensagem endereçada a *todo mundo* na rede local ao mesmo tempo
— o ARP, por exemplo, usa broadcast pra perguntar "quem tem esse IP?" porque ainda não sabe pra
quem mandar especificamente.

`[ATENÇÃO]` Broadcast não atravessa roteadores — ele fica contido dentro da rede local. Isso é
proposital: se broadcasts atravessassem a Internet inteira, ela ficaria inundada de tráfego
desnecessário.

## 15. IPv4

Você já viu, de forma resumida, que existem duas versões de endereço IP — agora vamos aprofundar o
IPv4, a versão mais antiga e ainda mais comum.

### 16. Endereço IP

O **IPv4** escreve o endereço como 4 números de 0 a 255 separados por ponto, por exemplo
`192.168.1.1`. Cada um desses números é 1 byte (8 bits), e o endereço inteiro tem 32 bits — o que
dá `2³²`, pouco mais de 4,3 bilhões de endereços possíveis (retome a conexão com "`n` bits
representam `2ⁿ` valores" do módulo 03).

### 17. Máscara de rede

Um endereço IP sozinho não diz "onde termina a rede e onde começa o dispositivo individual" — é
pra isso que existe a **máscara de rede**. Ela é escrita no mesmo formato de um IP (ex:
`255.255.255.0`) e, bit a bit, indica quais posições do endereço pertencem à "parte de rede" (bits
`1` na máscara) e quais pertencem à "parte de host" (bits `0` na máscara).

**Exemplo narrado:** o IP `192.168.1.10` com máscara `255.255.255.0` significa que os três
primeiros números (`192.168.1`) identificam a rede, e o último número (`10`) identifica o
dispositivo específico dentro dela — todo dispositivo de `192.168.1.1` até `192.168.1.254` está na
mesma rede local.

### 18. Network e Broadcast

Dentro de toda sub-rede, dois endereços são reservados e **não podem** ser atribuídos a nenhum
dispositivo: o **endereço de rede** (todos os bits de host em `0` — identifica a rede em si, ex:
`192.168.1.0`) e o **endereço de broadcast** (todos os bits de host em `1` — usado pra mandar uma
mensagem pra todos os dispositivos da sub-rede de uma vez, ex: `192.168.1.255`).

### 19. Gateway

O **gateway** (ou "gateway padrão") é o dispositivo — geralmente seu roteador — que serve de
"portão de saída" da sua rede local pra qualquer destino fora dela. Quando seu computador precisa
mandar dados pra um IP que não está na mesma sub-rede, ele manda primeiro pro gateway, que decide
o próximo passo.

### 20. IP público e IP privado

**IP privado** é usado dentro de redes locais e não é roteável na Internet pública (faixas
reservadas, como `192.168.x.x` e `10.x.x.x`) — vários dispositivos diferentes, em redes diferentes
ao redor do mundo, podem ter o mesmo IP privado sem conflito, porque nenhum deles é visível de
fora. **IP público** é único no mundo inteiro e é o que identifica sua rede de fora — normalmente,
uma casa inteira compartilha um único IP público (o do roteador), com todos os dispositivos
internos usando IPs privados por trás dele (conexão direta com NAT, mais adiante).

### 21. Subnetting

**Subnetting** é o processo de dividir uma rede grande em sub-redes menores, cada uma isolada das
outras — útil pra organizar (ex: separar rede de convidados da rede interna) e pra não desperdiçar
endereços. Isso é feito ajustando a máscara de rede: uma máscara "maior" (mais bits `1`) cria
sub-redes menores, com menos endereços de host disponíveis cada.

### 22. CIDR

**CIDR** (Classless Inter-Domain Routing) é a notação compacta pra escrever uma máscara de rede: em
vez de `255.255.255.0`, você escreve `/24` — o número depois da barra é quantos bits, contados da
esquerda, são "1" na máscara. `192.168.1.0/24` significa exatamente a mesma coisa que "rede
`192.168.1.0` com máscara `255.255.255.0`".

**Exemplo narrado:** dado o IP `192.168.1.50/24`, os primeiros 24 bits (`192.168.1`) são a rede,
restando 8 bits (o último octeto) pra hosts — de `192.168.1.1` até `192.168.1.254` (excluindo
`.0`, endereço de rede, e `.255`, broadcast), um total de 254 hosts utilizáveis.

`[TENTE VOCÊ]` Uma rede `10.0.5.0/24` — qual é o endereço de broadcast dela? Resposta:
`10.0.5.255` (últimos 8 bits todos em `1`, já que `/24` deixa exatamente 8 bits pra host).

## 23. IPv6

O esgotamento do IPv4 (só ~4,3 bilhões de endereços, insuficiente pra bilhões de pessoas com vários
dispositivos cada) motivou a criação do **IPv6**.

### 24. Estrutura do IPv6

IPv6 usa endereços de **128 bits** em vez de 32 — `2¹²⁸`, um número tão grande que não há risco
realista de esgotar tão cedo. Escrito em 8 grupos de 4 dígitos hexadecimais separados por
dois-pontos, por exemplo `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (grupos de zeros consecutivos
podem ser abreviados com `::`, uma única vez por endereço).

### 25. IPv4 vs IPv6

`[TENTE VOCÊ]` Por que 32 bits (IPv4) só dão ~4,3 bilhões de endereços, mas 128 bits (IPv6) já
resolvem o problema por décadas? Resposta: porque a quantidade de valores representáveis cresce
como potência de 2 conforme o número de bits — `2³²` é grande, mas `2¹²⁸` é astronomicamente maior
(seria como comparar o número de grãos de areia numa praia com o número de átomos no universo
observável). Cada bit a mais *dobra* a quantidade de endereços possíveis — é o mesmo princípio de
"`n` bits representam `2ⁿ` valores" do módulo 03, só que aplicado a um endereço de rede.

### 26. Endereçamento IPv6

IPv6 também usa o conceito de prefixo/CIDR (ex: `2001:db8::/32`), mas não precisa de NAT do jeito
que IPv4 precisa — há endereços de sobra pra cada dispositivo ter um IP público próprio, se
necessário. Isso não elimina a necessidade de firewalls, só a necessidade de "esconder" vários
dispositivos atrás de um único IP por escassez.

## 27. Roteamento

Depois de endereçar dispositivos (IPv4/IPv6), alguém precisa decidir *por onde* os dados viajam
entre redes diferentes — essa é a função do roteamento.

### 28. Roteador

Um **roteador** conecta redes diferentes entre si (diferente do switch, que conecta dispositivos
*dentro* de uma mesma rede) e decide, pacote por pacote, qual é o próximo salto na direção do
destino final.

### 29. Tabela de roteamento

Cada roteador mantém uma **tabela de roteamento**: uma lista de "pra chegar nesta faixa de
endereços, mande pra esse próximo salto". Ao receber um pacote, o roteador consulta essa tabela
pra decidir o próximo passo.

### 30. Rota padrão

Quando nenhuma entrada específica da tabela bate com o destino, o roteador usa a **rota padrão**
("default route") — basicamente "se eu não sei especificamente pra onde mandar isso, manda pra
cá" (geralmente, o próximo roteador em direção à Internet).

### 31. NAT

**NAT** (Network Address Translation) é o mecanismo que traduz os IPs privados de uma rede local
pro único IP público do roteador, e vice-versa — é por isso que vários dispositivos numa casa
conseguem acessar a Internet compartilhando um IP público só. O roteador mantém uma tabela
temporária de "qual dispositivo interno pediu o quê", pra rotear a resposta de volta pro
dispositivo certo.

### 32. Firewall

Um **firewall** filtra tráfego de rede segundo um conjunto de regras — permitindo ou bloqueando
pacotes com base em critérios como IP de origem/destino, porta, ou protocolo. Pode existir como
hardware dedicado, como parte do roteador, ou como software rodando no próprio sistema
operacional (o Windows e o Linux já vêm com firewall próprio).

`[TENTE VOCÊ]` Sua casa tem 5 dispositivos conectados no wifi, todos acessando a Internet
simultaneamente, mas seu provedor só atribuiu 1 IP público pra sua conexão. O que torna isso
possível? Resposta: NAT — o roteador traduz os IPs privados dos 5 dispositivos pro único IP
público na saída, e mantém controle de qual resposta pertence a qual dispositivo interno.

## 33. TCP

**TCP** (Transmission Control Protocol) garante que os dados cheguem completos e na ordem certa,
mesmo que a rede física real embaralhe pacotes ou perca pedaços no caminho — ele confere o que
chegou, pede reenvio do que faltou, e remonta tudo na ordem original antes de entregar pra
aplicação.

### 34. UDP

**UDP** (User Datagram Protocol) é uma alternativa ao TCP que abre mão da garantia de entrega em
troca de velocidade e simplicidade — sem handshake, sem confirmação, sem reenvio automático.

### 35. TCP vs UDP

Por que dois protocolos, e não um só? Porque são situações diferentes: em uma chamada de vídeo, é
preferível perder um quadro (UDP) do que travar esperando o reenvio de um pacote perdido (TCP) —
um pequeno defeito visual é menos ruim que uma pausa perceptível. Já num download de arquivo,
perder um pedaço silenciosamente corromperia o arquivo inteiro — ali, a garantia do TCP é
essencial.

`[ATENÇÃO]` Confundir IP com TCP é comum no início. Fixe assim: IP é **"pra onde"**, TCP/UDP é
**"como a entrega é gerenciada"**.

### 36. Portas

Um dispositivo pode rodar várias aplicações de rede ao mesmo tempo (um navegador, um cliente de
e-mail, um jogo online) — todas usando o mesmo endereço IP. **Portas** (números de 0 a 65535)
distinguem qual aplicação, dentro daquele IP, deve receber cada pacote. HTTP usa a porta 80 por
convenção, HTTPS a 443, e assim por diante — retome a tabela de referência mais abaixo neste
módulo.

### 37. Sockets

Um **socket** é a combinação **IP + porta** que identifica de forma única uma conexão de rede
específica — retome a conexão com o módulo 06: é exatamente essa abstração que o sistema
operacional oferece pra uma aplicação mandar/receber dados pela rede sem lidar com cabos ou
roteamento diretamente.

### 38. Three-Way Handshake

Antes de trocar dados de verdade, TCP estabelece a conexão com uma "negociação" de 3 mensagens:

```
Cliente → Servidor:  SYN       (quero conectar)
Servidor → Cliente:  SYN-ACK   (ok, também quero — e confirmo seu pedido)
Cliente → Servidor:  ACK       (confirmado, vamos começar)
```

Só depois desse handshake completo é que os dados de verdade (ex: a requisição HTTP) começam a
trafegar.

### 39. Controle de fluxo

O **controle de fluxo** evita que o emissor mande dados mais rápido do que o receptor consegue
processar — o receptor sinaliza quanto espaço de buffer ainda tem disponível, e o emissor ajusta o
ritmo de envio a isso.

### 40. Controle de congestionamento

O **controle de congestionamento** é parecido, mas olha pra rede como um todo, não só pro
receptor: se o TCP detecta perda de pacotes (sinal de que a rede está congestionada em algum
ponto do caminho), ele reduz o ritmo de envio pra aliviar essa rota, e vai aumentando de novo
gradualmente enquanto tudo continuar chegando bem.

## 41. DNS

Você já viu que pacotes na rede são roteados usando endereços IP — não nomes. Mas ninguém digita
`142.250.219.174` na barra de endereços; todo mundo digita `google.com`. Alguma coisa precisa
traduzir o nome legível pro endereço numérico que a rede de fato usa — essa é a única função do
**DNS** (Domain Name System). A analogia mais direta é a agenda de contatos do seu celular: você
toca em "Mãe" pra ligar, não digita o número decorado.

### 42. Domínios

Um **domínio** (ex: `github.com`) é o nome legível registrado que aponta pra um ou mais IPs. Um
**subdomínio** (ex: `api.github.com`) é uma subdivisão desse domínio, geralmente apontando pra um
servidor ou serviço diferente do domínio principal.

### 43. Resolução de nomes

**Exemplo narrado:** você digita `exemplo.com` na barra de endereços. *Antes* de qualquer coisa
acontecer com HTTP, o navegador precisa saber pra qual IP mandar a requisição — então ele pergunta
pro DNS "qual é o IP de `exemplo.com`?". O DNS responde com um endereço (ex: `93.184.216.34`). Só
então o navegador monta a requisição HTTP e a envia pra esse IP.

### 44. DNS Records

Um domínio pode ter vários tipos de registro DNS, cada um respondendo a um tipo de pergunta
diferente:

| Tipo | O que responde |
|---|---|
| `A` | O endereço IPv4 do domínio |
| `AAAA` | O endereço IPv6 do domínio |
| `CNAME` | "Este nome é só um apelido — a resposta de verdade está em outro nome" |
| `MX` | Qual servidor recebe e-mails para esse domínio |

### 45. DNS recursivo e autoritativo

Quando seu dispositivo pergunta "qual o IP de `exemplo.com`?", ele geralmente não pergunta direto
pro dono do domínio — ele pergunta pro **servidor DNS recursivo** do seu provedor de internet, que
faz esse trabalho de "correr atrás" da resposta em cadeia, até achar o **servidor autoritativo**
(o dono oficial daquele domínio, que tem a resposta definitiva) e trazer a resposta de volta pra
você.

### 46. Cache DNS

Pra não repetir essa busca inteira toda vez, a resposta é guardada em cache — no seu navegador, no
seu sistema operacional, e no servidor recursivo do provedor — por um tempo definido (TTL) pelo
dono do domínio.

`[ATENÇÃO]` Quando um site muda de servidor (e portanto de IP), a atualização do registro DNS
precisa "propagar" por todos esses níveis de cache espalhados pelo mundo — não é instantânea. É
por isso que, logo depois de uma migração, algumas pessoas acessam normalmente e outras (usando
cache desatualizado) veem erro ou a versão antiga por um tempo.

`[TENTE VOCÊ]` Se você já sabe o IP de um servidor, é possível digitar o IP direto na barra de
endereços em vez do domínio? Resposta: sim — o DNS é uma etapa de conveniência (nomes são mais
fáceis de lembrar), não uma exigência técnica do protocolo.

## 47. Internet x Web

Assim como uma estrada não é a mesma coisa que os caminhões que rodam nela, **Internet** não é a
mesma coisa que **Web**. Internet é a infraestrutura física e os protocolos de transporte (TCP/IP)
que conectam bilhões de dispositivos no mundo. Web é um serviço específico que roda por cima
dessa infraestrutura, usando um protocolo de aplicação particular: o **HTTP**. E-mail, por
exemplo, também roda sobre a Internet — mas usa outros protocolos de aplicação, então não é "Web".

## 48. HTTP

HTTP funciona em ciclos de **requisição-resposta**: seu navegador monta uma requisição pedindo um
recurso, e o servidor responde com esse recurso (ou com um erro, se algo deu errado).

**Exemplo narrado:** você digita uma URL. O navegador primeiro resolve o domínio via DNS pra
descobrir o IP do servidor; só então monta uma requisição HTTP pedindo aquela página, e envia pra
esse IP. O servidor recebe, processa, e responde com HTML — que o navegador então interpreta e
renderiza na tela.

### 49. HTTPS

**HTTPS** é HTTP rodando sobre uma camada de criptografia — protege o conteúdo da requisição e da
resposta contra quem estiver "escutando" a rede pelo caminho (ex: alguém na mesma rede wifi
pública). Hoje é o padrão esperado; navegadores marcam sites sem HTTPS como "não seguros".

### 50. TLS

A criptografia por trás do HTTPS se chama **TLS** (Transport Layer Security). De forma resumida:
antes de trocar qualquer dado de verdade, cliente e servidor fazem um "handshake TLS" pra negociar
uma chave de sessão compartilhada — a partir daí, tudo que trafega entre os dois é embaralhado com
essa chave, ilegível pra qualquer um no meio do caminho sem ela.

### 51. URL

Uma URL se decompõe em partes, cada uma com um papel específico:
```
https://exemplo.com/produtos?categoria=livros
  |         |            |          |
protocolo  domínio    caminho   query string
(como conversar) (com quem) (o quê especificamente) (parâmetros extras)
```

`[TENTE VOCÊ]` Decomponha `https://learngitbranching.js.org/?locale=pt_BR` nas suas partes.
Resposta: protocolo `https`, domínio `learngitbranching.js.org`, caminho `/` (a raiz do site),
query string `locale=pt_BR`.

### 52. Métodos HTTP

Toda requisição HTTP declara um **método**, indicando a intenção:

| Método | Intenção |
|---|---|
| `GET` | Buscar um recurso, sem alterar nada no servidor |
| `POST` | Criar um novo recurso (ex: enviar um formulário) |
| `PUT` | Substituir um recurso existente por completo |
| `PATCH` | Atualizar parte de um recurso existente |
| `DELETE` | Remover um recurso |

### 53. Status Codes

A resposta sempre vem com um código de status, agrupado por faixa:

```
1xx = informativo   (raro de ver diretamente)
2xx = sucesso        (200 OK, 201 Created)
3xx = redirecionamento (301 Moved Permanently, 302 Found)
4xx = erro do cliente  (404 Not Found, 401 Unauthorized)
5xx = erro do servidor (500 Internal Server Error)
```

### 54. Headers

**Headers** são metadados enviados junto com a requisição e a resposta, fora do "conteúdo"
principal — ex: `Content-Type` (que tipo de dado está sendo enviado), `Authorization` (credenciais
de acesso), `Cache-Control` (regras de cache).

### 55. Cookies

HTTP é, por natureza, **sem estado**: cada requisição é isolada, o servidor não "lembra" da
anterior sozinho. **Cookies** resolvem isso — um pequeno dado que o servidor pede pro navegador
guardar e reenviar em toda requisição futura àquele domínio, permitindo reconhecer o mesmo
visitante entre uma requisição e outra.

### 56. Sessions

Uma **session** é o mecanismo do lado do *servidor* que geralmente usa um cookie contendo só um ID
de sessão — o servidor guarda os dados de verdade (ex: "usuário logado como Maria") associados a
esse ID, em vez de confiar no cookie pra carregar informação sensível diretamente.

### 57. Cache HTTP

Headers como `Cache-Control` dizem ao navegador (ou a servidores intermediários) por quanto tempo
pode reutilizar uma resposta já recebida, sem precisar pedir de novo — evitando requisições
repetidas desnecessárias pra conteúdo que não muda com frequência (ex: uma imagem de logo).

`[ATENÇÃO]` Confundir "cookie" com "cache" é comum: cookie identifica *quem* está fazendo a
requisição; cache evita *refazer* uma requisição cuja resposta você já tem.

## 58. HTML

HTML é a estrutura da página que o servidor devolve numa resposta HTTP bem-sucedida — o
aprofundamento completo de HTML fica pro módulo 10; aqui, o que importa é o papel dele nesse
ciclo: é o "conteúdo" que viaja dentro da resposta HTTP.

### 59. Cliente Web

O **cliente Web** é quem inicia a requisição — na prática, quase sempre um navegador, mas também
pode ser um app mobile, um script, ou o próprio `curl` que você vai usar na prática deste módulo.

### 60. Servidor Web

O **servidor Web** é o programa que escuta requisições HTTP numa porta (geralmente 80/443) e
responde — pode servir arquivos estáticos prontos (HTML/CSS/imagens) ou gerar a resposta
dinamicamente, consultando um banco de dados antes de responder.

### 61. Browser

O **navegador** (browser) faz muito mais que só mandar a requisição e mostrar a resposta bruta:
ele interpreta o HTML, aplica o CSS, executa JavaScript, gerencia cookies/cache/sessions
automaticamente, e renderiza tudo isso como a página visual que você vê.

## 62. API HTTP

Uma **API** (Application Programming Interface) HTTP é um servidor que responde **dados**
(geralmente em JSON), não uma página pronta pra um humano ler — pensada pra ser consumida por
código, não por um navegador exibindo diretamente pra uma pessoa.

### 63. REST

**REST** é um estilo (não um protocolo formal) de organizar APIs HTTP em torno de **recursos**
(ex: `/usuarios`, `/pedidos/42`) e **métodos HTTP** (`GET /usuarios` lista, `POST /usuarios` cria,
`DELETE /pedidos/42` remove) — reaproveitando a semântica dos métodos já vistos, em vez de
inventar um vocabulário próprio pra cada ação.

### 64. JSON

**JSON** (JavaScript Object Notation) é o formato de dados mais comum pra respostas de API —
texto estruturado em pares chave-valor, fácil de ler tanto por humano quanto por código:
```json
{"nome": "Maria", "idade": 22, "ativo": true}
```

### 65. CORS

**CORS** (Cross-Origin Resource Sharing) é uma política de segurança que o *navegador* aplica: por
padrão, uma página de `siteA.com` não pode chamar uma API de `siteB.com` via JavaScript, a menos
que `siteB.com` explicitamente autorize isso através de headers específicos na resposta. Existe
pra impedir que um site malicioso "roube" ações em nome do usuário em outro site sem permissão.

`[TENTE VOCÊ]` Uma API responde `{"erro": "CORS bloqueado"}` quando chamada do navegador, mas
funciona perfeitamente quando testada com `curl`. Por que essa diferença? Resposta: CORS é uma
regra de segurança imposta pelo *navegador*, não pelo servidor nem pela rede — `curl` não é um
navegador, então não aplica essa restrição.

## 66. Protocolos de aplicação

HTTP é só *um* protocolo de aplicação entre vários — o que você escolhe usar depende da tarefa.

### 67. SSH

**SSH** (Secure Shell) permite acessar remotamente o terminal de outra máquina de forma
criptografada — é assim que desenvolvedores administram servidores sem estar fisicamente na frente
deles (`ssh usuario@servidor`).

### 68. FTP e SFTP

**FTP** (File Transfer Protocol) é mais antigo que HTTP e serve pra transferir arquivos entre
cliente e servidor — enviar, baixar, listar, apagar. Diferente de HTTP (pensado pra "pedir uma
página"), FTP foi desenhado em torno de operações de arquivo. Seu problema: tráfego sem
criptografia. **SFTP** (SSH File Transfer Protocol) faz a mesma coisa, mas rodando sobre uma
conexão SSH criptografada — por isso é a escolha recomendada hoje em dia.

### 69. SMTP

**SMTP** (Simple Mail Transfer Protocol) é o protocolo por trás do *envio* de e-mail — quando você
aperta "enviar", seu cliente de e-mail conversa com um servidor usando SMTP pra entregar a
mensagem até o servidor de destino.

### 70. IMAP

**IMAP** cuida da outra ponta: *ler* e sincronizar uma caixa de entrada entre vários dispositivos
(o e-mail continua no servidor, o app só sincroniza o que exibir) — diferente do POP3, mais antigo,
que baixava e geralmente removia do servidor.

### 71. WebSocket

Diferente do request-response do HTTP (o cliente sempre inicia), **WebSocket** estabelece uma
conexão **persistente e bidirecional** — depois do "handshake" inicial (que começa como uma
requisição HTTP, mas evolui pra esse novo tipo de conexão), tanto cliente quanto servidor podem
mandar mensagens a qualquer momento, sem precisar de uma requisição nova a cada troca. É a base de
funcionalidades em tempo real, como chat.

`[TENTE VOCÊ]` Você precisa enviar um e-mail com um relatório em anexo. Dois protocolos diferentes
estão envolvidos — quais? Resposta: SMTP entrega a mensagem até o servidor de destino; se depois
você acessar essa caixa de entrada por um app de e-mail, a leitura usa IMAP — SMTP só cobre o
envio.

`[ATENÇÃO]` Não confunda "protocolo de aplicação" com "a aplicação em si": FTP e um cliente FTP (o
programa que você abre pra usar FTP) não são a mesma coisa, exatamente como HTTP e um navegador
não são a mesma coisa.

## Aplicações web atuais

A maioria das aplicações web modernas segue um padrão parecido: o servidor expõe uma API (vista
acima), e uma aplicação separada — rodando no navegador — consome essa API e monta a interface do
lado do cliente. É a base do que você vai construir no módulo 13 (JavaScript/Node), consumindo e
expondo esse tipo de API.

## 72. Diagnóstico de rede

Tudo que você viu até aqui (endereçamento, DNS, camadas, TCP) tem comandos de terminal
correspondentes que tornam esses conceitos visíveis, em vez de abstratos.

### 73. ping

Testa se um host responde, e mede o tempo de ida e volta (latência):
```
ping google.com
```

### 74. traceroute / tracert

Mostra cada "salto" de roteador até o host de destino — `tracert` no Windows, `traceroute` no
Mac/Linux:
```
tracert google.com
```

### 75. nslookup

Consulta o DNS manualmente e mostra o IP resolvido — é literalmente o comando que faz, na sua mão,
a mesma consulta que o navegador faz sozinho antes de qualquer requisição HTTP:
```
nslookup google.com
```

### 76. dig

Alternativa ao `nslookup`, mais detalhada, comum em Linux/Mac (no Windows, geralmente via WSL) —
mostra os registros DNS brutos, incluindo TTL e o tipo de registro (retome o tópico 44):
```
dig google.com
```

### 77. curl

Ferramenta de linha de comando que monta e envia uma requisição HTTP e mostra a resposta bruta na
tela, sem renderizar nada (sem CSS, sem imagens, só o texto puro que o servidor devolveu):
```
curl https://exemplo.com
curl -v https://exemplo.com   # -v (verbose) também mostra a requisição enviada e os headers
```

### 78. ip / ipconfig

Mostra o seu próprio endereço IP — `ipconfig` no Windows, `ifconfig` ou `ip addr` no Mac/Linux:
```
ipconfig
```

### 79. netstat / ss

Lista as conexões de rede ativas na sua máquina no momento — útil pra ver quais portas estão
abertas/em uso, e por qual processo:
```
netstat -an     # Windows/Mac/Linux (sintaxe varia)
ss -tulnp       # Linux, equivalente mais moderno
```

### 80. Testando portas

Além de ver conexões já ativas, às vezes você precisa testar se uma porta específica está aberta
num host remoto — uma forma simples é tentar uma conexão TCP direta a ela (ex: com `curl` mesmo,
ou com ferramentas dedicadas como `Test-NetConnection` no PowerShell):
```
Test-NetConnection google.com -Port 443
```

### 81. Analisando tráfego com Wireshark

O **Wireshark** é uma ferramenta gráfica de captura de pacotes — ele mostra, quadro a quadro, tudo
que trafega pela sua interface de rede, com cada camada de encapsulamento (Ethernet, IP, TCP,
HTTP) visível e separável na interface. É a ferramenta que torna literal tudo que este módulo
explicou de forma abstrata: você vê o cabeçalho TCP, o cabeçalho IP, o quadro Ethernet, cada um
como uma camada real dentro do pacote capturado — útil pra depurar problemas de rede que os
comandos acima não explicam sozinhos.

`[TENTE VOCÊ]` Rode `ping` e `nslookup` para um domínio real no seu terminal agora. O `ping`
respondeu com um tempo em milissegundos? O IP que o `nslookup` mostrou é o que você esperava?

## Conceitos Fundamentais de Rede — Referência Rápida

| Conceito | O que é | Para aprofundar |
|---|---|---|
| HTTP/HTTPS | Protocolo de transferência de hipertexto. Define como cliente e servidor trocam mensagens. HTTPS adiciona criptografia TLS sobre o HTTP. | [MDN — Visão geral do HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview) |
| URL | Uniform Resource Locator. Endereço completo de um recurso: `scheme://user:pass@host:port/path?query#hash` | [MDN — O que é uma URL?](https://developer.mozilla.org/pt-BR/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL) |
| DNS | Domain Name System. Traduz nomes legíveis (google.com) em endereços IP. É a "agenda telefônica" da internet. | [Cloudflare — O que é DNS?](https://www.cloudflare.com/pt-br/learning/dns/what-is-dns/) |
| Domínio e Subdomínio | Domínio: github.com. Subdomínio: api.github.com. O subdomínio aponta para um servidor ou serviço diferente. | [MDN — Nomes de domínio](https://developer.mozilla.org/pt-BR/docs/Learn/Common_questions/Web_mechanics/What_is_a_domain_name) |
| TCP/IP | Protocolos de transporte da internet. TCP garante entrega ordenada e confiável de pacotes; IP cuida do roteamento. | [Cloudflare — O que é TCP/IP?](https://www.cloudflare.com/pt-br/learning/ddos/glossary/tcp-ip/) |
| Porta | Número que identifica um serviço específico em um host. HTTP=80, HTTPS=443, Node local=3000, PostgreSQL=5432. | [MDN — Portas TCP e UDP](https://developer.mozilla.org/en-US/docs/Glossary/Port) |
| Status HTTP | 1xx=informativo, 2xx=sucesso, 3xx=redirecionamento, 4xx=erro do cliente, 5xx=erro do servidor. | [MDN — Códigos de status HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status) |
| Headers | Metadados enviados junto com requisições e respostas: Content-Type, Authorization, Cache-Control, etc. | [MDN — HTTP Headers](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers) |
| Subnetting/CIDR | Dividir uma rede em sub-redes menores; `/24` é a notação compacta pra máscara. | [Cloudflare — O que é CIDR?](https://www.cloudflare.com/pt-br/learning/network-layer/what-is-cidr/) |
| Modelo OSI | Referência acadêmica de 7 camadas pra organizar responsabilidades de rede. | [Cloudflare — Modelo OSI](https://www.cloudflare.com/pt-br/learning/ddos/glossary/open-systems-interconnection-model-osi/) |

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Confundir Internet (infraestrutura) com Web (um serviço específico que roda sobre ela).
- Confundir IP ("pra onde") com TCP/UDP ("como a entrega é gerenciada").
- Achar que uma URL é só o domínio, esquecendo caminho e query string.
- Achar que "endereço IP" é uma coisa só, sem diferenciar IPv4 (32 bits) de IPv6 (128 bits).
- Esquecer que, antes de qualquer requisição HTTP, o navegador precisa resolver o domínio via DNS.
- Achar que HTTP é o único protocolo de aplicação que existe.
- Confundir cookie (identifica quem está pedindo) com cache (evita refazer o pedido).
- Achar que broadcast atravessa roteadores como unicast — ele fica contido na rede local.
- Confundir "protocolo de aplicação" com "a aplicação em si" (FTP não é o cliente FTP).

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Sockets e gerência de E/S | Módulo 06 — Sistemas Operacionais (pré-requisito, revisão) |
| `n` bits → `2ⁿ` valores (aplicado a endereços IPv4/IPv6) | Módulo 03 — Sistemas de Numeração (revisão) |
| Requisições HTTP, APIs REST e JSON | Módulo 13 — JavaScript/Node.js (consumo de APIs) |
| Estrutura de uma página (HTML) | Módulo 10 — HTML & CSS |

## `[REFERÊNCIA]`

- KUROSE, J. F.; ROSS, K. W. *Redes de Computadores e a Internet — Uma Nova Abordagem*, 3ª ed.,
  Pearson Education / Makron Books, 2005.
- [MDN — Visão geral do HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview)
- [Cloudflare Learning Center — DNS, TCP/IP, CIDR, modelo OSI e mais](https://www.cloudflare.com/pt-br/learning/)
- [curl — documentação oficial](https://curl.se/docs/manpage.html)
- [Wireshark — documentação oficial](https://www.wireshark.org/docs/)

## Checklist de saída

- [ ] Explico a arquitetura em camadas (OSI e TCP/IP) usando uma analogia própria, e sei o que é
      encapsulamento/desencapsulamento.
- [ ] Diferencio MAC de IP, e sei o papel do ARP e do switch numa rede local.
- [ ] Calculo a rede, o broadcast e a faixa de hosts de um endereço IPv4 com máscara CIDR (ex:
      `/24`).
- [ ] Diferencio IPv4 de IPv6 (formato do endereço e por que o IPv6 existe).
- [ ] Explico o que NAT e firewall fazem numa rede doméstica.
- [ ] Diferencio TCP de UDP e sei quando cada um é preferível.
- [ ] Descrevo o three-way handshake do TCP.
- [ ] Explico o que o DNS faz, os principais tipos de registro, e em que momento do fluxo (antes
      do HTTP) ele entra em ação.
- [ ] Diferencio Internet de Web.
- [ ] Decomponho uma URL em protocolo, domínio, caminho e query string.
- [ ] Descrevo o ciclo de requisição-resposta do HTTP, incluindo métodos, status codes, headers,
      cookies e sessions.
- [ ] Explico o que é uma API REST e por que existe CORS.
- [ ] Nomeio pelo menos três protocolos de aplicação além do HTTP (SSH, SMTP, FTP/SFTP, IMAP,
      WebSocket) e digo pra que cada um serve.
- [ ] Uso `ping`, `tracert`/`traceroute`, `ipconfig`/`ip`, `nslookup`/`dig`, `netstat`/`ss` e
      `curl` pra diagnosticar rede na prática.
