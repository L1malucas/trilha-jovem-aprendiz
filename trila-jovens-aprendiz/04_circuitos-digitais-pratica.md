# Módulo 04 — Circuitos Digitais — Prática

> **Objetivo da prática:** fixar o comportamento das portas lógicas montando tabelas verdade e
> combinando portas para resolver problemas simples.
> **Pré-requisito:** [04_circuitos-digitais-teoria.md](04_circuitos-digitais-teoria.md)
> **Ferramenta:** [Logisim](https://logisim.app/) (navegador) — veja o [guia do Logisim](04_logisim-guia.md).
> **Entregáveis:** na pasta `modulo-04/` do seu repositório do GitHub: `respostas.md`, os arquivos `.circ` e um print de cada circuito funcionando.
> **Formato de entrega:** publicado no GitHub, com README explicando a organização do repositório.

---

## Exercícios

### 1. Tabelas verdade

Monte a tabela verdade completa (todas as combinações de entrada) para:
1. `A AND B`
2. `A OR B`
3. `A XOR B`
4. `NOT A`

**No Logisim:** baixe [`ex01_tabelas.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/ex01_tabelas.circ), monte o circuito e teste todas as combinações. Confira com **Window > Combinational Analysis**. Entregue o `.circ` + print.

### 2. Combinando portas

Monte a tabela verdade de `A AND (B OR C)` para as 8 combinações possíveis de A, B e C.

**No Logisim:** baixe [`ex02_a_and_b_or_c.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/ex02_a_and_b_or_c.circ), monte o circuito e teste todas as combinações. Compare a tabela gerada com a sua. Entregue o `.circ` + print.

### 3. XOR sem XOR

O XOR pode ser construído combinando apenas AND, OR e NOT. Monte a expressão lógica equivalente
(dica: `(A OR B) AND NOT (A AND B)`) e prove, com a tabela verdade, que ela produz o mesmo
resultado que XOR.

**No Logisim:** baixe [`ex03_xor_sem_xor.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/ex03_xor_sem_xor.circ), monte o circuito e teste todas as combinações. Ligue as mesmas entradas na porta XOR nativa e no seu circuito e confirme que `XOR_NATIVO = XOR_MONTADO`. Entregue o `.circ` + print.

### 4. Combinacional x sequencial

Explique com suas palavras a diferença entre um circuito combinacional e um sequencial, usando um
exemplo do dia a dia para cada um (por exemplo: um circuito comparador de nível de água x uma
trava de porta com memória de estado — "aberta" ou "fechada").

### 5. Desafio — meio-somador

Monte a tabela verdade completa de um meio-somador (half adder): duas entradas (A, B), duas
saídas (Soma e Carry). Identifique qual porta lógica gera a Soma e qual gera o Carry.

**No Logisim:** baixe [`ex05_meio_somador.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/ex05_meio_somador.circ), monte o circuito e teste todas as combinações. Entregue o `.circ` + print.

### 6. Flip-flop tipo D — só muda no pulso

Um flip-flop tipo D recebe a seguinte sequência de eventos, na ordem em que acontecem:

```
t0: D = 0, sem pulso de clock
t1: D = 1, sem pulso de clock
t2: pulso de clock (↑)
t3: D = 0, sem pulso de clock
t4: D = 1, sem pulso de clock
t5: pulso de clock (↑)
t6: D = 0, sem pulso de clock
```

Para cada instante (t0 a t6), diga qual valor o flip-flop está guardando **depois** desse
instante. Lembre-se: ele só atualiza o valor guardado exatamente nos instantes com pulso de
clock (`↑`) — mudanças de `D` fora desses instantes não têm efeito imediato no valor guardado.

**No Logisim:** baixe [`ex06_flipflop_d.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/ex06_flipflop_d.circ), monte o circuito e teste todas as combinações. Reproduza a sequência t0–t6 (use o clock manual, **Ctrl+K**) e confira os valores de `Q`. Entregue o `.circ` + print.

### 7. Trava com senha de 4 dígitos

Uma trava eletrônica abre com a senha `8-1-5-3`. Descreva o estado interno do circuito (quantos
dígitos corretos confirmados até agora) a cada dígito digitado, para as duas sequências abaixo,
dizendo se a trava abre ao final de cada uma:

1. O usuário digita `8-1-5-3` (na ordem certa).
2. O usuário digita `8-1-9-3` (o terceiro dígito está errado).

Para a sequência 2, explique também: mesmo que o dígito `3` no final bata com o último dígito da
senha, por que isso sozinho não é suficiente pra abrir a trava?

**No Logisim:** baixe [`ex07_trava_senha.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/ex07_trava_senha.circ), monte o circuito e teste todas as combinações. Opcional (desafio): implemente a FSM no circuito. Entregue o `.circ` + print.

## Laboratórios

Agora você **monta o circuito de verdade** no [Logisim](https://logisim.app/): cada laboratório
tem uma **Parte A (Logisim)** — monta e testa o circuito a partir de um arquivo inicial — e, nos
laboratórios 40 a 44, uma **Parte B (C++)** — a mesma lógica em código, usando só `&`, `|`, `^`,
`~` (sem o operador aritmético nativo, que descaracterizaria o exercício). Isso conecta direto
com o módulo 08: hardware e programa são a mesma lógica, só em camadas diferentes.

### Laboratório 37 — Portas lógicas

> 🔬 **Parte A (Logisim): monte `NOT (A AND B)` na saída `ORIGINAL` e a forma simplificada (só OR e NOT) na saída `SIMPLIFICADA`; confirme que são sempre iguais.** Arquivo inicial: [`lab37_portas.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab37_portas.circ).

Simplifique a expressão `NOT (A AND B)` usando as leis de De Morgan (vistas na teoria) até chegar
numa forma só com OR e NOT. Depois monte a tabela verdade das duas formas (original e
simplificada) lado a lado e confirme que são idênticas.

### Laboratório 38 — Tabelas-verdade

> 🔬 **Parte A (Logisim): monte o circuito e confira a tabela com **Window > Combinational Analysis**.** Arquivo inicial: [`lab38_tabelas_verdade.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab38_tabelas_verdade.circ).

Monte a tabela verdade completa de `(A XOR B) OR (A AND C)` para as 8 combinações de A, B, C.
Identifique, olhando só a tabela pronta, em quais linhas a saída é `1` só por causa do primeiro
termo, só por causa do segundo, ou por causa dos dois.

### Laboratório 39 — Circuito combinacional (multiplexador)

> 🔬 **Parte A (Logisim): monte o MUX só com portas e compare com o componente **Multiplexer** nativo.** Arquivo inicial: [`lab39_multiplexador.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab39_multiplexador.circ).

Um multiplexador (MUX) de 2 entradas tem duas entradas de dados (`D0`, `D1`), um bit de seleção
(`S`) e uma saída: se `S=0`, a saída repete `D0`; se `S=1`, a saída repete `D1`. Monte a tabela
verdade completa (`D0`, `D1`, `S` → saída, 8 linhas) e escreva a expressão booleana equivalente
(dica: `(NOT S AND D0) OR (S AND D1)`).

### Laboratório 40 — Meio somador em código

> 🔬 **Parte A (Logisim): monte o meio somador (exemplo na teoria). **Parte B:** o código C++ abaixo.** Arquivo inicial: [`lab40_meio_somador.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab40_meio_somador.circ).

Implemente em C++ uma função `meio_somador(bool a, bool b)` que devolve um par `(soma, carry)`,
usando só `^` (XOR) pra soma e `&` (AND) pra carry — sem usar `+`. Teste com as 4 combinações de
entrada e confira contra a tabela verdade que você já montou no exercício 5.

### Laboratório 41 — Somador completo e somador de 4 bits

> 🔬 **Parte A (Logisim): somador completo (`lab41_somador_completo.circ`) e depois o de 4 bits ([`lab41_somador_4bits.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab41_somador_4bits.circ)) com sub-circuitos. **Parte B:** o código C++ abaixo.** Arquivo inicial: [`lab41_somador_completo.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab41_somador_completo.circ).

Implemente `somador_completo(bool a, bool b, bool carry_in)`, que devolve `(soma, carry_out)`,
combinando dois meios-somadores (o carry de saída é `1` se qualquer um dos dois meios-somadores
gerou carry). Depois, encadeie 4 chamadas de `somador_completo` pra somar dois números de 4 bits
(representados como `bool[4]`), propagando o carry de uma posição pra próxima — sem usar o
operador `+` em nenhum momento. Teste somando `0101` (5) com `0011` (3) e confirme que dá `1000`
(8).

### Laboratório 42 — Registrador

> 🔬 **Parte A (Logisim): registrador de 4 bits com `LOAD` e `CLK`. **Parte B:** o código C++ abaixo.** Arquivo inicial: [`lab42_registrador.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab42_registrador.circ).

Implemente em C++ uma "classe" ou struct simples `RegistradorD` com 4 bits, que só atualiza seu
valor guardado quando um método `pulso_clock()` é chamado (do mesmo jeito que um flip-flop tipo D
só muda no pulso, exercício 6). Simule a mesma sequência de eventos do exercício 6, mas agora
para os 4 bits ao mesmo tempo, e imprima o valor guardado depois de cada pulso de clock.

### Laboratório 43 — Contador

> 🔬 **Parte A (Logisim): contador de 3 bits com `RESET`, observando a sequência `000 → 111 → 000`. **Parte B:** o código C++ abaixo.** Arquivo inicial: [`lab43_contador.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab43_contador.circ).

Implemente um contador binário de 3 bits em C++: uma função que recebe o estado atual (3 bits) e
devolve o próximo estado, incrementando 1 a cada chamada (`000 → 001 → 010 → ... → 111 → 000`,
voltando ao início — isso se chama "estourar"/*overflow* do contador). Rode a função 10 vezes
seguidas e monte a tabela da sequência de estados percorrida.

### Laboratório 44 — Máquina de estados (formalizando a trava de senha)

> 🔬 **Parte A (Logisim): desenhe o diagrama de estados e implemente a FSM da trava com flip-flops e portas. **Parte B:** o código C++ abaixo.** Arquivo inicial: [`lab44_maquina_estados.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/starters/lab44_maquina_estados.circ).

Pegue a trava de senha do exercício 7 e formalize como uma máquina de estados finita (FSM) em
C++: defina um `enum class EstadoTrava { ESPERANDO_DIGITO_1, ESPERANDO_DIGITO_2,
ESPERANDO_DIGITO_3, ESPERANDO_DIGITO_4, ABERTA }`, e uma função que recebe o estado atual + o
dígito digitado, e devolve o próximo estado (voltando pra `ESPERANDO_DIGITO_1` se o dígito
estiver errado). Rode as duas sequências do exercício 7 através dessa função e confirme que os
resultados batem com o que você já respondeu manualmente.

## Critérios de entrega

- Todo o conteúdo publicado em um repositório no GitHub.
- Um `README.md` na raiz do repositório, explicando a organização dos arquivos.
- Cada exercício com o enunciado copiado junto da resposta.
- Tabelas verdade completas — não pule combinações de entrada.
- Nos laboratórios 40-44, o código C++ deve compilar e rodar (documente a saída do terminal).
- Cada arquivo `.circ` deve abrir sem erro no Logisim, com os pins nomeados como no arquivo inicial.
- Um print de cada circuito funcionando e um parágrafo curto sobre o que você aprendeu ao montá-los.

## Checklist de entrega

- [ ] Exercício 1 (tabelas verdade básicas) resolvido para as 4 portas.
- [ ] Exercício 2 (combinação de portas) resolvido com as 8 combinações.
- [ ] Exercício 3 (XOR sem XOR) resolvido com a prova via tabela verdade.
- [ ] Exercício 4 (combinacional x sequencial) explicado com exemplos próprios.
- [ ] Exercício 5 (meio-somador) resolvido com a tabela verdade completa.
- [ ] Exercício 6 (flip-flop tipo D) resolvido para os 7 instantes.
- [ ] Exercício 7 (trava com senha) resolvido para as duas sequências, com a explicação pedida.
- [ ] Laboratório 37 (portas lógicas) resolvido com a simplificação via De Morgan.
- [ ] Laboratório 38 (tabelas-verdade) resolvido para as 8 combinações.
- [ ] Laboratório 39 (MUX) resolvido com tabela verdade e expressão booleana.
- [ ] Laboratório 40 (meio somador em código) resolvido, compilando e testado nas 4 combinações.
- [ ] Laboratório 41 (somador de 4 bits) resolvido, testado com o exemplo `0101 + 0011`.
- [ ] Laboratório 42 (registrador) resolvido, com saída documentada a cada pulso de clock.
- [ ] Laboratório 43 (contador) resolvido, com a tabela dos 10 estados percorridos.
- [ ] Laboratório 44 (máquina de estados) resolvido, confirmando os resultados do exercício 7.
- [ ] Arquivos `.circ` e prints dos exercícios/laboratórios entregues na pasta `modulo-04/`.
