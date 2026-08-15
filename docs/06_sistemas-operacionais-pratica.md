---
id: 06_sistemas-operacionais-pratica
title: "Módulo 06 — Sistemas Operacionais — Prática"
sidebar_position: 61
---

# Módulo 06 — Sistemas Operacionais — Prática

> **Objetivo da prática:** explorar, no seu próprio sistema operacional, os conceitos de
> processos, threads, memória, sistemas de arquivos, concorrência e administração Linux vistos na
> teoria.
> **Pré-requisito:** [06_sistemas-operacionais-teoria.md](06_sistemas-operacionais-teoria.md)
> **Entregáveis:** um arquivo `respostas.md` neste módulo, no seu repositório do GitHub.
> **Formato de entrega:** publicado no GitHub, com README explicando a organização do repositório.

---

## Antes dos laboratórios de Linux: preparando o ambiente

Boa parte da teoria deste módulo (comandos `ps`/`top`/`kill`, permissões `chmod`/`chown`, systemd,
`journalctl`) é especificamente Linux. Se você usa Windows, o caminho mais direto pra praticar de
verdade — sem precisar de outro computador — é o **WSL** (Windows Subsystem for Linux), que roda
um Linux real dentro do Windows.

`[CLI]` Instalando o WSL (PowerShell **como administrador**):
```
wsl --install
```
Isso instala o WSL e uma distribuição Ubuntu por padrão. Depois de reiniciar, abra "Ubuntu" no
menu Iniciar, crie um usuário e senha quando pedido, e você já tem um terminal Linux completo.

Alternativas, se o WSL não for viável na sua máquina: uma distro Linux rodando numa máquina
virtual (VirtualBox/VMware) ou uma distro *live* rodando de um pendrive — ambas cobrem os mesmos
laboratórios, só exigem mais configuração inicial.

`[TENTE VOCÊ]` Depois de instalar, abra o terminal Linux e rode `whoami` e `pwd`. Resposta
esperada: `whoami` mostra o nome do usuário que você criou; `pwd` mostra seu diretório atual —
tipicamente `/home/<seu-usuario>` (o "home" do Linux, equivalente ao `C:\Users\<usuario>` do
Windows).

---

## Exercícios

### 1. Estados de um processo

Liste, na ordem correta, os estados possíveis de um processo (novo, pronto, executando,
bloqueado, terminado) e descreva o que causa a transição entre dois estados à sua escolha (ex: o
que faz um processo sair de "executando" para "bloqueado"?).

### 2. Explorando processos no seu sistema

`[CLI]` Abra um terminal e rode `ps aux` (Linux/Mac) ou abra o Gerenciador de Tarefas
(`Ctrl+Shift+Esc` no Windows). Identifique 3 processos rodando e diga, para cada um, se é um
processo do próprio sistema operacional ou de uma aplicação que você abriu.

### 3. RAM x memória virtual

Explique, com suas próprias palavras, a diferença entre memória RAM (física) e memória virtual.

### 4. Linux x Windows

Monte uma tabela comparando Linux e Windows em pelo menos 3 critérios (ex: código aberto, uso
típico, interface padrão).

### 5. Desafio — encerrando um processo

`[CLI]` Abra um aplicativo simples e seguro para encerrar via terminal (ex: um bloco de notas,
uma calculadora). Descubra o PID dele (`ps aux | grep nome` no Linux/Mac, ou a coluna PID no
Gerenciador de Tarefas no Windows) e encerre-o usando `kill <PID>` (Linux/Mac) ou
`taskkill /PID <pid> /F` (Windows). Descreva o comando exato que você usou e o resultado.

---

## Laboratórios (Linux / WSL)

Os 9 laboratórios abaixo assumem um terminal Linux (WSL ou equivalente) aberto. Cada um tem
contexto, comandos exatos e critério de aceite — documente comando + saída real no seu
`respostas.md`, não um exemplo genérico.

### Laboratório 94 — Processos

1. Rode `ps aux` e identifique 3 processos. Para um deles, anote PID, usuário dono do processo e
   comando.
2. Abra um processo de teste inofensivo em segundo plano, por exemplo:
   ```
   sleep 300 &
   ```
   Isso cria um processo que só "dorme" por 300 segundos — seguro pra matar. Anote o PID que o
   shell mostra.
3. Encerre esse processo com `kill <PID>`. Confirme com `ps aux | grep sleep` que ele sumiu.
4. Tente matar o mesmo PID de novo (`kill <PID>`). Cole o erro exato que aparece — explique por
   que ele acontece (o processo não existe mais).
5. Crie outro `sleep 300 &` e mude a prioridade dele com `renice`:
   ```
   renice -n 10 -p <PID>
   ```
   Rode `ps -o pid,ni,cmd -p <PID>` antes e depois pra mostrar o campo `NI` (nice, prioridade)
   mudando.

**Critério de aceite:** os 3 processos do passo 1 identificados corretamente; saída real dos
comandos `kill` (sucesso e erro) colada; valor de `NI` mudando confirmado.

### Laboratório 95 — Threads

1. Escolha um processo que você sabe que usa múltiplas threads (ex: seu navegador, ou o próprio
   terminal). Descubra o PID dele com `ps aux | grep <nome>`.
2. Liste as threads desse processo com:
   ```
   ps -eLf | grep <PID>
   ```
   ou, de forma interativa: `top -H -p <PID>`.
3. Conte quantas linhas (threads) apareceram para esse único processo (PID). Explique por que um
   processo aparece várias vezes aqui, mesmo sendo "um só" processo — cada linha é uma thread
   diferente rodando dentro dele.

**Critério de aceite:** saída de `ps -eLf`/`top -H` colada, com a contagem de threads explicitada
e a explicação de por que threads do mesmo processo compartilham o PID mas têm identificadores de
thread (`LWP`/`TID`) diferentes.

### Laboratório 96 — Memória

1. Rode `free -h` e anote o total de memória e quanto está livre/em uso.
2. Rode `cat /proc/meminfo | head -5` e compare os primeiros valores com o que `free -h` mostrou.
3. Crie um script simples que consome memória de propósito (cuidado, sem exagerar):
   ```
   python3 -c "a = ' ' * (200 * 1024 * 1024); input('pressione Enter para sair')"
   ```
   Isso aloca ~200MB e espera você apertar Enter. Enquanto ele está rodando, abra outro terminal
   (ou outra aba) e rode `free -h` de novo.
4. Compare o "antes" (passo 1) com o "durante" (passo 3) — quanto a memória em uso subiu?
5. Aperte Enter no primeiro terminal pra encerrar o script, rode `free -h` de novo e confirme que
   a memória foi liberada.

**Critério de aceite:** as três medições de `free -h` (antes, durante, depois) coladas, com a
diferença de uso de memória calculada e batendo aproximadamente com os ~200MB alocados.

### Laboratório 97 — Permissões

1. Crie um arquivo de teste: `echo "conteudo secreto" > teste.txt`.
2. Veja as permissões atuais com `ls -l teste.txt` — identifique dono, grupo e os três blocos de
   permissão (dono/grupo/outros).
3. Remova a permissão de leitura pra todo mundo, inclusive você: `chmod 000 teste.txt`. Tente ler
   o arquivo (`cat teste.txt`) e cole o erro de permissão negada.
4. Devolva a permissão de leitura só pro dono: `chmod 400 teste.txt`. Confirme que `cat
   teste.txt` funciona de novo.
5. Repita o passo 4 usando a notação simbólica em vez da numérica: `chmod u+r,go-r teste.txt` —
   confirme com `ls -l` que o resultado é o mesmo.
6. Se você tiver `sudo` disponível, teste `chown` pra mudar o dono do arquivo para outro usuário
   do sistema (ou pule este passo com uma explicação, se não tiver outro usuário disponível).

**Critério de aceite:** o erro de permissão negada do passo 3 colado; confirmação de que `400` e
`u+r,go-r` chegam ao mesmo resultado — conecte explicitamente com a representação octal vista no
módulo 03 (cada dígito de `chmod 400` é um número de 0 a 7, a mesma base usada lá).

### Laboratório 98 — Sistema de arquivos

1. Crie um arquivo original: `echo "original" > arquivo.txt`.
2. Crie um link simbólico e um hard link pro mesmo arquivo:
   ```
   ln -s arquivo.txt link_simbolico.txt
   ln arquivo.txt link_fisico.txt
   ```
3. Edite `arquivo.txt` (ex: `echo "editado" >> arquivo.txt`) e depois rode `cat` nos três
   arquivos (`arquivo.txt`, `link_simbolico.txt`, `link_fisico.txt`). Explique por que os três
   mostram o conteúdo atualizado.
4. Apague o arquivo original (`rm arquivo.txt`). Rode `cat` no link simbólico (deve dar erro — o
   link ficou "quebrado", apontando pra um nome que não existe mais) e no hard link (deve
   continuar funcionando — ele aponta pro mesmo inode, que só é removido quando o último link
   pra ele é apagado).
5. Rode `df -h` e identifique quantos gigabytes estão livres na partição onde você está.

**Critério de aceite:** a diferença de comportamento entre link simbólico (quebra) e hard link
(sobrevive) demonstrada e explicada em termos de inode.

### Laboratório 99 — Processos Linux (serviços do sistema)

1. Liste os serviços ativos com `systemctl list-units --type=service --state=running`.
2. Escolha um serviço não-crítico pra observar (ex: `cron` ou `rsyslog`, nunca pare um serviço
   que não reconhece). Veja o status dele: `systemctl status <servico>`.
3. Reinicie esse serviço: `sudo systemctl restart <servico>`. Rode `systemctl status <servico>`
   de novo e compare o horário de "Active since" antes e depois.

**Critério de aceite:** saída do `status` antes e depois do restart colada, mostrando o horário de
início do serviço mudando.

### Laboratório 100 — Serviços (criando o seu próprio)

1. Crie um arquivo de unidade systemd mínimo em `/etc/systemd/system/meuteste.service`:
   ```
   [Unit]
   Description=Serviço de teste da trilha

   [Service]
   ExecStart=/bin/bash -c 'while true; do echo "rodando"; sleep 5; done'

   [Install]
   WantedBy=multi-user.target
   ```
2. Recarregue o systemd e inicie o serviço:
   ```
   sudo systemctl daemon-reload
   sudo systemctl start meuteste
   sudo systemctl status meuteste
   ```
3. Pare o serviço: `sudo systemctl stop meuteste`. Confirme com `systemctl status meuteste` que
   ele está `inactive`.

**Critério de aceite:** o serviço aparecendo como `active (running)` depois do `start`, e
`inactive` depois do `stop`.

### Laboratório 101 — Logs

1. Com o serviço `meuteste` do laboratório anterior rodando de novo (`sudo systemctl start
   meuteste`), veja os logs dele: `journalctl -u meuteste`.
2. Acompanhe os logs em tempo real: `journalctl -u meuteste -f` (deixe rodando uns 15 segundos pra
   ver as linhas "rodando" aparecendo a cada 5 segundos, depois interrompa com `Ctrl+C`).
3. Reinicie o serviço (`sudo systemctl restart meuteste`) e identifique, no `journalctl`, a linha
   que marca o reinício.

**Critério de aceite:** trecho do log colado mostrando pelo menos 3 linhas "rodando" e a marca de
reinício do serviço.

### Laboratório 102 — Troubleshooting (desafio integrador)

**Cenário:** você recebe um chamado — "o serviço `meuteste` parou de responder e o disco parece
estar cheio". Investigue usando os comandos vistos nos laboratórios anteriores, nesta ordem
sugerida (mas registre tudo que você rodar, mesmo que não ajude):

1. `systemctl status meuteste` — o serviço está rodando, parado, ou com erro?
2. Se estiver parado ou com erro: `journalctl -u meuteste -n 50` — o que os últimos logs dizem?
3. `df -h` — alguma partição está com uso próximo de 100%?
4. `free -h` — a memória está esgotada?
5. `ps aux --sort=-%mem | head -5` — quais processos mais consomem memória agora?
6. Baseado no que você encontrou, escreva um parágrafo explicando a causa mais provável do
   problema (pode ser fictícia/hipotética, já que o cenário é simulado) e o comando que você
   usaria pra resolver.

**Critério de aceite:** os 5 comandos de diagnóstico rodados de verdade (mesmo que no seu sistema
não haja de fato nenhum problema — o objetivo é praticar o roteiro de investigação), com a saída
real colada, e uma conclusão escrita conectando as pistas encontradas.

## Critérios de entrega

- Todo o conteúdo publicado em um repositório no GitHub.
- Um `README.md` na raiz do repositório, explicando a organização dos arquivos.
- Cada exercício/laboratório com o enunciado copiado junto da resposta.
- Nos exercícios 2 e 5 e em todos os laboratórios, use a saída real do seu terminal — não um
  exemplo genérico.

## Checklist de entrega

- [ ] Exercício 1 (estados de um processo) resolvido com a transição explicada.
- [ ] Exercício 2 (explorando processos) resolvido com saída real do terminal.
- [ ] Exercício 3 (RAM x memória virtual) explicado com suas palavras.
- [ ] Exercício 4 (Linux x Windows) resolvido com tabela comparativa.
- [ ] Exercício 5 (encerrando um processo) resolvido com o comando usado e o resultado.
- [ ] Laboratório 94 (processos) resolvido, com o erro de `kill` repetido documentado.
- [ ] Laboratório 95 (threads) resolvido, com a contagem de threads de um processo real.
- [ ] Laboratório 96 (memória) resolvido, com as três medições de `free -h`.
- [ ] Laboratório 97 (permissões) resolvido, conectando com a base octal do módulo 03.
- [ ] Laboratório 98 (sistema de arquivos) resolvido, com a diferença link simbólico x hard link.
- [ ] Laboratório 99 (processos Linux) resolvido, com o horário de restart do serviço.
- [ ] Laboratório 100 (serviços) resolvido, com o serviço próprio criado e testado.
- [ ] Laboratório 101 (logs) resolvido, com o trecho de `journalctl` colado.
- [ ] Laboratório 102 (troubleshooting) resolvido, com o roteiro de investigação e a conclusão.
