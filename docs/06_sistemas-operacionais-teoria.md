---
id: 06_sistemas-operacionais-teoria
title: "Módulo 06 — Sistemas Operacionais"
sidebar_position: 60
---

# Módulo 06 — Sistemas Operacionais

> **Objetivo:** entender o papel do sistema operacional como intermediário entre hardware e
> aplicações, e como ele gerencia processos, memória, arquivos e dispositivos de E/S — da teoria
> até o uso real da linha de comando Linux.
> **Pré-requisitos:** Módulo 05 (Arquitetura de Computadores).
> **Tempo de referência:** 8 a 10 horas (módulo extenso — pode ser dividido em vários dias).
> **Prática correspondente:** [06_sistemas-operacionais-pratica.md](06_sistemas-operacionais-pratica.md)

---

## 1. Por que isso importa

No módulo 05 você viu que a CPU executa uma instrução de cada vez, seguindo o ciclo
fetch-decode-execute. Mas o seu computador roda dezenas de programas "ao mesmo tempo" — navegador,
editor de texto, música tocando. Como isso é possível, se a CPU só faz uma coisa por vez? A
resposta é a camada de software que fica entre o hardware e cada programa, decidindo quem usa a
CPU e quando: o sistema operacional. Entender o que ele faz explica, por exemplo, por que dois
programas não conseguem "invadir" a memória um do outro, por que a sensação de simultaneidade é
uma ilusão bem construída, e — na segunda metade deste módulo — como controlar tudo isso
diretamente pelo terminal Linux, a ferramenta de trabalho mais comum em servidores e ambientes de
desenvolvimento profissional.

## 2. O que é um sistema operacional

Um sistema operacional (SO) é o programa que gerencia todos os recursos de hardware (CPU, memória,
disco, rede, dispositivos) e oferece uma interface consistente para que outros programas
("aplicações") os usem sem precisar saber os detalhes de cada peça física. Sem um SO, cada
aplicativo teria que reimplementar do zero como falar com o disco, com a rede, com o teclado — e
dois aplicativos rodando ao mesmo tempo poderiam facilmente atropelar um ao outro tentando usar o
mesmo pedaço de memória ou o mesmo arquivo.

## 3. Níveis de organização da máquina

```
Hardware (CPU, memória, dispositivos — o que você viu no módulo 05)
  → Sistema Operacional (kernel)
    → Aplicações (navegador, editor de texto, seu programa)
```

O sistema operacional abstrai o hardware: uma aplicação pede "leia este arquivo" sem precisar
saber em qual setor físico do disco os dados estão — do mesmo jeito que você dirige um carro sem
precisar entender a injeção eletrônica por baixo do capô.

## 4. Kernel e User Space

O **kernel** é o núcleo do sistema operacional — a parte que roda com acesso direto e privilegiado
ao hardware. Tudo que não é kernel (seu navegador, seu editor de texto, o programa que você
escreveu no módulo 08) roda no **user space** ("espaço do usuário"): uma área isolada, sem acesso
direto ao hardware, justamente para que um programa com bug (ou malicioso) não consiga travar a
máquina inteira ou ler a memória de outro programa.

`[ATENÇÃO]` "Kernel" não é sinônimo de "sistema operacional inteiro" — o SO completo inclui o
kernel mais uma porção enorme de programas de suporte (shell, bibliotecas, utilitários). O kernel
é só o núcleo com acesso privilegiado.

## 5. Kernel Mode e User Mode

Essa separação entre kernel e user space é reforçada pelo próprio processador: a CPU tem um bit de
modo que indica se está rodando em **modo kernel** (privilegiado, acesso total ao hardware) ou
**modo usuário** (restrito, sem acesso direto a memória alheia ou dispositivos). Um programa comum
roda inteiramente em modo usuário — e quando precisa de algo que só o kernel pode fazer (ler um
arquivo, por exemplo), ele não acessa o disco diretamente: ele pede ao kernel.

## 6. Funções do sistema operacional

- **Gerência de processos**: decidir quem usa a CPU e quando.
- **Gerência de memória**: alocar e proteger a memória usada por cada processo.
- **Gerência de arquivos**: organizar dados em disco de forma estruturada (sistema de arquivos).
- **Gerência de E/S**: intermediar o acesso a teclado, tela, rede, disco.
- **Interface com o usuário**: linha de comando ou interface gráfica.

## 7. Gerenciamento de recursos

Todas as funções acima são, no fundo, uma única responsabilidade vista de ângulos diferentes:
**arbitrar recursos escassos entre programas que competem por eles**. CPU, RAM e disco são finitos
— o SO decide, a cada instante, quem recebe quanto de cada um, tentando ser justo (todo processo
avança) e eficiente (o hardware não fica ocioso à toa).

## 8. Abstração de hardware

Cada modelo de disco, cada placa de rede, cada teclado tem detalhes elétricos e de protocolo
diferentes — mas uma aplicação não precisa saber nada disso. O SO oferece uma interface uniforme
("leia bytes deste arquivo", "envie estes dados pela rede") que funciona igual não importa a marca
do hardware por trás. Essa abstração é o que permite que o mesmo programa rode em computadores
fisicamente diferentes sem ser reescrito.

## 9. System Calls

Um programa comum não pode acessar hardware diretamente — por segurança e estabilidade (lembra do
modo kernel x modo usuário?). Quando um programa precisa de algo que só o kernel pode fazer (ler
um arquivo, criar um processo, alocar memória), ele faz uma **system call** (chamada de sistema):
uma requisição formal ao kernel, que troca temporariamente para modo kernel, executa a operação
com seus privilégios, e devolve o controle ao programa em modo usuário. É a única porta de entrada
legítima entre o user space e o hardware.

**Exemplo narrado:** quando seu programa em C++ do módulo 08 chama `std::cin >> numero`, por trás
dos panos a biblioteca padrão eventualmente faz uma system call (como `read()`, no Linux) pedindo
ao kernel os bytes digitados no teclado — o programa nunca conversa com o driver do teclado
diretamente.

`[TENTE VOCÊ]` Por que um programa não pode simplesmente escrever direto num endereço de memória
do disco, sem passar por uma system call? Resposta: porque isso violaria o isolamento entre modo
usuário e modo kernel — um programa com bug (ou malicioso) poderia corromper dados de outros
processos ou do próprio SO. A system call existe justamente para que o kernel valide e controle
cada acesso.

## 10. Drivers

Um **driver** é o software específico que sabe conversar com um dispositivo de hardware exato (um
modelo de placa de vídeo, um modelo de impressora). O kernel oferece uma interface genérica
("imprimir", "desenhar na tela"), e o driver de cada dispositivo traduz isso nos comandos elétricos
exatos que aquele hardware entende. Sem o driver certo, o SO até reconhece que um dispositivo
existe, mas não sabe como falar com ele.

## Nível: Processos

## 11. Processos

**Processo** é um programa em execução (com seu próprio espaço de memória, estado, etc.) —
diferente de **programa**, que é apenas o arquivo executável parado em disco, sem nenhuma dessas
coisas ainda alocadas.

## 12. Programa vs Processo

`[ATENÇÃO]` É fácil tratar "processo" e "programa" como sinônimos — mas o programa é só o arquivo
em disco (estático, sem estado); o processo só existe enquanto está rodando, com memória e estado
próprios. O mesmo programa pode gerar vários processos ao mesmo tempo — abra três abas do mesmo
navegador e você terá (em geral) três processos diferentes rodando a partir do mesmo arquivo
executável.

## 13. Estados de um processo

Como você viu no módulo 05, a CPU só executa uma instrução por vez. Com mais processos do que
núcleos de CPU disponíveis, o sistema operacional não roda tudo em paralelo de verdade — ele
alterna rapidamente entre os processos (escalonamento), dando fatias curtas de tempo pra cada um,
como uma pessoa alternando a atenção entre várias conversas tão rápido que parece estar em todas
ao mesmo tempo. A simultaneidade que você percebe é essa troca acontecendo rápido demais para o
olho humano notar.

Um processo passa por estados ao longo de sua vida:

```
Novo → Pronto → Executando → (Bloqueado ↔ Executando) → Terminado
```

**Exemplo narrado:** um processo entra em "Pronto" assim que está preparado, mas só passa a
"Executando" quando o escalonador decide dar a vez a ele. Se, no meio da execução, ele precisar
esperar algo lento (ex: uma resposta de disco), o sistema operacional o tira de "Executando" e
coloca em "Bloqueado" — assim a CPU não fica parada esperando, e pode dar a vez a outro processo
"Pronto" nesse meio tempo. Quando o disco responde, o processo volta para "Pronto", na fila para
executar de novo.

`[TENTE VOCÊ]` Um processo está em "Executando" e faz uma leitura de arquivo, que demora. Pra
qual estado ele vai, e por quê? Resposta: "Bloqueado" — ele está esperando uma operação lenta de
E/S, e fica parado até ela terminar, liberando a CPU para outro processo nesse meio tempo.

## 14. Process Control Block

Todo processo que o SO gerencia tem uma "ficha" associada, o **Process Control Block** (PCB) —
uma estrutura de dados guardada pelo kernel contendo tudo que é preciso pra pausar e retomar
aquele processo exatamente de onde parou: o valor de cada registrador no momento da pausa, o
estado atual (Pronto/Bloqueado/etc.), a lista de arquivos abertos, e mais. É o PCB que torna
possível trocar de processo sem perder progresso.

## 15. Process ID (PID)

Cada processo recebe, na criação, um número único enquanto estiver vivo: o **PID** (Process ID).
É por esse número que você (ou o SO) se refere a um processo específico — por exemplo, pra
encerrá-lo.

## 16. Processos pai e filho

Um processo pode criar outro — o processo que cria é o **pai**, o processo criado é o **filho**.
**Exemplo narrado:** ao abrir um terminal e digitar um comando, o próprio terminal (um processo)
cria um processo filho pra executar aquele comando; quando o comando termina, o filho encerra e o
terminal continua rodando.

## 17. Criação e finalização de processos

Um processo nasce (via uma system call de criação — no Linux, `fork()` seguido de `exec()`) e
termina de dois jeitos: normalmente (executou tudo e retornou um código de saída, geralmente `0`
para sucesso) ou anormalmente (foi encerrado à força, ou travou com um erro). O SO libera os
recursos do processo terminado (memória, PID, arquivos abertos) para reuso.

## 18. Context Switch

**Context switch** (troca de contexto) é o ato de o escalonador pausar um processo em execução,
salvar seu estado completo no PCB, carregar o PCB de outro processo, e retomar a execução dele —
tudo isso acontecendo rápido o suficiente (milhares de vezes por segundo) pra criar a ilusão de
simultaneidade já explicada.

`[ATENÇÃO]` Context switch não é "grátis" — salvar e restaurar todo o estado consome tempo de CPU
que não é gasto executando o trabalho real de nenhum processo. Trocar de contexto com frequência
demais (muitos processos disputando pouca CPU) reduz a eficiência geral do sistema.

## Nível: Threads e Concorrência

## 19. Threads

Uma **thread** é um "fio de execução" dentro de um processo. Diferente de processos (que são
isolados, cada um com sua própria memória), várias threads do mesmo processo **compartilham** o
mesmo espaço de memória — o que torna a comunicação entre elas mais rápida, mas também mais
arriscada (uma thread pode acidentalmente sobrescrever um dado que outra thread do mesmo processo
está usando).

## 20. Processo vs Thread

| | Processo | Thread |
|---|---|---|
| Memória | Isolada, própria | Compartilhada com as outras threads do mesmo processo |
| Criação | Mais "cara" (mais recursos alocados) | Mais leve/rápida de criar |
| Comunicação entre eles | Precisa de mecanismos explícitos (ex: arquivos, sockets) | Direta, via memória compartilhada — mas exige cuidado |
| Isolamento de falhas | Um processo travando não derruba outro | Uma thread travando pode derrubar o processo inteiro |

## 21. Threads dentro de um processo

**Exemplo narrado:** um navegador moderno costuma ter uma thread cuidando da interface (pra não
travar a tela enquanto carrega uma página), outra baixando o conteúdo da rede, outra decodificando
um vídeo — todas dentro do mesmo processo, compartilhando o mesmo espaço de memória (ex: o cache
de imagens já carregadas fica acessível pra todas).

## 22. Concorrência

**Concorrência** é a capacidade de várias tarefas progredirem dentro do mesmo período de tempo,
mesmo que não estejam executando no exato mesmo instante — elas podem estar intercaladas num único
núcleo de CPU, como o escalonamento de processos já visto.

## 23. Paralelismo

**Paralelismo** é mais específico: várias tarefas executando literalmente ao mesmo tempo, em
núcleos de CPU diferentes — o que só é possível numa CPU multicore (retome a conexão com o módulo
05).

`[TENTE VOCÊ]` Um computador com 1 núcleo de CPU rodando 5 processos ao mesmo tempo tem
concorrência, paralelismo, ou os dois? Resposta: só concorrência — com 1 núcleo, é fisicamente
impossível dois processos executarem no mesmo instante; o que existe é alternância rápida
(escalonamento).

## 24. Escalonamento de processos

**Escalonamento** é a decisão de qual processo (dentre os "Prontos") recebe a CPU a seguir, e por
quanto tempo.

## 25. Scheduler

O **scheduler** (escalonador) é o componente do kernel responsável por essa decisão — ele roda a
cada context switch, escolhendo o próximo processo com base numa política (round-robin, prioridade,
etc.).

## 26. Preemptivo vs não preemptivo

- **Preemptivo**: o SO pode interromper um processo em execução à força, mesmo que ele não tenha
  terminado nem pedido pra parar — garante que nenhum processo monopolize a CPU indefinidamente.
  É o modelo usado por praticamente todo SO moderno (Linux, Windows, macOS).
- **Não preemptivo (cooperativo)**: um processo só libera a CPU voluntariamente (quando termina ou
  quando decide esperar por algo). Se um processo mal-comportado nunca libera a CPU, o sistema
  inteiro trava — modelo usado em sistemas antigos/simples.

## 27. Prioridades

Nem todo processo é igualmente urgente — o SO permite atribuir **prioridades**, e o scheduler tende
a favorecer processos de prioridade mais alta na hora de decidir quem executa a seguir. `[ATENÇÃO]`
Prioridade não é garantia absoluta de execução imediata — é só um peso na decisão do scheduler,
pra evitar que um processo de baixa prioridade nunca rode (fome de recursos), a maioria dos
schedulers ainda dá alguma chance de execução até pros processos "menos importantes".

## 28. Context Switching (revisão)

Já visto no tópico 18 — repare que ele é o mecanismo *físico* por trás de qualquer decisão de
escalonamento: toda vez que o scheduler decide trocar quem executa, é um context switch que
executa essa troca.

## 29. Estados e filas de processos

Na prática, o SO organiza processos "Prontos" numa **fila de prontos**, e processos "Bloqueados"
esperando por diferentes eventos (disco, rede, teclado) em **filas de espera** separadas por tipo
de evento — quando o evento que um processo bloqueado esperava acontece, ele sai da fila de espera
e volta pra fila de prontos, de onde o scheduler pode escolhê-lo de novo.

## Nível: Gerência de Memória

## 30. Gerência de memória

Assim como um processo precisa de um espaço isolado pra rodar sem interferir em outro, a memória
RAM inteira do computador precisa ser dividida entre todos os processos ativos — sem que um leia
ou sobrescreva o espaço do outro por acidente ou má-fé.

## 31. Memória virtual

É pra isso que existe a **memória virtual**: cada processo enxerga um espaço de memória próprio e
isolado, como se tivesse a máquina inteira só pra ele, mesmo que fisicamente vários processos
estejam dividindo a mesma RAM.

`[ATENÇÃO]` Memória virtual não é a mesma coisa que RAM física — é uma camada de abstração que
pode, inclusive, usar espaço em disco quando a RAM não é suficiente. Quando isso acontece, o
sistema fica visivelmente mais lento, porque disco é muito mais lento que RAM (lembra da
hierarquia de memória do módulo 05?).

## 32. Espaço de endereçamento

O **espaço de endereçamento** de um processo é a faixa completa de endereços de memória virtual
que ele enxerga como "sua" — tipicamente organizada em regiões bem definidas: código do programa,
dados globais, heap, e stack (próximo tópico).

## 33. Stack e Heap

- **Stack** (pilha): memória usada automaticamente para variáveis locais de função e controle de
  chamadas — cresce e encolhe sozinha conforme funções são chamadas e retornam (LIFO: a última
  função chamada é a primeira a "desempilhar"). Retome o módulo 08: toda variável local declarada
  dentro de uma função em C++ vive na stack.
- **Heap**: memória alocada dinamicamente, sob demanda do programa (em C++, via `new`), e que
  precisa ser gerenciada explicitamente (ou por um coletor de lixo, em linguagens como JavaScript)
  — não cresce/encolhe automaticamente como a stack.

`[TENTE VOCÊ]` Uma variável `int x = 5;` declarada dentro de uma função C++ vai pra stack ou pra
heap? Resposta: stack — é uma variável local comum, sem alocação dinâmica explícita.

## 34. Paginação

A memória virtual é implementada através de **paginação** — a memória é dividida em blocos de
tamanho fixo (páginas), e o SO mapeia páginas virtuais (o que o processo "acha" que está usando)
para endereços físicos reais (onde os dados realmente estão).

## 35. Page

Uma **page** (página) é a unidade básica dessa divisão — tipicamente 4 KB em sistemas modernos.
Toda a memória virtual e física é organizada em blocos desse tamanho, o que simplifica o mapeamento
entre os dois espaços.

## 36. Page Fault

Um **page fault** acontece quando um processo tenta acessar uma página que não está atualmente na
RAM física (por exemplo, foi movida pro disco por falta de espaço). O kernel intercepta esse
acesso, busca a página no disco, carrega de volta na RAM, ajusta o mapeamento, e só então deixa o
processo continuar — tudo isso de forma transparente pro programa, que nem percebe que aconteceu
(exceto pela lentidão).

## 37. Swap

**Swap** é o espaço em disco reservado para guardar páginas de memória que não cabem mais na RAM
física — é o "extravasamento" já mencionado na memória virtual. Usar swap com frequência (porque a
RAM está sempre cheia) é chamado de "thrashing", e deixa o sistema perceptivelmente lento, porque
disco é ordens de grandeza mais lento que RAM.

## 38. Memory Mapping

**Memory mapping** (mapeamento de memória, `mmap` no Linux) é uma técnica onde um arquivo em disco
é mapeado diretamente no espaço de endereços de um processo — o processo pode ler/escrever nele
como se fosse memória comum, e o kernel cuida de sincronizar com o disco por trás dos panos, sem
precisar de chamadas explícitas de leitura/escrita a cada acesso.

## Nível: Sistemas de Arquivos

## 39. Sistemas de arquivos

Um **sistema de arquivos** é a estrutura que organiza como dados são guardados e recuperados num
dispositivo de armazenamento — sem ele, um disco seria só uma sequência gigante de bytes sem
nenhuma noção de "onde termina um arquivo e começa outro".

## 40. Arquivos e diretórios

Um **arquivo** é uma sequência nomeada de bytes; um **diretório** (pasta) é uma estrutura que
agrupa arquivos (e outros diretórios) de forma hierárquica — a "árvore" de pastas que você já usa
no Windows desde o módulo 08.

## 41. File Descriptors

Quando um processo abre um arquivo, o kernel não devolve o arquivo inteiro pra ele — devolve um
**file descriptor**: um número inteiro pequeno que o processo usa daí em diante pra se referir
àquele arquivo aberto (ler, escrever, fechar). No Linux, todo processo já nasce com três file
descriptors padrão: `0` (entrada padrão), `1` (saída padrão) e `2` (saída de erro).

## 42. Inodes

No Linux, cada arquivo tem um **inode** — uma estrutura separada do nome do arquivo, guardando os
metadados reais (dono, permissões, tamanho, data de modificação, e onde os dados ficam fisicamente
no disco). O nome do arquivo que você vê num diretório é só um "apelido" apontando pra um inode —
isso é o que torna possível o próximo tópico.

## 43. Permissões

Todo arquivo/diretório no Linux tem permissões de **leitura (r)**, **escrita (w)** e **execução
(x)**, definidas separadamente para três categorias: o **dono**, o **grupo**, e **outros**. Você
vai usar isso na prática com `chmod` mais adiante neste módulo.

## 44. Ownership

**Ownership** (posse) é quem é o dono de um arquivo — cada arquivo pertence a um usuário e a um
grupo. Só o dono (ou o superusuário `root`) pode, por padrão, alterar as permissões de um arquivo.

## 45. Links simbólicos e hard links

- **Hard link**: uma segunda entrada de nome apontando pro *mesmo inode* de um arquivo já
  existente — os dois nomes são igualmente "o arquivo original", não existe um "original" e uma
  "cópia".
- **Link simbólico** (symlink): um arquivo especial e pequeno que só contém o *caminho* de outro
  arquivo/pasta — como um atalho. Se o arquivo original for apagado, o symlink fica "quebrado"
  (apontando pra nada); um hard link não tem esse problema, porque aponta direto pro inode.

## 46. Mount

**Mount** (montar) é o ato de anexar um sistema de arquivos (um disco, uma partição, um
dispositivo USB) a um ponto específico da árvore de diretórios existente — no Linux, tudo vive
numa única árvore a partir de `/`, e "conectar" um disco novo significa escolher em qual pasta
seu conteúdo vai aparecer (diferente do Windows, que dá uma letra de unidade nova, tipo `D:`).

## 47. Partições e sistemas de arquivos

Um disco físico pode ser dividido em **partições** — seções independentes, cada uma podendo ter
seu próprio sistema de arquivos (ext4 e Btrfs são comuns no Linux; NTFS no Windows). Uma máquina
pode, por exemplo, ter uma partição com o sistema operacional e outra separada para dados do
usuário.

## Nível: Gerência de E/S

## 48. Gerência de Entrada e Saída

A gerência de E/S do sistema operacional coordena o acesso a todo dispositivo que troca dados com
o mundo externo — teclado, tela, disco, rede.

## 49. Dispositivos de E/S

Cada dispositivo (impressora, mouse, placa de rede) tem características bem diferentes de
velocidade e forma de comunicação — o SO precisa lidar com essa diversidade sem expor essa
complexidade toda pras aplicações.

## 50. Drivers (revisão)

Já visto no tópico 10 — repare que é exatamente aqui, na gerência de E/S, que os drivers entram em
ação: cada dispositivo tem o seu, traduzindo pedidos genéricos do SO em comandos específicos.

## 51. Buffers

Um **buffer** é uma área de memória temporária usada pra suavizar a diferença de velocidade entre
quem produz dados e quem consome — por exemplo, ao ler um arquivo grande, o SO lê um pedaço maior
de uma vez pro buffer, e o programa consome dali aos poucos, evitando pedir ao disco byte por
byte (o que seria extremamente lento, dado o que você já sabe sobre latência de disco no módulo
05).

## 52. Interrupções (revisão)

A gerência de E/S usa exatamente o mecanismo de interrupções que você viu no módulo 05: o
dispositivo avisa quando termina uma operação por meio de uma interrupção, em vez de o SO ficar
checando repetidamente (polling) se já terminou — muito mais eficiente.

## 53. DMA

**DMA** (Direct Memory Access) permite que um dispositivo (ex: disco, placa de rede) transfira
dados diretamente para a memória RAM **sem** passar pela CPU a cada byte — a CPU só inicia a
transferência e é avisada (por interrupção) quando ela termina, ficando livre pra fazer outra
coisa nesse meio tempo. Sem DMA, transferir um arquivo grande manteria a CPU ocupada só copiando
bytes, um de cada vez.

## 54. I/O síncrono vs assíncrono

- **Síncrono (bloqueante)**: o processo que pede uma operação de E/S fica parado ("Bloqueado",
  lembra do tópico 13?) até ela terminar.
- **Assíncrono (não bloqueante)**: o processo dispara a operação de E/S e continua fazendo outra
  coisa, sendo notificado (ou verificando depois) quando ela terminar — mais complexo de
  programar, mas evita desperdiçar tempo de CPU esperando.

## Nível: Concorrência e Sincronização

## 55. Concorrência e sincronização

Quando múltiplas threads (ou processos) compartilham um mesmo recurso (uma variável, um arquivo),
é preciso coordenar o acesso — caso contrário, o resultado final pode depender da ordem exata em
que cada uma executou, o que é imprevisível e gera bugs difíceis de reproduzir.

## 56. Race Condition

Uma **race condition** (condição de corrida) acontece quando duas threads acessam o mesmo dado
compartilhado ao mesmo tempo, sem coordenação, e o resultado final depende de qual delas "ganhou a
corrida" pra executar primeiro.

**Exemplo narrado:** duas threads leem o saldo de uma conta bancária (R$ 100) ao mesmo tempo, cada
uma soma R$ 50 e escreve de volta. Se as duas leem antes de qualquer uma escrever, o resultado
final é R$ 150 — quando deveria ser R$ 200 (as duas somas aplicadas). Uma das atualizações "se
perdeu" porque não houve coordenação.

## 57. Critical Section

A **seção crítica** é o trecho de código que acessa o recurso compartilhado e precisa de acesso
exclusivo — só uma thread por vez pode estar executando essa seção, senão a race condition do
exemplo acima acontece.

## 58. Mutex

Um **mutex** (mutual exclusion, exclusão mútua) é uma trava que só uma thread pode segurar por vez
— antes de entrar na seção crítica, a thread "pega" o mutex; ao sair, "solta". Se outra thread
tentar pegar um mutex já segurado, ela espera até ser liberado.

## 59. Semáforos

Um **semáforo** generaliza a ideia do mutex: em vez de permitir só 1 acesso simultâneo, um
semáforo permite até **N** acessos simultâneos a um recurso (um mutex é, na prática, um semáforo
com N=1). Útil quando um recurso suporta um número limitado (mas maior que 1) de usuários ao
mesmo tempo — ex: um pool de N conexões de banco de dados.

## 60. Deadlocks

Um **deadlock** acontece quando duas (ou mais) threads ficam esperando eternamente uma pela outra
— por exemplo, a thread A segura o mutex 1 e espera o mutex 2; a thread B segura o mutex 2 e
espera o mutex 1. Nenhuma das duas consegue avançar, porque cada uma está esperando um recurso que
a outra não vai soltar.

`[ATENÇÃO]` Deadlocks não travam o sistema inteiro necessariamente — só as threads envolvidas
ficam paradas para sempre, o que ainda assim é um bug grave (a funcionalidade daquelas threads
simplesmente para de responder).

`[TENTE VOCÊ]` Duas threads, A e B, cada uma segura um mutex diferente e espera pelo mutex da
outra. O que evitaria esse deadlock? Resposta: definir uma ordem fixa e consistente para pegar os
mutexes (ex: sempre pegar o mutex 1 antes do mutex 2, nunca ao contrário) — assim as duas threads
nunca ficam esperando uma pela outra em sentido cruzado.

## Nível: Linux

## 61. Linux

**Linux** é, tecnicamente, apenas o kernel — mas no uso comum, "Linux" se refere ao sistema
operacional completo construído em torno desse kernel (kernel + shell + utilitários + gerenciador
de pacotes, entre outros). É open-source, gratuito, e a base da imensa maioria dos servidores do
mundo — por isso, entender Linux por linha de comando é uma habilidade quase obrigatória para
quem trabalha com desenvolvimento e infraestrutura.

## 62. Kernel Linux

O kernel Linux, criado por Linus Torvalds em 1991, é mantido de forma colaborativa e aberta —
qualquer pessoa pode ler, estudar e propor mudanças ao código-fonte
(kernel.org). Ele é monolítico (a maior parte das funções do SO roda dentro do próprio kernel,
diferente de kernels micro que isolam mais componentes em processos separados), mas altamente
modular — drivers e funcionalidades podem ser carregados/descarregados dinamicamente.

## 63. Distribuições Linux

O kernel sozinho não é usável — uma **distribuição** ("distro") empacota o kernel Linux junto com
um conjunto de programas, gerenciador de pacotes e configurações padrão, formando um sistema
completo e instalável. Ubuntu, Debian, Fedora e Arch são exemplos de distribuições populares —
todas compartilham o mesmo kernel, mas diferem em filosofia, gerenciador de pacotes e público-alvo.

## 64. Linux vs Windows

| | Linux | Windows |
|---|---|---|
| Código-fonte | Aberto (open-source) | Fechado (proprietário) |
| Kernel | Monolítico, customizável | Monolítico híbrido |
| Uso comum | Servidores, desenvolvimento | Desktops, uso geral |
| Interface padrão | Linha de comando forte, GUI opcional | GUI como padrão |
| Custo | Gratuito | Licenciado (majoritariamente) |

## 65. Shell

O **shell** é o interpretador de comandos — o programa que lê o que você digita no terminal,
interpreta, e executa (chamando os programas correspondentes ou as funções internas do próprio
shell). `bash` e `zsh` são shells comuns no Linux/Mac; no Windows, o equivalente é o Prompt de
Comando (cmd) ou o PowerShell, já usados desde o módulo 08.

## 66. Processos no Linux

Todo processo no Linux nasce de outro processo via `fork()` (que duplica o processo pai) seguido
geralmente de `exec()` (que substitui o conteúdo duplicado pelo novo programa a rodar) — é assim
que o shell cria processos filhos para os comandos que você digita.

## 67. Serviços e Daemons

Um **daemon** é um processo que roda em segundo plano, sem interação direta do usuário,
tipicamente iniciado junto com o sistema e ficando ativo o tempo todo (ex: um servidor web, um
servidor SSH). "Serviço" é o termo mais genérico para esse tipo de processo gerenciado pelo SO.

## 68. Systemd

**systemd** é o sistema de inicialização e gerenciamento de serviços usado pela maioria das
distribuições Linux modernas — é ele quem decide a ordem de inicialização dos serviços no boot,
monitora se continuam rodando, e reinicia automaticamente se um cair (dependendo da configuração).
O comando `systemctl` é a ferramenta principal pra interagir com ele.

## 69. Logs

**Logs** são registros textuais de eventos que aconteceram no sistema ou em um serviço específico
— essenciais para diagnosticar problemas depois que já aconteceram, já que você raramente está
olhando a tela no exato momento de uma falha. No Linux com systemd, o comando `journalctl` centraliza
o acesso aos logs; tradicionalmente, logs também ficam em arquivos de texto dentro de `/var/log`.

## Nível: Linha de Comando — Processos

## 70. Gerenciamento de processos via CLI

A partir daqui, cada comando é uma ferramenta real que você vai praticar no laboratório
correspondente — sempre com sintaxe, um exemplo de saída fabricada mas realista, e os erros mais
comuns.

### `ps` — listar processos

```
ps aux
```
Lista todos os processos do sistema, com colunas como PID, uso de CPU/memória e o comando que
originou o processo. `[REFERÊNCIA]` [man ps](https://man7.org/linux/man-pages/man1/ps.1.html).

### `top` e `htop` — monitorar em tempo real

```
top     # monitor interativo, atualiza a cada poucos segundos, já vem instalado por padrão
htop    # versão mais amigável visualmente, geralmente precisa ser instalada
```
Mostram os processos que mais consomem CPU/memória *no momento*, atualizando ao vivo — úteis pra
descobrir "o que está deixando meu sistema lento agora".

### `kill` — encerrar um processo pelo PID

```
kill <PID>       # pede ao processo pra terminar educadamente (SIGTERM)
kill -9 <PID>    # força o encerramento imediato (SIGKILL), sem chance de o processo "se despedir"
```
`[ATENÇÃO]` `kill -9` é um último recurso — como ele não dá ao processo nenhuma chance de fechar
arquivos ou liberar recursos com cuidado, prefira sempre `kill` sem `-9` primeiro, e só escale se
o processo realmente não responder.

### `pkill` — encerrar processo(s) pelo nome

```
pkill nome-do-processo
```
Evita ter que descobrir o PID manualmente com `ps` antes — mas `[ATENÇÃO]`: se o nome combinar com
mais de um processo, `pkill` mata todos eles, o que pode ser mais do que você queria.

### `jobs`, `bg` e `fg` — gerenciar processos em segundo plano

```
comando-demorado &   # roda em segundo plano (o & no final)
jobs                 # lista os processos em segundo plano da sessão atual do shell
bg %1                # retoma o job 1 em segundo plano, se estiver pausado
fg %1                # traz o job 1 de volta pro primeiro plano
```

### `nice` e `renice` — ajustar prioridade

```
nice -n 10 comando       # inicia um comando com prioridade mais baixa (mais "gentil" com os outros)
renice -n 5 -p <PID>     # muda a prioridade de um processo que já está rodando
```
Conecta diretamente com o conceito de prioridades do escalonador (tópico 27) — `nice` é a forma
prática de influenciar essa decisão.

## Nível: Linha de Comando — Arquivos

## 78. Gerenciamento de arquivos via CLI

A mesma lógica do bloco anterior, agora para navegação e manipulação de arquivos/pastas — a base
de qualquer trabalho por terminal, seja no Linux, seja no Git Bash/WSL no Windows.

### `pwd` — onde eu estou

```
pwd
```
Imprime o caminho absoluto da pasta atual (print working directory).

### `ls` — o que tem aqui

```
ls          # lista o conteúdo da pasta atual
ls -la      # inclui arquivos ocultos (-a) e detalhes como permissões/dono/tamanho (-l)
```

### `cd` — navegar entre pastas

```
cd nome-da-pasta    # entra numa subpasta
cd ..               # sobe um nível
cd ~                # vai direto pra pasta pessoal do usuário
```

### `cp` — copiar

```
cp origem.txt destino.txt
cp -r pasta-origem/ pasta-destino/    # -r é obrigatório pra copiar pastas (recursivo)
```

### `mv` — mover ou renomear

```
mv arquivo.txt outra-pasta/    # move
mv nome-antigo.txt nome-novo.txt    # renomeia (é a mesma operação, só muda o destino)
```

### `rm` — remover

```
rm arquivo.txt
rm -r pasta/     # remove uma pasta inteira, recursivamente
```
`[ATENÇÃO]` `rm` não manda nada pra lixeira — é permanente. Antes de rodar `rm -r` numa pasta,
confira com `ls` exatamente o que está prestes a apagar; o que fazer no lugar de sair rodando
`rm -rf` direto: liste primeiro, confirme visualmente, só então apague.

### `mkdir` — criar pasta

```
mkdir nome-da-pasta
mkdir -p pasta/subpasta/outra-subpasta    # -p cria toda a hierarquia de uma vez, sem erro se já existir parte dela
```

### `find` — localizar arquivos

```
find . -name "*.txt"          # procura, a partir da pasta atual, todo arquivo terminado em .txt
find . -type d -name "docs"   # procura uma pasta chamada "docs"
```

### `grep` — buscar texto dentro de arquivos

```
grep "erro" arquivo.log             # mostra as linhas que contêm "erro"
grep -r "TODO" .                    # busca recursivamente em todos os arquivos a partir daqui
grep -i "erro" arquivo.log          # ignora maiúsculas/minúsculas
```
`[TENTE VOCÊ]` Como você combinaria `find` e `grep` pra procurar a palavra "senha" dentro de todos
os arquivos `.txt` de uma pasta? Resposta: `grep -r "senha" --include="*.txt" .` (ou, alternativa
mais explícita: `find . -name "*.txt" -exec grep "senha" {} \;`).

## Nível: Linha de Comando — Permissões

## 88. Permissões Linux

Retomando os conceitos teóricos de permissões/ownership (tópicos 43-44): aqui está a ferramenta
prática pra ler e mudar isso.

### `chmod` — mudar permissões

```
chmod 755 script.sh
```
Os três dígitos representam dono/grupo/outros, cada um somando: leitura=4, escrita=2, execução=1
(ex: `7` = 4+2+1 = leitura+escrita+execução; `5` = 4+1 = leitura+execução, sem escrita).

`[ATENÇÃO]` `chmod 777` (todo mundo pode ler, escrever e executar) é um antipadrão de segurança
comum — qualquer usuário do sistema ganha controle total sobre o arquivo. O que fazer no lugar:
dê só a permissão mínima necessária pra cada categoria (ex: `755` para um script que só o dono
precisa editar, mas todos podem executar; `644` para um arquivo de dados que ninguém precisa
executar).

### `chown` — mudar o dono

```
chown novo-usuario arquivo.txt
```

### `chgrp` — mudar o grupo

```
chgrp novo-grupo arquivo.txt
```

### `sudo` — executar como superusuário

```
sudo comando
```
Roda um único comando com privilégios de administrador (`root`) — necessário para operações que
mexem em arquivos/configurações do sistema que o usuário comum não tem permissão de tocar.
`[ATENÇÃO]` Usar `sudo` sem entender o que o comando faz é uma das formas mais comuns de quebrar um
sistema Linux — sempre confira o comando antes de rodar com `sudo`.

### Usuários e grupos

O Linux é multiusuário por design: cada arquivo pertence a um usuário e a um grupo (tópico 44), e
um usuário pode pertencer a vários grupos. Isso permite, por exemplo, que um time inteiro (um
grupo) compartilhe acesso de escrita a uma pasta de projeto, sem dar esse acesso a todo o sistema.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Achar que "processo" e "programa" são a mesma coisa.
- Achar que fechar a janela de um aplicativo sempre encerra o processo imediatamente.
- Ignorar que memória virtual não é RAM física — pode envolver disco, que é muito mais lento.
- Confundir concorrência (alternância) com paralelismo (execução simultânea de verdade).
- Usar `kill -9` como primeira opção, em vez de `kill` simples.
- Rodar `rm -r` ou `chmod 777` sem checar antes o que está sendo afetado.
- Duas threads acessando o mesmo dado compartilhado sem mutex/semáforo — race condition.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Gerência de E/S | Módulo 07 — Redes de Computadores (sockets usam essa camada) |
| SO como camada intermediária | Módulo 08 — onde o interpretador/compilador roda |
| Stack e Heap | Módulo 08 — alocação de variáveis em C++ |
| Permissões (chmod) | Módulo 01 — Git (`.gitignore`, hooks executáveis) |

## `[REFERÊNCIA]`

- TANENBAUM, Andrew S. *Sistemas Operacionais Modernos*, 2ª ed., Prentice Hall, 2007.
- BROOKSHEAR, J. Glenn. *Ciência da Computação — Uma Visão Abrangente*, 7ª ed., Bookman, 2005 —
  Capítulo 3 (Sistemas Operacionais).
- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/) — documentação
  oficial do kernel Linux.
- [Microsoft Learn — Gerenciador de Tarefas](https://learn.microsoft.com/pt-br/windows/client-management/administrative-tools-in-windows#task-manager) —
  documentação oficial sobre gerência de processos no Windows.
- [man7.org — Linux man-pages](https://man7.org/linux/man-pages/) — referência oficial de todo
  comando Linux citado neste módulo (`ps`, `kill`, `chmod`, etc.).
- [systemd — documentação oficial](https://www.freedesktop.org/software/systemd/man/) —
  referência de `systemctl` e `journalctl`.

## Checklist de saída

- [ ] Explico a diferença entre kernel/user space e modo kernel/modo usuário.
- [ ] Explico o que é uma system call e por que ela existe.
- [ ] Explico a diferença entre processo e programa.
- [ ] Descrevo os estados possíveis de um processo e narro, com um exemplo, o que causa a
      transição entre eles.
- [ ] Diferencio processo de thread, e concorrência de paralelismo.
- [ ] Explico, com minhas próprias palavras, por que memória virtual existe, e diferencio
      stack de heap.
- [ ] Explico o que é um inode e a diferença entre hard link e link simbólico.
- [ ] Explico o que é uma race condition e como mutex/semáforo evitam esse problema.
- [ ] Comparo Linux e Windows em pelo menos 2 critérios, e sei o que systemd faz.
- [ ] Uso os comandos de processo (`ps`, `top`, `kill`, `pkill`, `jobs`), de arquivo (`pwd`, `ls`,
      `cd`, `cp`, `mv`, `rm`, `mkdir`, `find`, `grep`) e de permissão (`chmod`, `chown`, `sudo`)
      pelo terminal.
