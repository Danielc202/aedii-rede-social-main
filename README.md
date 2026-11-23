# Atividade Final — Algoritmos e Estruturas de Dados II

## Rede Social Simplificada

Você vai construir o núcleo de uma rede social: cadastro de usuários, quem segue quem e postagens. A rede tem **2.000 usuários**, **15.000 conexões** e **20.000 posts**. Com esse volume, escolher a estrutura de dados certa faz diferença: uma solução O(n²) fica visivelmente lenta.

O trabalho usa **todos os conteúdos da disciplina**: tabela hash, árvore AVL, heap, ordenação e grafos.

> **Prazo:** 08/12 · **Entrega:** virtual, pelo Blackboard (sem apresentação presencial) · **Formato:** individual ou em dupla

---

## 1. Como começar

```bash
git clone <url-deste-repositorio>
cd <pasta-do-repositorio>
```

Escolha **uma** linguagem e trabalhe apenas na pasta dela:

| Linguagem  | Pasta | Como rodar           |
|------------|-------|----------------------|
| Python 3   | `py/` | `python3 py/main.py` |
| JavaScript | `js/` | `node js/main.js`    |

O `main` só lê os três arquivos de dados e mostra quantos registros carregou. **Todo o resto é com você.** Crie quantos arquivos quiser dentro da pasta escolhida e organize o código do jeito que achar melhor.

---

## 2. Os dados

Os três arquivos ficam na raiz do repositório. Eles usam `;` como separador e têm cabeçalho na primeira linha. **Não altere os arquivos de dados.**

**`usuarios.csv`**
```
id;usuario;nome;data_cadastro
1;@henrique_nascimento;Henrique Nascimento;2022-10-26
```
`usuario` é único e sempre começa com `@`.

**`seguidores.csv`**: cada linha é uma conexão dirigida, em que `seguidor` segue `seguido` (pelo `id`).
```
seguidor;seguido
440;243
```

**`posts.csv`**
```
id;autor;data;curtidas;texto
1;1844;2025-09-01;1;Incrível treino treino almoço bug algoritmo
```
`autor` é o `id` do usuário, e `data` está no formato `AAAA-MM-DD`.

---

## 3. O que deve ser implementado

O programa recebe comandos no terminal e responde a cada um. O formato abaixo é uma **sugestão**: você pode usar um menu numerado, por exemplo, desde que todas as funcionalidades existam.

### 3.1 `BUSCAR @usuario`: tabela hash
Mostra os dados do usuário: nome, data de cadastro, quantos segue, quantos seguidores tem e quantos posts publicou.
- A busca por `@usuario` deve ser feita em uma **tabela hash implementada por você**, com função de hash própria e tratamento de colisões (encadeamento ou endereçamento aberto, à sua escolha).
- Se o usuário não existir, informe isso claramente.

### 3.2 `SUGERIR @usuario k`: grafo + heap
Sugere até `k` pessoas para o usuário seguir, no estilo "amigos de amigos".
- **Candidatos:** quem é seguido por alguém que o usuário segue, ou seja, quem está a distância 2 no grafo. Ficam de fora o próprio usuário e quem ele já segue.
- **Ordem:** pelo número de conexões em comum, isto é, quantas pessoas que o usuário segue também seguem o candidato, do maior para o menor.
- O grafo deve ser representado por você (lista de adjacência é o recomendado), e a seleção dos `k` melhores deve usar uma **heap implementada por você**.

### 3.3 `COMUNIDADES`: grafo
Encontra as comunidades da rede, tratando "seguir" como uma ligação **não dirigida** entre os dois usuários. Cada comunidade é um **componente conexo**.
- Mostre quantas comunidades existem e o tamanho de cada uma, da maior para a menor.
- Mostre também quantos usuários estão totalmente isolados.
- Use BFS ou DFS implementada por você.

### 3.4 `POSTS_ENTRE data1 data2`: árvore AVL
Lista os posts publicados entre `data1` e `data2`, com as duas datas incluídas, em ordem cronológica.
- Os posts devem estar indexados por data em uma **árvore AVL implementada por você**, com as rotações.
- A consulta por intervalo **não pode** percorrer a árvore inteira: ela deve descer apenas pelos ramos que podem conter datas do intervalo.
- Mostre também quantos posts foram encontrados.

### 3.5 `TOP_SEGUIDOS k` e `TOP_CURTIDOS k`: heap
- `TOP_SEGUIDOS k`: os `k` usuários com mais seguidores.
- `TOP_CURTIDOS k`: os `k` posts com mais curtidas, com autor, data e texto.
- Use a **sua heap**. Explique no relatório se usou heap de máximo ou de mínimo, e por quê.

### 3.6 `RANKING`: ordenação
Gera o ranking de **todos** os usuários por "engajamento", definido como:

```
engajamento = seguidores × 2 + soma das curtidas dos seus posts
```

- A ordem é do maior engajamento para o menor. Em caso de empate, vale a ordem alfabética do `@usuario`.
- Use um algoritmo **O(n log n) implementado por você**: Merge Sort, Quick Sort ou Heap Sort.
- Mostre os 20 primeiros colocados e a posição de um usuário informado, se quiser.

### 3.7 Bônus (opcional): API de consulta via linha de comando
**Depois** de concluir os itens 3.1 a 3.6, transforme o programa em uma **API de linha de comando**. Assim, qualquer consulta é feita em uma única chamada no terminal, sem menu interativo:

```bash
python3 py/main.py buscar @ana_silva
python3 py/main.py sugerir @ana_silva 5
python3 py/main.py comunidades
python3 py/main.py posts-entre 2025-03-01 2025-03-31
python3 py/main.py top-seguidos 10
python3 py/main.py top-curtidos 10
python3 py/main.py ranking --limite 20
python3 py/main.py sugerir @ana_silva 5 --json
python3 py/main.py ajuda
```

Em JavaScript, os mesmos comandos funcionam com `node js/main.js ...`.

Requisitos:
- **Todas** as funcionalidades de 3.1 a 3.6 ficam acessíveis por argumentos.
- **Ajuda:** `ajuda`, ou um comando inválido, lista os comandos, os parâmetros de cada um e um exemplo de uso.
- **Saída em JSON:** a opção `--json` troca a saída legível por **JSON válido**, para outro programa consumir o resultado. Exemplo: `python3 py/main.py top-seguidos 3 --json > saida.json`.
- **Erros:**
  - parâmetros faltando ou inválidos (data mal formatada, `k` não numérico, usuário inexistente) geram uma mensagem clara;
  - em caso de erro, o programa termina com **código de saída diferente de 0**: `sys.exit(1)` em Python, `process.exit(1)` em JS;
  - em caso de sucesso, o código de saída é 0.
- **Restrição:** a API só **usa** as estruturas que você implementou. As regras da seção 4 continuam valendo.
- **Ferramentas permitidas:** para ler os argumentos, você pode usar `sys.argv` ou `argparse` em Python, e `process.argv` em JS.
- **Relatório:** documente a API, com uma tabela de comandos e exemplos de chamada com a saída obtida, e explique como você organizou o código para separar as estruturas da interface.

---

## 4. Regras

**Não é permitido** usar as estruturas prontas da linguagem para resolver o problema:

| Python (proibido)                                                       | JavaScript (proibido)                                                        |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `dict`, `set`, `heapq`, `sorted()`, `list.sort()`, `bisect`, `collections` | `Map`, `Set`, `WeakMap`, objeto `{}` usado como dicionário, `Array.prototype.sort()` |

- **Pode usar:** listas e arrays simples (acesso por índice, `append`/`push`, `pop`), classes, tipos primitivos e strings.
- A leitura dos arquivos já está pronta no `main`, e você pode mantê-la como está.
- Não use bibliotecas externas: nada de `pip install` ou `npm install`.
- Os trabalhos são comparados entre si. Cópia entre grupos ou de fontes externas zera a nota de todos os envolvidos.

---

## 5. Documentação (obrigatória)

Entregue um arquivo `RELATORIO.md` (ou `RELATORIO.pdf`) na raiz do repositório. Ele deve explicar:

1. **O que foi feito:** quais funcionalidades foram implementadas e quais ficaram incompletas, se houver.
2. **Como foi feito:** como está organizado o código, quais arquivos existem e o que cada um faz.
3. **Escolhas tomadas e por quê.** Exemplos:
   - Qual função de hash você usou, como tratou colisões e qual tamanho de tabela escolheu.
   - Por que AVL, e não uma lista ordenada, para as datas.
   - Heap de máximo ou de mínimo no top-k.
   - Qual algoritmo de ordenação você escolheu e por quê.
   - Como o grafo foi representado.
4. **Complexidade:** a complexidade de tempo de cada comando (seções 3.1 a 3.6), com uma justificativa curta.
5. **Testes feitos manualmente:** quais comandos você executou, com quais entradas e quais saídas obteve. Inclua casos de borda, como usuário inexistente, `k` maior que o número de candidatos, intervalo de datas sem posts ou com datas invertidas, e usuário isolado. Prints ou trechos da saída do terminal são bem-vindos.

Na dupla, identifique os dois integrantes no início do relatório.

---

## 6. Entrega

- **Prazo:** 08/12, pelo Blackboard. Não há entrega presencial.
- **O que enviar:** o **link do seu repositório** (público ou com acesso liberado ao professor) **e** um `.zip` com o código e o relatório.
- **Dupla:** apenas um integrante envia, mas os dois nomes devem constar no relatório.

---

## 7. Critérios de avaliação

A avaliação é por **conceito (A, B, C ou D)** e considera:

- completude do código;
- clareza da explicação de métodos, funções e classes;
- documentação;
- entrega no prazo;
- bônus.

> **O conceito A exige o bônus (item 3.7).**

Os critérios completos e o que é exigido para cada conceito estão em **[AVALIACAO.md](AVALIACAO.md)**. Leia esse arquivo antes de começar.

Bom trabalho!
