# Aula 6 - Pilha e Fila Encadeadas

## 1. TAD e estrutura de dados

Um TAD (Tipo Abstrato de Dados) define o comportamento e as operações que podem ser realizadas sobre uma coleção de dados, sem determinar necessariamente como ela será implementada.

A estrutura de dados é a forma concreta utilizada para armazenar e organizar os elementos.

Nesta atividade, a `PilhaEncadeada` representa o TAD pilha, que segue o princípio LIFO (Last In, First Out): o último elemento inserido é o primeiro a ser removido.

Sua implementação utiliza uma lista simplesmente encadeada. Cada nó possui um valor e uma referência para o próximo nó. A pilha mantém uma referência para o nó do topo e um contador de elementos.

## 2. Pilha encadeada

A pilha foi implementada manualmente, sem utilizar `list`, `tuple`, `dict` ou `collections.deque` como estrutura de armazenamento.

As operações possuem os seguintes custos:

| Operação | Complexidade |
|---|---|
| `push(item)` | O(1) |
| `pop()` | O(1) |
| `topo()` | O(1) |
| `esta_vazia()` | O(1) |
| `len()` | O(1) |
| `repr()` | O(N) |

As operações `push`, `pop` e `topo` trabalham diretamente com o nó do topo, por isso não precisam percorrer a lista.

O método `len()` utiliza um contador mantido pela própria classe, evitando a necessidade de percorrer os nós para descobrir a quantidade de elementos.

O método `repr()` precisa percorrer os elementos da pilha para construir uma representação legível do topo até a base, portanto possui custo O(N).

Operações sobre uma pilha vazia, como `pop()` e `topo()`, geram `IndexError` com uma mensagem explicativa.

## 3. Fila encadeada por composição

A `FilaEncadeada` utiliza duas instâncias de `PilhaEncadeada`:

- pilha de entrada (`_entrada`);
- pilha de saída (`_saida`).

A fila utiliza composição, pois possui objetos `PilhaEncadeada` internamente em vez de herdar dessa classe.

A pilha de entrada recebe os novos elementos. Quando é necessário remover ou consultar o primeiro elemento e a pilha de saída está vazia, os elementos da pilha de entrada são transferidos para a pilha de saída.

Essa transferência inverte a ordem dos elementos e permite que o elemento mais antigo fique no topo da pilha de saída.

As operações possuem os seguintes custos:

| Operação | Complexidade |
|---|---|
| `enfileirar(item)` | O(1) |
| `desenfileirar()` | O(1) amortizado |
| `frente()` | O(1) amortizado |
| `esta_vazia()` | O(1) |
| `len()` | O(1) |
| `repr()` | O(N) |

A fila não acessa os atributos internos da `PilhaEncadeada`. Ela utiliza somente sua interface pública: `push`, `pop`, `topo`, `esta_vazia`, `len` e `repr`.

## 4. Custo amortizado

Uma operação individual de `desenfileirar()` ou `frente()` pode custar O(N).

Isso acontece quando a pilha de saída está vazia e é necessário transferir todos os elementos da pilha de entrada para a pilha de saída.

Apesar disso, o custo amortizado é O(1).

A razão é que cada elemento pode ser transferido da pilha de entrada para a pilha de saída no máximo uma vez. Depois de transferido, ele permanece na pilha de saída até ser removido.

Assim, considerando uma sequência de muitas operações:

1. cada elemento é inserido uma vez na pilha de entrada;
2. cada elemento é transferido no máximo uma vez para a pilha de saída;
3. cada elemento é removido uma vez da pilha de saída.

Portanto, embora uma operação isolada possa custar O(N), o custo total distribuído entre as operações é linear em relação ao número de elementos. Dessa forma, o custo médio por operação é O(1) amortizado.

## 5. Testes automatizados

Foram implementados testes utilizando o módulo `unittest` da biblioteca padrão do Python.

Os testes verificam:

- comportamento LIFO da pilha;
- comportamento FIFO da fila;
- inserções e remoções;
- operações alternadas;
- consulta do topo e da frente;
- comportamento com valores repetidos;
- utilização de `None`;
- consistência do tamanho;
- comportamento de estruturas vazias;
- reutilização da mesma fila após ficar vazia.

Os testes podem ser executados com:

```bash
python3 -m unittest -v P06_3511_testes.py
