---
id: 01_git-teoria
title: "Módulo 01 — Git"
sidebar_position: 10
---

# Módulo 01 — Git

> **Objetivo:** entender o que é controle de versão e dominar os 20 tópicos essenciais do Git —
> do básico (commits, branches, remotos) ao avançado (rebase, bisect, hooks, CI/CD) — organizados
> em três níveis de profundidade.
> **Pré-requisitos:** nenhum — primeiro módulo da trilha.
> **Tempo de referência:** 8 a 12 horas (é o módulo mais extenso da trilha, de propósito — Git é
> a ferramenta que você vai usar todos os dias, em todos os módulos seguintes).
> **Prática correspondente:** [01_git-pratica.md](01_git-pratica.md)

---

## Por que isso importa

Você já usa `Ctrl+Z` — desfazer uma ação, um passo de cada vez. Mas o `Ctrl+Z` do seu editor de
texto tem três limitações: some quando você fecha o programa, só funciona sozinho (se outra
pessoa mexeu no mesmo arquivo, seu histórico de "desfazer" não sabe nada sobre isso), e é
estritamente linear (não dá pra "desfazer só uma parte" e manter o resto). Git resolve as três
coisas ao mesmo tempo: um histórico permanente, compartilhável entre várias pessoas, e não-linear
(você pode ter caminhos diferentes de mudança acontecendo ao mesmo tempo, sem um atropelar o
outro). Esse módulo é a base de tudo o que vem depois na trilha — a partir daqui, todo módulo
pede entrega via GitHub.

Este módulo está organizado em três níveis. O **Básico** cobre o que você usa todo santo dia. O
**Intermediário** cobre o que você usa toda semana, quando o trabalho em equipe fica mais
complexo. O **Avançado** cobre ferramentas que resolvem problemas específicos — você não vai usar
todas elas o tempo todo, mas vai precisar saber que existem quando o problema aparecer.

---

# Nível Básico

## 1. Fundamentos

Imagine editar um documento em conjunto com um colega trocando arquivos por e-mail:
`projeto_final.docx`, depois `projeto_final_v2.docx`, depois `projeto_final_v2_CORRIGIDO.docx`.
Rapidamente fica impossível saber qual é a versão certa, o que mudou entre uma e outra, ou quem
mudou o quê. Controle de versão resolve isso guardando, de forma automática e ordenada, um
**snapshot** (uma foto completa do estado do projeto) a cada mudança significativa que você
decide registrar — chamada de **commit**. Cada commit sabe quem fez, quando, e o que mudou em
relação ao commit anterior.

Um **repositório** é o projeto inteiro rastreado dessa forma: os arquivos atuais, mais todo o
histórico de commits que levou até eles, guardado numa pasta oculta chamada `.git`.

`[CLI]`
```
git init
```
Transforma a pasta atual em um repositório Git, criando a pasta `.git` (onde todo o histórico vai
ser guardado). A partir daqui, o Git passa a observar as mudanças nos arquivos dessa pasta.

```
git status
```
Responde a pergunta "onde eu estou agora?" — mostra quais arquivos mudaram desde o último commit,
e quais dessas mudanças já estão prontas para virar o próximo commit.

`[TENTE VOCÊ]` Rode `git init` numa pasta vazia e, em seguida, `git status`. O que aparece?
Resposta: algo como "nothing to commit, working tree clean" — porque não existe nenhum arquivo
ainda para rastrear.

### `.gitignore` — o que o Git nunca deveria rastrear

Nem todo arquivo dentro de uma pasta de projeto deveria virar parte do histórico. Arquivos
gerados automaticamente (ex: pastas de dependências baixadas, como `node_modules/`) ou que
contêm dados sensíveis/locais (ex: senhas de ambiente num arquivo `.env`) não devem ser
versionados — cada pessoa que clona o repositório já gera ou configura os seus próprios. Um
arquivo `.gitignore`, na raiz do projeto, diz ao Git "nunca me pergunte sobre esses arquivos":

```
node_modules/
.env
*.log
__pycache__/
```

`[ATENÇÃO]` Se um arquivo já foi commitado *antes* de entrar no `.gitignore`, adicioná-lo à lista
não remove ele do histórico — o Git só ignora *mudanças futuras* nele. O que fazer no lugar: rode
`git rm --cached nome-do-arquivo` (remove do rastreamento sem apagar o arquivo do seu disco),
*depois* adicione ao `.gitignore`, e commit essa remoção.

`[REFERÊNCIA]` [git-scm.com/docs/git-init](https://git-scm.com/docs/git-init),
[git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore).

## 2. Commit

Um detalhe que confunde quem começa: por que não existe um único comando "salvar tudo"? Porque o
Git separa **selecionar o que vai entrar no próximo commit** (`git add`) de **de fato registrar
esse commit** (`git commit`). Pense em empacotar uma caixa para enviar pelos Correios: primeiro
você escolhe o que vai dentro da caixa (`add`), depois lacra e despacha (`commit`). Essa separação
existe porque você pode ter mexido em três arquivos diferentes, mas só quer registrar a mudança
de um deles agora — o `add` deixa você escolher exatamente isso, mesmo quando várias mudanças não
relacionadas estão acontecendo ao mesmo tempo na sua pasta de trabalho.

**Exemplo narrado:** você editou `app.py` e `notas.txt`, mas só quer registrar a mudança do
`app.py` agora:
```
git add app.py
git commit -m "adiciona validação de login"
```
`notas.txt` continua modificado no seu diretório, mas fora desse commit — ele só entra quando
você decidir dar `git add notas.txt` também.

`[ATENÇÃO]` Esquecer o `git add` antes do `git commit` é o erro mais comum no início — o commit
sai vazio, ou sem as mudanças que você esperava que estivessem lá. Rode `git status` sempre antes
de commitar, para conferir exatamente o que está preparado (staged).

`[TENTE VOCÊ]` Crie um arquivo `ola.txt` com qualquer texto, e registre-o em um commit. Resposta:
`git add ola.txt` seguido de `git commit -m "adiciona ola.txt"`.

### `git diff` — vendo exatamente o que mudou, antes de decidir

`git add` escolhe *quais arquivos* entram no commit, mas antes de decidir isso, muitas vezes você
quer conferir *o que exatamente* mudou dentro deles — não só "o arquivo `app.py` foi modificado",
mas as linhas específicas. `git diff` mostra isso.

**Exemplo narrado:** você alterou uma função em `app.py`, adicionando uma verificação de senha.
Antes de dar `git add`, você roda:
```
git diff
```
```diff
diff --git a/app.py b/app.py
index 3f8a1b2..9c7d4e5 100644
--- a/app.py
+++ b/app.py
@@ -12,7 +12,7 @@ def validar_login(usuario, senha):
     if not usuario or not senha:
         return False
-    return usuario in banco_de_dados
+    return usuario in banco_de_dados and senha == banco_de_dados[usuario]
```
Linhas com `-` (vermelho, no terminal) são o que existia antes; linhas com `+` (verde) são o que
existe agora. `git diff`, sozinho, mostra as mudanças que **ainda não foram** adicionadas com
`git add` (working directory vs. último commit). Depois de dar `git add app.py`, rodar `git diff`
de novo não mostra mais nada — porque não há diferença entre o *working directory* e o que está
*staged*. Pra ver o que está staged, comparado ao último commit, o comando é outro:
```
git diff --staged
```

`[TENTE VOCÊ]` Você editou um arquivo e já rodou `git add`. Quer conferir de novo, com calma, o
que exatamente vai entrar no commit antes de confirmar. Qual comando usa? Resposta:
`git diff --staged` — `git diff` sozinho não mostraria nada, porque a mudança já está staged.

`[REFERÊNCIA]` [git-scm.com/docs/git-add](https://git-scm.com/docs/git-add),
[git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit),
[git-scm.com/docs/git-diff](https://git-scm.com/docs/git-diff). A documentação oficial descreve
`add` como a preparação da "próxima instantânea" (*next commit*) — é literalmente esse o
vocabulário usado pelo próprio Git internamente (a *staging area* também é chamada de *index*).

## 3. Branch

Imagine que você quer testar uma mudança arriscada num projeto que já funciona, sem correr o
risco de estragar a versão estável enquanto testa. No mundo dos documentos, você faria uma cópia.
No Git, essa "cópia" se chama **branch** — só que, em vez de duplicar o projeto inteiro, o Git só
rastreia inteligentemente os pontos em que a branch nova diverge da original, o que faz criar uma
branch ser praticamente instantâneo (é só um ponteiro de 41 bytes apontando pra um commit — não
uma cópia física dos arquivos).

```
git branch nome-da-branch     # cria a branch
git switch nome-da-branch     # troca para ela
```

**Exemplo narrado:** você está na branch `main` (a branch principal, "estável"). Cria uma branch
`experimento`, troca para ela, e faz um commit lá. Se você voltar para `main` com
`git switch main`, esse commit **não aparece** no histórico da `main` — ele existe só dentro de
`experimento`, isolado, até que alguém decida trazê-lo de volta.

`[TENTE VOCÊ]` Crie uma branch chamada `teste`, faça uma mudança nela, volte para `main` e rode
`git log`. O commit da branch `teste` aparece? Resposta: não — ele só passa a existir na `main`
depois que você fizer `git merge teste` estando na `main` (mais sobre merge no tópico 6).

`[REFERÊNCIA]` [git-scm.com/docs/git-branch](https://git-scm.com/docs/git-branch),
[git-scm.com/docs/git-switch](https://git-scm.com/docs/git-switch) — a doc oficial descreve
branch como "a movable pointer" (um ponteiro que se move), o que explica por que criar/trocar de
branch é tão barato comparado a duplicar arquivos.

## 4. Remote

Até aqui, tudo aconteceu só na sua máquina. Um **remoto** (como o GitHub) é uma cópia do
repositório hospedada em outro lugar, que permite colaboração — várias pessoas mandando e
recebendo commits do mesmo lugar central.

Quando você começa um projeto localmente (com `git init`) e só depois cria o repositório vazio no
GitHub, precisa *ligar* os dois manualmente:

```
git remote add origin https://github.com/seu-usuario/seu-projeto.git
git remote -v
```
`git remote add origin <url>` registra o endereço do remoto sob o apelido `origin` (convenção
padrão — poderia ter outro nome, mas quase ninguém muda). `git remote -v` lista os remotos
configurados, confirmando que o endereço ficou certo.

`[TENTE VOCÊ]` Você quer conferir se o endereço do remoto que você configurou está correto, sem
tentar enviar nada ainda. Qual comando usa? Resposta: `git remote -v`.

`[REFERÊNCIA]` [git-scm.com/docs/git-remote](https://git-scm.com/docs/git-remote).

## 5. Fetch / Pull / Push

```
git clone <url>    # baixa uma cópia completa de um repositório remoto
git push           # envia seus commits locais para o remoto
git pull           # traz commits novos do remoto e já mescla no seu branch atual
git fetch          # só baixa a informação do remoto, sem mesclar automaticamente
```

A diferença entre `pull` e `fetch` costuma confundir: `git pull` é, na prática, um `git fetch`
seguido de um `git merge` automático. `git fetch` sozinho deixa você ver o que mudou no remoto
antes de decidir se quer trazer isso para o seu branch atual — útil quando você quer conferir
antes de misturar.

`[TENTE VOCÊ]` Você quer só ver se existem commits novos no remoto, sem aplicá-los ainda no seu
branch atual. Qual comando usa? Resposta: `git fetch`.

### Configurando a tracking branch, e o que fazer quando o push é rejeitado

No primeiro `push` de uma branch nova, é preciso avisar ao Git qual branch remota essa branch
local deve **rastrear** (a *tracking branch*) — depois disso, `git push`/`git pull` sozinhos já
sabem pra onde ir:
```
git push -u origin main
```
O `-u` (de *upstream*) faz exatamente essa ligação, uma vez só; nos próximos pushes dessa branch,
`git push` sozinho já basta.

Um push é rejeitado quando o remoto tem commits que você ainda não tem localmente (ex: outra
pessoa já enviou algo desde a última vez que você sincronizou). O Git recusa o push pra não
sobrescrever esse trabalho às cegas.

```
git push
# ! [rejected] main -> main (fetch first)
# error: failed to push some refs
```

O que fazer: trazer o que está faltando antes de tentar de novo.
```
git pull
git push
```

`[ATENÇÃO]` Existe uma forma de "forçar" o push mesmo com a rejeição (`git push --force`), mas
isso **sobrescreve** o histórico do remoto com o seu, descartando silenciosamente qualquer commit
que estivesse lá e você não tem — perigoso numa branch compartilhada, porque apaga trabalho de
outras pessoas sem aviso. O que fazer no lugar: resolva com `git pull` (trazendo e mesclando o
que está faltando) antes de tentar o push de novo; se realmente precisar forçar em algum cenário
específico (ex: reescreveu um commit só seu, ainda não visto por ninguém), use
`git push --force-with-lease` em vez de `--force` puro — ele falha com segurança se alguém mais
tiver enviado algo desde a última vez que você sincronizou, em vez de sobrescrever cegamente.

`[TENTE VOCÊ]` Depois de rodar `git push -u origin main` uma vez, o que muda no próximo commit
que você quiser enviar? Resposta: basta `git push`, sem precisar especificar `origin main` de
novo — a tracking branch já foi configurada.

`[REFERÊNCIA]` [git-scm.com/docs/git-push](https://git-scm.com/docs/git-push),
[git-scm.com/docs/git-pull](https://git-scm.com/docs/git-pull),
[git-scm.com/docs/git-fetch](https://git-scm.com/docs/git-fetch),
[git-scm.com/docs/git-clone](https://git-scm.com/docs/git-clone).

## 6. Merge

Para trazer as mudanças de uma branch de volta para outra (geralmente da sua branch de trabalho
de volta pra `main`):
```
git merge experimento
```
(rodado estando na branch que vai *receber* as mudanças).

O Git tenta resolver o merge de duas formas, dependendo da situação:

- **Fast-forward**: se a branch que recebe (`main`) não teve nenhum commit novo desde que
  `experimento` foi criada, o Git só "empurra o ponteiro da main pra frente" até o último commit
  de `experimento` — não precisa criar nenhum commit novo de merge, porque não havia nada pra
  combinar.
- **3-way merge**: se as duas branches divergiram (cada uma tem commits que a outra não tem), o
  Git precisa de fato combinar as duas histórias, e cria um **commit de merge** novo, com dois
  "pais" — essa é a situação que você já viu no `git log --graph` do tópico 1, com o `*` e o `|\`.

`[TENTE VOCÊ]` Você criou a branch `experimento`, fez um commit nela, e nunca mais tocou na
`main` desde então. Ao mesclar de volta, o Git vai criar um commit de merge novo? Resposta: não —
como a `main` não teve nenhum commit novo nesse meio tempo, o merge é fast-forward, só avança o
ponteiro.

`[REFERÊNCIA]` [git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge) — a doc oficial
detalha as estratégias de merge disponíveis (`ort`, `recursive`, etc.), mas pra uso do dia a dia
o essencial é a distinção fast-forward x 3-way descrita acima.

## 7. Conflitos

Um conflito de merge acontece quando a **mesma linha** de um arquivo foi alterada de formas
diferentes em duas branches que você está tentando juntar — o Git não tem como adivinhar qual das
duas versões é a "certa", então ele para e pede pra você decidir. É a mesma situação de duas
pessoas editando o mesmo parágrafo de um documento ao mesmo tempo, cada uma à sua maneira:
alguém precisa olhar as duas versões e decidir a final.

Quando isso acontece, o Git marca o trecho conflitante diretamente no arquivo:
```
<<<<<<< HEAD
sua versão da linha
=======
versão da outra branch
>>>>>>> experimento
```
Você edita o arquivo manualmente, decidindo o que fica (pode ser uma das duas versões, as duas
combinadas, ou algo novo), **remove os marcadores** (`<<<<<<<`, `=======`, `>>>>>>>`), e finaliza
o merge normalmente:
```
git add arquivo-resolvido.txt
git commit
```

`[ATENÇÃO]` Esquecer de remover os marcadores de conflito antes de commitar é um erro clássico —
o arquivo fica com esse "lixo" do Git salvo dentro dele, e ninguém percebe até rodar o código (ou
ler o arquivo) e ver os `<<<<<<<` lá dentro.

`[TENTE VOCÊ]` Duas branches mudaram a mesma linha de um arquivo de formas diferentes, e você deu
merge. O Git resolveu sozinho ou parou pedindo sua decisão? Resposta: parou — sempre que a mesma
linha muda de forma diferente nas duas branches, o Git não decide por você.

`[REFERÊNCIA]` [git-scm.com/book/pt-br/v2/Branches-no-Git-Merge-Básico-e-Conflitos-de-Merge](https://git-scm.com/book/pt-br/v2/Branches-no-Git-Merge-Básico-e-Conflitos-de-Merge) —
capítulo do Pro Git Book dedicado inteiramente a conflitos.

---

# Nível Intermediário

## 8. Rebase

`git merge` (tópico 6) preserva a história exatamente como ela aconteceu — inclusive o commit de
merge com dois pais, quando houve divergência. `git rebase` faz algo diferente: **reescreve** a
história, pegando os commits de uma branch e "replantando-os" em cima de outro ponto, como se
tivessem sido feitos a partir dali desde o início.

**Exemplo narrado:** você criou `feature/1234` a partir da `main`, fez 2 commits nela. Enquanto
isso, a `main` recebeu 3 commits novos de outras pessoas. Com `git merge`, o resultado final teria
um commit de merge combinando as duas histórias divergentes. Com `git rebase main` (rodado dentro
de `feature/1234`), o Git "desmonta" temporariamente os seus 2 commits, atualiza sua branch até o
ponto mais recente da `main`, e "replanta" os 2 commits um por um em cima disso — o resultado
final parece que você começou a trabalhar *depois* dos 3 commits novos da `main`, não antes.
```
git switch feature/1234
git rebase main
```

`[ATENÇÃO]` Nunca faça rebase de uma branch que **outras pessoas já baixaram/puxaram**. Como
rebase reescreve os commits (troca os hashes deles), qualquer pessoa que já tinha a versão antiga
dessa branch vai ter um histórico divergente e conflitante com o que você reescreveu — a mesma
lógica de perigo do `git reset --hard` num commit já compartilhado (tópico 9). Regra prática:
rebase é seguro em branches que só existem na sua máquina, ou que você tem certeza que mais
ninguém puxou ainda.

`[TENTE VOCÊ]` Você está numa branch só sua, ainda não compartilhada, e quer trazer as
atualizações mais recentes da `main` mantendo um histórico linear (sem commit de merge). Usa
`merge` ou `rebase`? Resposta: `rebase` — é seguro porque a branch é só sua, e o resultado é um
histórico limpo, sem o commit de merge extra.

`[REFERÊNCIA]` [git-scm.com/docs/git-rebase](https://git-scm.com/docs/git-rebase),
[git-scm.com/book/pt-br/v2/Ramificações-no-Git-Rebase](https://git-scm.com/book/pt-br/v2/Ramificações-no-Git-Rebase).

## 9. Reset / Restore / Revert

Lá na abertura deste módulo, a comparação foi com `Ctrl+Z` — um "desfazer" permanente e
compartilhável. Git tem três comandos que resolvem três problemas diferentes de "desfazer":

- **`git restore`** — desfaz mudanças **não commitadas ainda**, em arquivos individuais. É o
  "Ctrl+Z" mais literal: descarta o que você mudou num arquivo desde o último commit (ou desde o
  último `add`), sem mexer no histórico de commits.
  ```
  git restore arquivo.txt          # descarta mudanças não staged em arquivo.txt
  git restore --staged arquivo.txt # tira arquivo.txt da staging area, sem descartar a mudança
  ```
- **`git reset`** move o histórico da branch pra trás, como se os commits mais recentes nunca
  tivessem existido — ele **reescreve** o histórico local.
  ```
  git reset --soft HEAD~1   # desfaz o último commit, mas mantém as mudanças "staged"
  git reset --hard HEAD~1   # desfaz o último commit E descarta as mudanças de vez
  ```
- **`git revert`** não apaga nada do histórico — ele cria um **novo commit** que aplica o efeito
  contrário do commit escolhido, cancelando a mudança sem reescrever nada que já existia.
  ```
  git revert a3f9c21
  ```

`[ATENÇÃO]` `git reset --hard` num commit que **já foi enviado** pra um remoto compartilhado
(`git push`) é perigoso: reescreve um histórico que outras pessoas já baixaram, e a próxima vez
que elas sincronizarem vai gerar confusão ou conflito. O que fazer no lugar: em branches
compartilhadas, prefira `git revert` — ele desfaz o efeito sem apagar o que já aconteceu, então
todo mundo consegue sincronizar normalmente. Reserve `git reset` para commits que **ainda estão
só na sua máquina**, nunca enviados.

`[TENTE VOCÊ]` Você já deu `git push` de um commit com um bug, e outras duas pessoas do time já
baixaram esse commit. Você usaria `git reset` ou `git revert` pra corrigir? Resposta: `git
revert` — como o commit já foi compartilhado, reescrever o histórico com `reset` bagunçaria o
repositório de quem já baixou; `revert` desfaz o efeito com um commit novo, sem esse problema.

`[REFERÊNCIA]` [git-scm.com/docs/git-restore](https://git-scm.com/docs/git-restore),
[git-scm.com/docs/git-reset](https://git-scm.com/docs/git-reset),
[git-scm.com/docs/git-revert](https://git-scm.com/docs/git-revert).

## 10. Stash

Cenário comum: você está no meio de uma mudança em `experimento`, ainda não pronta pra virar
commit, e precisa trocar rapidamente para `main` (ex: pra corrigir algo urgente). O Git não deixa
trocar de branch com mudanças conflitantes soltas no meio do caminho — e você não quer forçar um
commit incompleto só pra "guardar o lugar". `git stash` resolve isso: guarda suas mudanças não
commitadas num "bolso" separado, deixando a pasta de trabalho limpa de novo.

```
git stash          # guarda as mudanças atuais, limpa a pasta de trabalho
git stash list     # lista o que está guardado
git stash pop      # traz de volta o último stash guardado, removendo-o da lista
```

`[TENTE VOCÊ]` Você guardou uma mudança com `git stash`, trocou de branch, resolveu o que
precisava, e voltou pra branch original. Como recupera a mudança guardada? Resposta:
`git stash pop`.

`[REFERÊNCIA]` [git-scm.com/docs/git-stash](https://git-scm.com/docs/git-stash).

## 11. Histórico / Reflog

`git log` (visto no tópico 1) é como você **lê** o histórico de commits depois. Sem ele, o
trabalho de dias vira uma caixa preta: você sabe que existe um histórico, mas não consegue
enxergá-lo. Rodando `git log` num repositório com alguns commits, a saída é parecida com esta
(exemplo fabricado, mas no formato real):

```
commit e91a4c73f8b2d0e1a9c4567890abcdef1234567 (HEAD -> main)
Merge: 4f1d9a2 a3f9c21
Author: Ana Souza <ana.souza@email.com>
Date:   Tue Aug 12 14:35:10 2026 -0300

    Merge branch 'feature/1234-cadastro-usuario'

commit a3f9c21e8b4d5f67890123456789abcdef01234
Author: Ana Souza <ana.souza@email.com>
Date:   Tue Aug 12 14:32:07 2026 -0300

    feat: adicionar validação de e-mail no cadastro

commit 7c2e814f3a9b0d1e2f3456789abcdef012345678
Author: Ana Souza <ana.souza@email.com>
Date:   Mon Aug 11 09:15:43 2026 -0300

    fix: corrigir mensagem de erro ao login

commit 4f1d9a2c6e8b7f0123456789abcdef0123456789
Author: Ana Souza <ana.souza@email.com>
Date:   Mon Aug 11 08:50:21 2026 -0300

    docs: adicionar instruções de instalação no README
```

Lendo de cima para baixo (do mais recente para o mais antigo): o topo é o merge que trouxe a
branch `feature/1234-cadastro-usuario` de volta para a `main` (repare o prefixo `feature/1234-...`
— é exatamente o padrão de nome de branch do Módulo 02); embaixo dele, os dois commits que essa
branch trouxe (`feat` e `fix`, com o hash e o autor de cada um); e na base, um commit anterior já
existente na `main` (`docs`).

Duas variações do mesmo comando, pra situações diferentes:

```
git log --oneline
```
```
e91a4c7 Merge branch 'feature/1234-cadastro-usuario'
a3f9c21 feat: adicionar validação de e-mail no cadastro
7c2e814 fix: corrigir mensagem de erro ao login
4f1d9a2 docs: adicionar instruções de instalação no README
```
A mesma história, comprimida numa linha por commit (hash curto + mensagem) — útil quando você só
quer escanear rapidamente o que aconteceu, sem ler autor/data de cada um.

```
git log --graph --oneline
```
```
*   e91a4c7 Merge branch 'feature/1234-cadastro-usuario'
|\
| * a3f9c21 feat: adicionar validação de e-mail no cadastro
| * 7c2e814 fix: corrigir mensagem de erro ao login
|/
* 4f1d9a2 docs: adicionar instruções de instalação no README
```
Aqui a estrutura fica visual: as duas linhas com `|` mostram os dois commits que viveram numa
branch separada antes de voltar pra `main` no merge (`*` com `|\`). É a mesma informação do
primeiro `git log`, só que desenhada — ajuda muito quando o histórico tem várias branches indo e
voltando.

`[TENTE VOCÊ]` Olhando o `git log --graph --oneline` acima, quantos commits foram feitos *dentro*
da branch `feature/1234-cadastro-usuario`, antes dela ser mesclada de volta? Resposta: 2
(`a3f9c21` e `7c2e814`) — são os dois que aparecem na linha desviada (`|`) antes de ela voltar a
se juntar com a `main`.

`[CLI]` Quer ver só o conteúdo exato que um commit específico mudou (não só a mensagem)?
```
git show a3f9c21
```
Mostra a mensagem do commit *e* o diff (as linhas exatas que mudaram) daquele commit específico —
como abrir uma "foto" isolada do histórico, sem precisar navegar pelo projeto inteiro.

### `git reflog` — a rede de segurança final

`git log` mostra o histórico de **commits alcançáveis** a partir de onde você está agora. Mas e se
você deu um `git reset --hard` errado e "perdeu" um commit? Ele não desapareceu de verdade — só
saiu do alcance do `git log`. `git reflog` mostra um histórico *diferente*: tudo que o `HEAD` (o
"você está aqui" do Git) já apontou, incluindo commits que `git log` não mostra mais.

```
git reflog
```
```
a3f9c21 (HEAD -> main) HEAD@{0}: commit: feat: adicionar validação de e-mail
7c2e814 HEAD@{1}: reset: moving to HEAD~1
4f1d9a2 HEAD@{2}: commit: docs: adicionar instruções de instalação
```
Cada linha é um momento em que o `HEAD` mudou de lugar. Se você "perdeu" o commit `7c2e814` com
um `reset --hard` por engano, o reflog ainda mostra o hash dele — e você pode voltar com
`git reset --hard 7c2e814` (ou `git cherry-pick 7c2e814`, tópico 16).

`[ATENÇÃO]` O reflog é **local** — não é enviado ao remoto, e tem um prazo de expiração padrão
(90 dias pra entradas alcançáveis, 30 para as não alcançáveis). Não é uma cópia de segurança
permanente, mas resolve o pânico de "apaguei um commit sem querer" na grande maioria dos casos.

`[TENTE VOCÊ]` Você rodou `git reset --hard HEAD~1` por engano, apagando um commit que ainda não
tinha sido enviado a lugar nenhum. Como recupera o hash desse commit "perdido"? Resposta:
`git reflog` — ele mostra o hash do commit mesmo depois que `git log` parou de listá-lo.

`[REFERÊNCIA]` [git-scm.com/docs/git-log](https://git-scm.com/docs/git-log),
[git-scm.com/docs/git-show](https://git-scm.com/docs/git-show),
[git-scm.com/docs/git-reflog](https://git-scm.com/docs/git-reflog).

## 12. Tags

Uma tag é como um marcador de página num livro — só que, em vez de apontar pra uma posição
aproximada, ela aponta pra um commit exato, de forma permanente, e com um nome legível
(`v1.4.0`) em vez do hash comprido do commit. Diferente de uma branch, uma tag **não se move**:
depois de criada, ela sempre aponta pro mesmo commit, para sempre.

```
git tag -a v1.4.0 -m "Lançamento da versão 1.4.0"   # cria uma tag anotada
git push origin v1.4.0                              # envia essa tag ao remoto
git push origin --tags                               # envia todas as tags locais de uma vez
```

O `-a` importa: cria uma tag **anotada**, que guarda autor, data e mensagem — um objeto completo
no histórico do Git, igual um commit. Sem o `-a`, o Git cria uma tag **leve** (*lightweight*), que
é só um apelido apontando pro commit, sem esse metadado. Para marcar lançamentos de versão, a
anotada é a prática recomendada.

`[TENTE VOCÊ]` Depois de rodar `git tag -a v2.0.0 -m "..."` localmente, o comando sozinho já foi
suficiente pra essa tag aparecer no GitHub? Resposta: não — tags, assim como commits, precisam de
um `git push` explícito (`git push origin v2.0.0` ou `git push origin --tags`) pra chegar ao
remoto.

**Exemplo de repositório real:** o repositório do [React](https://github.com/facebook/react/tags)
usa tags seguindo exatamente o padrão de Versionamento Semântico (`v18.2.0`, `v18.3.1`, etc.) já
visto no Módulo 02 — cada tag marca um lançamento oficial, e é a partir delas que o gerenciador de
pacotes npm sabe qual versão instalar.

`[REFERÊNCIA]` [git-scm.com/docs/git-tag](https://git-scm.com/docs/git-tag),
[git-scm.com/book/pt-br/v2/Fundamentos-do-Git-Marcando](https://git-scm.com/book/pt-br/v2/Fundamentos-do-Git-Marcando).
O detalhamento de quando incrementar `MAJOR.MINOR.PATCH` está no
[Módulo 02](02_padroes-projeto-teoria.md).

## 13. Conventional Commits

Aqui é o lado **mecânico** do formato — o Módulo 02 já cobre a convenção completa da equipe
(prefixos permitidos, exemplos, regras específicas do time). O que importa entender neste módulo
é *por que* esse formato existe do ponto de vista técnico: `PREFIXO: descrição` (ex:
`feat: adicionar login`) é um formato **estruturado o suficiente para ferramentas conseguirem
interpretar programaticamente** — um script consegue abrir o histórico de commits, separar por
prefixo, e gerar automaticamente um changelog ou decidir a próxima versão semântica, sem
intervenção humana. Uma mensagem livre como "mexi no login" não permite esse tipo de automação.

`[REFERÊNCIA]` A especificação formal (não é exclusiva do Git — é uma convenção adotada pela
comunidade, documentada em [conventionalcommits.org](https://www.conventionalcommits.org/pt-br/)).
Aprofundamento das convenções específicas desta trilha (quais prefixos usar, quando) está no
[Módulo 02](02_padroes-projeto-teoria.md).

## 14. Pull Request / Code Review

Um detalhe que surpreende quem está começando: **Pull Request não é um comando do Git** — é uma
funcionalidade de plataformas como GitHub, GitLab ou Bitbucket, construída *em cima* do Git puro.
Tecnicamente, um Pull Request é uma **comparação entre duas branches** (ex: `feature/1234` contra
`main`), exibida numa interface visual, onde outras pessoas podem comentar linha por linha, pedir
mudanças, aprovar, e só então mesclar (merge) através da própria interface — em vez de alguém dar
`git merge` na mão pelo terminal.

O fluxo técnico por trás de um PR, resumido:
1. Você cria uma branch (`git switch -c feature/1234-...`) e faz commits nela.
2. Você envia essa branch ao remoto (`git push -u origin feature/1234-...`).
3. Na interface do GitHub, você abre um Pull Request comparando `feature/1234-...` contra `main`.
4. Revisores comentam, você ajusta e faz novos commits (mais `git push` na mesma branch — o PR se
   atualiza sozinho, porque ele só está observando essa branch remota).
5. Quando aprovado, alguém clica em "Merge" — que, por baixo, executa um `git merge` (ou
   `git rebase`, dependendo da estratégia configurada) no servidor.

`[TENTE VOCÊ]` Depois de abrir um Pull Request, você percebe que esqueceu de tratar um caso e
precisa corrigir. O que você faz: fecha o PR e abre outro, ou só continua commitando na mesma
branch? Resposta: continua commitando na mesma branch local e dá `git push` de novo — o PR já
aberto se atualiza automaticamente, porque ele acompanha a branch, não uma "foto" fixa dela.

`[REFERÊNCIA]` [docs.github.com/pt/pull-requests](https://docs.github.com/pt/pull-requests) —
documentação oficial do GitHub sobre Pull Requests. O modelo de descrição/título específico desta
trilha está no [Módulo 02](02_padroes-projeto-teoria.md).

---

# Nível Avançado

## 15. Git Flow / Trunk Based

Esses são dois **modelos** (convenções de equipe, não comandos do Git) de como organizar branches
num projeto ao longo do tempo — cada um resolve um problema diferente.

- **Git Flow**: usa branches de vida longa (`develop`, `release/*`, `hotfix/*`, além das
  `feature/*` de curta duração), com um processo formal de preparar uma versão antes de ela ir
  pra produção. Resolve bem cenários com ciclos de lançamento espaçados e bem definidos (ex:
  software que é "lançado" em versões, não continuamente).
- **Trunk Based Development**: uma única branch principal de longa duração (o "tronco" —
  geralmente `main`), com integrações **frequentes** (várias vezes por dia) e branches de
  feature muito curtas (horas, não semanas). Funcionalidades incompletas ficam escondidas atrás
  de *feature flags* em vez de isoladas numa branch por semanas. Resolve bem cenários de entrega
  contínua, onde o objetivo é sempre poder lançar o que está na `main`.

`[TENTE VOCÊ]` Um time faz deploy pra produção várias vezes por dia, direto da `main`. Esse time
provavelmente segue Git Flow ou Trunk Based? Resposta: Trunk Based — a cadência de deploy
contínuo não combina com o processo de preparação formal de versão do Git Flow, que assume ciclos
de lançamento mais espaçados.

`[REFERÊNCIA]` O post original que formalizou o Git Flow:
[nvie.com/posts/a-successful-git-branching-model](https://nvie.com/posts/a-successful-git-branching-model/).
Sobre Trunk Based: [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/).

## 16. Cherry-pick

`git cherry-pick` copia um **commit específico** de uma branch para outra, sem trazer o resto do
histórico dessa branch — como pegar só uma página de um livro e colar em outro, em vez de copiar
o livro inteiro.

**Cenário clássico:** você corrigiu um bug crítico numa branch de feature ainda em andamento
(`feature/1234`), mas esse mesmo bug também afeta a versão já em produção (`main`). Em vez de
mesclar a `feature/1234` inteira (que ainda não está pronta) na `main`, você "pinça" só o commit
da correção:

```
git switch main
git cherry-pick a3f9c21
```
Isso cria, na `main`, um novo commit com o mesmo conteúdo (mesmo diff) do commit `a3f9c21` — mas
com um hash diferente, porque tecnicamente é um commit novo, aplicado num contexto diferente.

`[ATENÇÃO]` Como o cherry-pick cria um commit novo (hash diferente do original), se depois você
mesclar a branch de origem inteira, o Git pode não perceber que aquele commit já foi aplicado —
resultando numa mudança duplicada ou num conflito desnecessário. Fique atento quando as duas
branches (a de origem do cherry-pick e a que recebeu) forem mescladas depois.

**Exemplo de repositório real:** o projeto Kubernetes documenta formalmente seu processo de
cherry-pick para levar correções de bugs da branch principal de volta pra branches de versões já
lançadas — vale ler como um time grande, real, formaliza esse processo:
[github.com/kubernetes/community — cherry-picks.md](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-release/cherry-picks.md).

`[TENTE VOCÊ]` Você tem um commit de correção numa branch de feature ainda incompleta, e precisa
dessa correção específica também na `main`, sem esperar a feature inteira ficar pronta. Qual
comando usa? Resposta: `git cherry-pick <hash-do-commit>`, estando na `main`.

`[REFERÊNCIA]` [git-scm.com/docs/git-cherry-pick](https://git-scm.com/docs/git-cherry-pick).

## 17. Bisect

`git bisect` aplica busca binária ao histórico de commits, pra achar **qual commit específico**
introduziu um bug — em vez de revisar um por um, linearmente, entre centenas de commits.

**Exemplo narrado — sessão completa:** você sabe que a versão atual (`HEAD`) tem um bug, e que a
tag `v1.0.0`, lá atrás, não tinha esse bug. Existem 100 commits entre as duas.

```
git bisect start
git bisect bad                # o commit atual (HEAD) tem o bug
git bisect good v1.0.0         # esse commit lá atrás não tinha o bug
```
O Git automaticamente faz checkout de um commit **no meio** desses 100. Você testa o projeto
nesse ponto e informa o resultado:
```
git bisect good    # se esse meio não tinha o bug
# ou
git bisect bad     # se esse meio já tinha o bug
```
O Git repete o processo, sempre dividindo ao meio o intervalo restante — em vez de até 100 testes,
você precisa de no máximo `log₂(100) ≈ 7` testes (a mesma matemática de "quantos bits pra
representar N valores", vista no Módulo 03, aplicada aqui a commits em vez de bits). Quando só
sobra um commit candidato, o Git aponta exatamente qual foi o culpado. Ao final:
```
git bisect reset   # volta pro estado original (HEAD), encerrando a sessão
```

`[ATENÇÃO]` Não esqueça o `git bisect reset` no final — enquanto a sessão de bisect está aberta,
você está com o repositório "no meio do caminho", em checkout de um commit antigo qualquer, não
na sua branch de trabalho normal.

`[TENTE VOCÊ]` Entre o commit bom e o commit ruim existem 32 commits. Aproximadamente quantos
testes o `git bisect` precisa pra encontrar o culpado? Resposta: cerca de 5 (`log₂(32) = 5`) —
bem menos que testar os 32 um por um.

`[REFERÊNCIA]` [git-scm.com/docs/git-bisect](https://git-scm.com/docs/git-bisect).

## 18. Worktree

Cenário: você está no meio de um trabalho numa branch, com mudanças ainda não commitadas, e
precisa urgentemente olhar/testar outra branch — sem perder o que está fazendo. As opções vistas
até aqui seriam `git stash` (guardar e depois recuperar) ou clonar o repositório de novo numa
pasta separada (gasta espaço em disco duplicado, e você teria que reconfigurar tudo).
`git worktree` resolve isso de um jeito melhor: permite ter **duas branches diferentes,
"abertas" em duas pastas diferentes, ao mesmo tempo**, tudo dentro do mesmo repositório Git (um
único histórico, sem duplicar o `.git`).

```
git worktree add ../projeto-hotfix hotfix/9101-erro-critico
```
Isso cria uma pasta nova (`../projeto-hotfix`), com a branch `hotfix/9101-erro-critico` já em
checkout ali — enquanto sua pasta original continua exatamente como estava, na branch que você já
estava trabalhando. Você pode abrir as duas pastas em janelas de editor separadas, testar as duas
ao mesmo tempo, sem stash nenhum.

Pra remover depois de terminar:
```
git worktree remove ../projeto-hotfix
```

`[TENTE VOCÊ]` Você está no meio de uma feature grande, com várias mudanças não commitadas, e
precisa testar rapidamente uma outra branch em paralelo, sem mexer no que já está em andamento.
`stash` ou `worktree` resolve isso sem exigir que você pare o que está fazendo? Resposta:
`worktree` — ele cria uma pasta separada com a outra branch, sem precisar guardar/tirar do stash
o trabalho atual.

`[REFERÊNCIA]` [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree).

## 19. Hooks

Hooks são scripts que o Git executa **automaticamente** em certos momentos do fluxo de trabalho
(antes de um commit, depois de um commit, antes de um push, etc.) — ficam na pasta
`.git/hooks/` de qualquer repositório, mas por padrão essa pasta não é versionada (é local,
específica de cada cópia do repositório).

**Exemplo — hook `pre-commit`:** um script que roda automaticamente toda vez que você tenta
commitar, e pode **cancelar** o commit se algo estiver errado. Um exemplo simples (arquivo
`.git/hooks/pre-commit`, precisa ter permissão de execução):
```bash
#!/bin/sh
if git diff --cached | grep -q "console.log"; then
  echo "Commit bloqueado: existe um console.log esquecido no código."
  exit 1
fi
```
Se esse script terminar com um código de saída diferente de zero (`exit 1`), o Git cancela o
commit — a pessoa precisa remover o `console.log` antes de conseguir commitar.

`[ATENÇÃO]` Como `.git/hooks/` não é versionado por padrão, hooks escritos manualmente assim só
existem na sua máquina — outra pessoa que clona o repositório não ganha esse hook automaticamente.
Na prática, times usam ferramentas que resolvem esse problema.

**Exemplo de repositório real:** [Husky](https://github.com/typicode/husky) é a ferramenta mais
usada no ecossistema JavaScript/Node para gerenciar hooks de forma versionada e compartilhada
entre todo o time — o próprio repositório do Husky no GitHub documenta exatamente esse problema
(hooks locais não versionados) e como ele resolve.

`[TENTE VOCÊ]` Por que um hook `pre-commit` escrito manualmente na sua máquina não "viaja" junto
quando você faz `git push`? Resposta: porque `.git/hooks/` não faz parte do histórico versionado
do repositório — é uma pasta de configuração local, específica de cada cópia.

`[REFERÊNCIA]` [git-scm.com/docs/githooks](https://git-scm.com/docs/githooks).

## 20. Git + CI/CD

O Módulo 02 já conectou Git a versionamento semântico — este tópico fecha o círculo mostrando
como um evento do Git (um `push`, a criação de uma `tag`) pode **disparar automaticamente** um
pipeline de build, teste e/ou publicação, sem intervenção manual. Isso é CI/CD (Integração
Contínua / Entrega Contínua): CI roda testes/verificações a cada mudança; CD publica
automaticamente quando os critérios são atendidos.

**Exemplo real, desta própria trilha:** o site que você está lendo agora é publicado
automaticamente sempre que um `git push` acontece na branch `main` deste repositório, através de
um workflow do GitHub Actions. O arquivo que configura isso é literalmente público e navegável:
[`.github/workflows/deploy.yml`](https://github.com/L1malucas/trilha-jovem-aprendiz/blob/main/.github/workflows/deploy.yml).
Ele diz, essencialmente: "sempre que houver um push em `main`, instale as dependências, gere os
arquivos estáticos do site, e publique no GitHub Pages" — tudo isso disparado só pelo `git push`,
sem ninguém precisar rodar esses passos manualmente.

`[TENTE VOCÊ]` Se um workflow de CI/CD está configurado pra rodar "a cada push em `main`", e você
só está trabalhando numa branch `feature/1234` sem nunca mesclar na `main`, o workflow roda?
Resposta: não — ele só dispara no evento configurado (push em `main`); trabalhar numa outra
branch não aciona o gatilho até essa branch ser mesclada.

`[REFERÊNCIA]` [docs.github.com/pt/actions](https://docs.github.com/pt/actions) — documentação
oficial do GitHub Actions, a ferramenta de CI/CD usada nesta trilha.

---

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Esquecer o `git add` antes do `git commit`.
- Commitar um arquivo que já deveria estar no `.gitignore` antes de existir.
- Deixar marcadores de conflito (`<<<<<<<`, `=======`, `>>>>>>>`) no arquivo depois de resolver.
- Confundir `pull` (traz e já mescla) com `fetch` (só traz a informação).
- Usar `git reset --hard` num commit que já foi enviado a um remoto compartilhado.
- Usar `git push --force` puro numa branch compartilhada, em vez de `--force-with-lease` (ou,
  melhor ainda, resolver com `pull` antes).
- Fazer `git rebase` de uma branch que outras pessoas já puxaram.
- Esquecer o `git bisect reset` ao final de uma sessão de bisect.
- Escrever hooks manuais em `.git/hooks/` esperando que outra pessoa também tenha eles — sem uma
  ferramenta como Husky, hooks locais não são compartilhados automaticamente.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Nomes de branch, prefixos de commit, SemVer, PR | Módulo 02 — Padrões de Projeto formaliza as convenções específicas da equipe |
| `git log` e histórico de commits | Módulo 02 — mensagens de commit padronizadas aparecem exatamente nesse formato |
| `log₂(N)` aplicado a commits (bisect) | Módulo 03 — a mesma matemática, aplicada a bits |
| Commits, branches, PRs e histórico | Todo módulo cuja entrega é feita via GitHub |
| CI/CD disparado por push | O próprio deploy desta trilha, e qualquer projeto com pipeline automatizado |

## `[REFERÊNCIA]`

- [Pro Git Book (pt-BR)](https://git-scm.com/book/pt-br/v2) — livro oficial e gratuito do Git,
  base de praticamente todo este módulo.
- [Documentação oficial do Git](https://git-scm.com/doc) — referência de todos os comandos
  citados.
- [Learn Git Branching](https://learngitbranching.js.org/?locale=pt_BR) — ferramenta interativa
  usada na prática deste módulo.
- Exemplos de repositórios reais citados ao longo do módulo:
  [React (tags de release)](https://github.com/facebook/react/tags),
  [Kubernetes (processo de cherry-pick)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-release/cherry-picks.md),
  [Husky (hooks compartilhados)](https://github.com/typicode/husky),
  [o workflow de deploy desta própria trilha](https://github.com/L1malucas/trilha-jovem-aprendiz/blob/main/.github/workflows/deploy.yml).

## Checklist de saída

**Básico**
- [ ] Crio um repositório e faço commits, sabendo explicar por que `add` e `commit` são passos
      separados.
- [ ] Configuro um `.gitignore` e sei corrigir um arquivo que foi commitado por engano antes dele
      existir.
- [ ] Uso `git diff` e `git diff --staged` pra conferir mudanças antes de commitar.
- [ ] Crio e mesclo branches, sabendo explicar por que o commit de uma branch não aparece nas
      outras até o merge.
- [ ] Configuro um remoto do zero com `git remote add`/`-u`, e sei resolver um push rejeitado sem
      usar `--force` puro.
- [ ] Explico a diferença entre `pull` e `fetch`, e entre merge fast-forward e 3-way.
- [ ] Resolvo um conflito de merge manualmente, removendo os marcadores corretamente.

**Intermediário**
- [ ] Sei quando usar `rebase` (histórico só local) em vez de `merge`, e por que nunca fazer
      rebase de uma branch já compartilhada.
- [ ] Sei quando usar `git restore`, `git reset` (histórico só local) e `git revert` (histórico já
      compartilhado).
- [ ] Uso `git stash` pra trocar de branch sem perder uma mudança em andamento.
- [ ] Leio a saída de `git log`, `git log --graph` e uso `git reflog` pra recuperar um commit
      "perdido".
- [ ] Crio e envio uma tag anotada, explicando a diferença entre tag anotada e leve.
- [ ] Explico por que Conventional Commits é um formato pensado pra automação, não só estilo.
- [ ] Explico o que um Pull Request é tecnicamente (comparação entre branches numa plataforma),
      não um comando nativo do Git.

**Avançado**
- [ ] Explico a diferença entre Git Flow e Trunk Based, e qual problema cada um resolve.
- [ ] Uso `git cherry-pick` pra levar um commit específico de uma branch pra outra.
- [ ] Conduzo uma sessão completa de `git bisect` até encontrar o commit culpado.
- [ ] Uso `git worktree` pra trabalhar em duas branches ao mesmo tempo, em pastas separadas.
- [ ] Escrevo um hook `pre-commit` simples e explico por que ele não é compartilhado
      automaticamente sem uma ferramenta como Husky.
- [ ] Explico como um `git push` pode disparar um pipeline de CI/CD automaticamente, citando o
      exemplo real desta trilha.
