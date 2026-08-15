---
id: 07_redes-computadores-web-pratica
title: "Módulo 07 — Redes de Computadores e Web — Prática"
sidebar_position: 71
---

# Módulo 07 — Redes de Computadores e Web — Prática

> **Objetivo da prática:** inspecionar requisições HTTP reais e decompor URLs, conectando a
> teoria a tráfego de rede real.
> **Pré-requisito:** [07_redes-computadores-web-teoria.md](07_redes-computadores-web-teoria.md)
> **Entregáveis:** um arquivo `respostas.md` neste módulo, no seu repositório do GitHub.
> **Formato de entrega:** publicado no GitHub, com README explicando a organização do repositório.

---

## Exemplo resolvido

`[CLI]` Rodando `curl -v https://example.com`:
```
> GET / HTTP/1.1
> Host: example.com
...
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=UTF-8
...
```
O `>` mostra o que foi enviado (a requisição: método `GET`, para o host `example.com`). O `<`
mostra o que foi recebido (a resposta: código de status `200 OK`, significando sucesso, e o
cabeçalho `Content-Type` dizendo que o corpo da resposta é HTML).

Agora é a sua vez.

## Exercícios

### 1. Inspecionando uma requisição real

`[CLI]` Rode `curl -v <uma URL à sua escolha>` no terminal (ou abra o DevTools do navegador, aba
Network, e recarregue uma página). Cole a saída relevante e identifique:
- O método HTTP usado (ex: `GET`).
- O código de status da resposta (ex: `200`, `404`).
- Pelo menos 2 cabeçalhos de resposta.

### 2. Decompondo URLs

Decomponha 3 URLs à sua escolha em protocolo, domínio, caminho e query string (escolha pelo menos
uma que tenha query string).

### 3. Contando requisições de uma página

Usando o DevTools (aba Network), abra um site e recarregue a página. Quantas requisições foram
feitas para carregar a página inteira (HTML, CSS, imagens, scripts, etc.)? Liste pelo menos 3
delas e diga o tipo de recurso que cada uma trouxe.

### 4. TCP x UDP

Explique com suas palavras a diferença entre TCP e UDP, e cite um exemplo de aplicação que
provavelmente usa cada um, justificando por quê.

### 5. Desafio

`[CLI]` Usando `curl -I <url>` (só cabeçalhos, sem baixar o corpo), compare os cabeçalhos de
resposta de dois sites diferentes e aponte pelo menos uma diferença entre eles.

## Laboratórios

A teoria deste módulo cresceu bastante (endereçamento IPv4/IPv6, subnetting, roteamento, TCP/UDP,
DNS completo, HTTP completo, APIs, protocolos de aplicação, diagnóstico de rede) — os
laboratórios abaixo colocam cada bloco em prática, sempre pelo terminal.

### Laboratório 82 — Endereçamento IPv4

Dado o IP `192.168.10.130` com máscara `255.255.255.192` (`/26`), calcule na mão: endereço de
rede, endereço de broadcast, e a faixa de hosts válidos. Depois confira o resultado com uma
calculadora de sub-rede online (ex: buscar "IP subnet calculator") ou, no Linux/WSL, com
`ipcalc 192.168.10.130/26`.

### Laboratório 83 — Subnetting

Você recebeu a rede `10.0.0.0/24` e precisa dividi-la em 4 sub-redes de tamanho igual. Calcule,
pra cada uma das 4 sub-redes: a nova máscara (`/26`), o endereço de rede, o de broadcast e a faixa
de hosts válidos. Mostre o raciocínio, não só o resultado final.

### Laboratório 84 — DNS

`[CLI]` Rode `nslookup github.com` (ou `dig github.com` se disponível) duas vezes seguidas. Cole
as duas saídas e responda: o IP retornado mudou? O tempo de resposta da segunda consulta foi
menor — e por quê (pense em cache DNS, já visto na teoria)? Identifique também, na saída, o tipo
de registro retornado (`A`, por exemplo).

### Laboratório 85 — TCP e UDP

`[CLI]` Rode `netstat -an` (Windows/Mac/Linux) ou `ss -tan` (Linux) com o navegador aberto em
algumas abas. Cole um trecho da saída e identifique pelo menos 3 conexões `ESTABLISHED` — o que
provavelmente está gerando cada uma (o navegador, algum app em segundo plano)?

### Laboratório 86 — HTTP

`[CLI]` Rode `curl -v <um site real>`. Na saída, identifique e cole separadamente: (1) a linha de
requisição com o método, (2) pelo menos 3 cabeçalhos de requisição, (3) o status code da
resposta, (4) pelo menos 3 cabeçalhos de resposta.

### Laboratório 87 — HTTPS

`[CLI]` Rode `curl -v <um site HTTPS>` e, na mesma saída do laboratório anterior, identifique as
linhas relacionadas à negociação TLS (o `curl -v` mostra o handshake TLS antes da requisição HTTP
em si — procure por linhas mencionando `TLS`, `SSL` ou o certificado do servidor). Explique com
suas palavras o que essas linhas indicam que está acontecendo antes da requisição HTTP começar.

### Laboratório 88 — APIs

`[CLI]` Escolha uma API REST pública gratuita e simples (ex: uma API de teste conhecida, como as
sugeridas em listas de "APIs públicas para testes"). Rode `curl <endpoint da API>`, cole o JSON
retornado, e identifique pelo menos 3 campos do JSON e o que cada um representa.

### Laboratório 89 — Diagnóstico de rede

Cenário: "o site `exemplo-lento.com` (troque por um site real de sua escolha) está demorando pra
carregar — investigue." Rode, nessa ordem, e cole a saída de cada um: `ping <site>` (há perda de
pacote? qual o tempo médio de resposta?), `tracert <site>` no Windows ou `traceroute <site>` no
Mac/Linux (em qual salto o tempo de resposta aumenta bruscamente, se aumentar?), `nslookup <site>`
(a resolução de DNS foi rápida?). Escreva uma conclusão de uma frase sobre onde pareceu estar o
gargalo, com base no que você observou.

### Laboratório 90 — Captura de tráfego

Instale o [Wireshark](https://www.wireshark.org/download.html). Inicie uma captura na sua
interface de rede principal, navegue até um site simples (ex: `example.com`), e pare a captura
depois de alguns segundos. Use o filtro `dns` e cole uma linha da captura mostrando a consulta
DNS; use o filtro `http` (ou `tls` se o site for HTTPS) e cole uma linha mostrando a
requisição/resposta.

### Laboratório 91 — Cliente e servidor

`[CLI]` Suba um servidor HTTP local simples com `python3 -m http.server 8000` (rode dentro de uma
pasta com algum arquivo, ex: um `index.html` simples). Acesse `http://localhost:8000` de duas
formas: pelo navegador, e com `curl http://localhost:8000`. Cole a saída do `curl` e explique, com
suas palavras, quem é o "cliente" e quem é o "servidor" nesse cenário — e o que muda em relação a
acessar um site na internet (dica: nada muda no protocolo, só o endereço).

## Critérios de entrega

- Todo o conteúdo publicado em um repositório no GitHub.
- Um `README.md` na raiz do repositório, explicando a organização dos arquivos.
- Cada exercício/laboratório com o enunciado copiado junto da resposta, incluindo a saída real do
  terminal/DevTools/Wireshark (não um exemplo genérico).

## Checklist de entrega

- [ ] Exercício 1 (inspecionando requisição) resolvido com saída real do terminal/DevTools.
- [ ] Exercício 2 (decompondo URLs) resolvido com as 3 URLs.
- [ ] Exercício 3 (contando requisições) resolvido com pelo menos 3 requisições listadas.
- [ ] Exercício 4 (TCP x UDP) explicado com exemplos próprios.
- [ ] Exercício 5 (comparando cabeçalhos) resolvido com a diferença apontada.
- [ ] Laboratório 82 (endereçamento IPv4) resolvido com o raciocínio mostrado.
- [ ] Laboratório 83 (subnetting) resolvido para as 4 sub-redes.
- [ ] Laboratório 84 (DNS) resolvido com as duas consultas comparadas.
- [ ] Laboratório 85 (TCP/UDP) resolvido com 3 conexões identificadas.
- [ ] Laboratório 86 (HTTP) resolvido com os 4 itens pedidos.
- [ ] Laboratório 87 (HTTPS) resolvido com a negociação TLS identificada.
- [ ] Laboratório 88 (APIs) resolvido com 3 campos do JSON explicados.
- [ ] Laboratório 89 (diagnóstico de rede) resolvido com os 3 comandos e a conclusão.
- [ ] Laboratório 90 (captura de tráfego) resolvido com as capturas DNS e HTTP/TLS.
- [ ] Laboratório 91 (cliente e servidor) resolvido com a explicação pedida.
