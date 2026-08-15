---
id: 03_sistemas-numeracao-pratica
title: "Módulo 03 — Sistemas de Numeração — Prática"
sidebar_position: 31
---

# Módulo 03 — Sistemas de Numeração — Prática

> **Objetivo da prática:** treinar conversões entre decimal, binário e hexadecimal até
> conseguir justificar cada passo — não só chegar na resposta certa por mecânica.
> **Pré-requisito:** [03_sistemas-numeracao-teoria.md](03_sistemas-numeracao-teoria.md)
> **Entregáveis:** um arquivo `respostas.md` neste módulo, no seu repositório do GitHub.
> **Formato de entrega:** publicado no GitHub, com README explicando a organização do repositório.

---

## Exemplo resolvido (para você seguir o mesmo raciocínio nos exercícios)

**Convertendo `50` para binário, pelo método das moedas (`1, 2, 4, 8, 16, 32...`):**

```
Maior moeda que cabe em 50? → 32 (sobra 18)
Maior moeda que cabe em 18? → 16 (sobra 2)
Maior moeda que cabe em 2?  → 2  (sobra 0)
```
Moedas usadas: `32, 16, 2`. Marcando `1` nessas casas e `0` nas demais:
```
32  16   8   4   2   1
 1   1   0   0   1   0   →  110010
```
Conferindo com o terminal: `python3 -c "print(bin(50))"` → `0b110010`. Bate.

Agora é a sua vez — nos exercícios abaixo, mostre o raciocínio (não só a resposta final), do
mesmo jeito que foi feito acima.

## Exercícios

### 1. Decimal → binário

Converta pelo método das moedas, mostrando cada passo: `13`, `41`, `100`, `255`.

### 2. Binário → decimal

Converta somando o valor de cada casa (posição), mostrando a soma: `1010`, `101010`, `11111111`.

### 3. Binário ↔ hexadecimal

1. Converta `11010110` para hexadecimal, mostrando o agrupamento em blocos de 4 bits.
2. Converta `0x3F` para binário e depois para decimal.

### 4. Soma binária

Some, mostrando coluna por coluna e o vai-um explicitamente (como no exemplo da teoria):
1. `0110 + 0011`
2. `1011 + 0111`

### 5. Quantos bits são necessários?

Quantos bits, no mínimo, são necessários para representar todos os números inteiros de `0` até
`1000`? Não vale só dar o número — explique o raciocínio: quantos valores diferentes `n` bits
conseguem representar, e a partir de qual `n` esse total passa de 1000.

### 6. Conferindo com o terminal

`[CLI]` Depois de resolver os exercícios 1 a 3 na mão, confira cada resposta rodando:
```
python3 -c "print(bin(N), hex(N))"          # decimal -> binário/hex
python3 -c "print(int('BINARIO', 2))"       # binário -> decimal
python3 -c "print(int('HEX', 16))"          # hex -> decimal
```
Cole, no seu arquivo de respostas, a saída do terminal ao lado de cada resposta manual. Se algo
não bater, o objetivo não é só corrigir a resposta — é achar em qual passo do raciocínio manual
o erro aconteceu, e anotar isso também.

### 7. Decimal ↔ octal, e a "quarta base"

1. Converta `41` para octal (base 8), usando o mesmo método de divisões sucessivas — só que
   dividindo por 8 em vez de por 2. Mostre cada passo.
2. Converta `0o61` (octal) de volta para decimal, somando o valor de posição de cada dígito
   (potências de 8, não de 2).
3. Converta `101001` (binário) direto para octal, agrupando de **3 em 3 bits** a partir da
   direita (não de 4 em 4 como no hexadecimal — explique por que o agrupamento muda: `2³ = 8`).
4. `[CLI]` Confira tudo com `python3 -c "print(oct(41), int('61', 8))"`.

### 8. Subtração binária

A subtração binária segue a mesma lógica da subtração decimal com "empréstimo" (borrow), do
mesmo jeito que a soma usa "vai-um" (carry) — quando falta valor numa coluna, você empresta 1 da
coluna seguinte (que vale o dobro).

1. Subtraia mostrando coluna por coluna e o empréstimo explícito: `1011 - 0011`.
2. Subtraia: `1000 - 0001` (esse exemplo tem empréstimo encadeado por várias colunas — mostre
   cada uma).
3. Agora resolva `1011 - 0011` de novo, mas usando **complemento de 2** de `0011` somado a
   `1011` (você vai fazer isso no exercício 9 — volte aqui depois de resolver o 9 e confirme que
   os dois métodos dão o mesmo resultado).

### 9. Complemento de 2 (representando negativos)

Complemento de 2 é como um computador representa números negativos usando só `0` e `1` — sem
precisar de um símbolo de `-`. Considerando registradores de 4 bits:

1. Encontre o complemento de 2 de `0011` (decimal `3`), passo a passo: inverta todos os bits
   (complemento de 1) e depois some `1`. Confirme que o resultado, interpretado como negativo,
   representa `-3`.
2. Faça o caminho inverso: dado `1101` (em complemento de 2, 4 bits), descubra que número
   decimal negativo ele representa (inverta os bits do resultado e some 1, depois leia como
   positivo e aplique o sinal de menos).
3. Volte ao exercício 8.3 e confirme, escrevendo explicitamente, que `1011 - 0011` e
   `1011 + complemento_de_2(0011)` dão o mesmo resultado (descartando o vai-um extra que
   "estoura" os 4 bits, se houver).
4. `[TENTE VOCÊ]` Por que complemento de 2 evita a necessidade de um circuito separado pra
   subtração (ele reaproveita o mesmo somador)? Resposta: porque subtrair `A - B` vira somar
   `A + complemento_de_2(B)` — o hardware só precisa saber somar, nunca subtrair de fato.

### 10. Overflow na prática, com código C++

1. Sem rodar nada ainda: preveja o que acontece se você somar `1` ao valor `255` guardado numa
   variável `unsigned char` (8 bits sem sinal, capacidade máxima `255`). Escreva sua previsão
   antes de checar.
2. Escreva e rode este programa em C++ (revise o módulo 08 se precisar relembrar como compilar no
   Windows) pra confirmar:
   ```cpp
   #include <iostream>

   int main() {
       unsigned char valor = 255;
       valor = valor + 1;
       std::cout << "Resultado: " << static_cast<int>(valor) << "\n";
       return 0;
   }
   ```
3. O resultado bateu com sua previsão? Explique, em termos de bits, por que `255 + 1` "dá a volta"
   e vira `0` num tipo de 8 bits (dica: quantos valores `8` bits representam, e o que acontece
   quando você tenta ir um valor além do maior deles).

### 11. ASCII, Unicode e UTF-8

1. Sem consultar nada, tente lembrar (ou pesquisar numa tabela ASCII) o código decimal do
   caractere `'A'` maiúsculo. Depois confira com `[CLI]` `python3 -c "print(ord('A'))"`.
2. Faça o mesmo para `'a'` minúsculo e para o dígito `'0'`. Compare os três códigos — qual a
   diferença numérica entre `'A'` e `'a'`? E entre `'0'` e o valor inteiro que ele representa?
3. Rode `python3 -c "print(len('á'.encode('utf-8')))"`. O resultado não é `1` — explique por que
   um único caractere acentuado como `á` ocupa mais de 1 byte quando codificado em UTF-8 (dica:
   ASCII original só cobre 128 símbolos — 7 bits — porque não precisava representar acentos;
   UTF-8 precisa de mais bytes pra cobrir símbolos fora desse conjunto original, mantendo
   compatibilidade com ASCII puro pros primeiros 128).

### 12. Aplicação real: endereço IP em binário

Um endereço IPv4 como `192.168.1.1` é, por baixo dos panos, 4 números de 8 bits (0-255) cada,
separados por pontos — o mesmo conceito de bits e bytes deste módulo, só que aplicado a um caso
real que você vai encontrar de novo no módulo 07 (Redes).

1. Converta cada um dos 4 octetos de `192.168.1.1` para binário (8 bits cada, com zeros à
   esquerda se precisar), e junte tudo numa sequência de 32 bits.
2. Faça o caminho inverso: dado o binário `00001010 00000000 00000000 00000001`, separe em 4
   octetos e converta cada um de volta pra decimal, remontando o endereço IP no formato usual.

## Critérios de entrega

- Todo o conteúdo publicado em um repositório no GitHub.
- Um `README.md` na raiz do repositório, explicando a organização dos arquivos.
- Cada exercício com o enunciado copiado junto da resposta, **incluindo o raciocínio passo a
  passo** — uma resposta só com o número final, sem o caminho até ela, não é considerada completa.
- No exercício 6, se alguma resposta manual não bateu com o terminal, documente onde foi o erro.
- No exercício 10, inclua o código C++ usado e a saída real do terminal (compilação + execução).

## Checklist de entrega

- [ ] Exercício 1 (decimal → binário) resolvido com o passo a passo das moedas.
- [ ] Exercício 2 (binário → decimal) resolvido com a soma das posições explícita.
- [ ] Exercício 3 (binário ↔ hexadecimal) resolvido nos dois sentidos, com o agrupamento mostrado.
- [ ] Exercício 4 (soma binária) resolvido com o vai-um explícito, coluna por coluna.
- [ ] Exercício 5 (quantos bits) resolvido com justificativa, não só o número.
- [ ] Exercício 6 (conferência via terminal) com as saídas coladas e qualquer divergência explicada.
- [ ] Exercício 7 (decimal ↔ octal) resolvido, incluindo a conversão direta binário → octal.
- [ ] Exercício 8 (subtração binária) resolvido com o empréstimo explícito.
- [ ] Exercício 9 (complemento de 2) resolvido nos dois sentidos, conectado de volta ao exercício 8.
- [ ] Exercício 10 (overflow em C++) resolvido com previsão + código + saída real.
- [ ] Exercício 11 (ASCII/Unicode/UTF-8) resolvido com os três códigos e a explicação de UTF-8.
- [ ] Exercício 12 (IP em binário) resolvido nos dois sentidos.