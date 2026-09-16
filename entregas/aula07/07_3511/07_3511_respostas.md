# Aula 7 - Busca em Labirinto

## Questão 1

Foi implementada uma versão iterativa da busca em profundidade (DFS).

A implementação utiliza uma pilha para armazenar as posições que ainda
precisam ser visitadas. Dessa forma, a busca é realizada sem utilizar
recursão.

As posições visitadas são armazenadas para evitar que uma mesma posição
seja processada novamente.

## Questão 2

Para encontrar o caminho da posição (1,1) até o queijo, foi utilizada a
busca em profundidade (DFS).

A escolha do DFS foi feita porque o algoritmo permite explorar o labirinto
por diferentes caminhos utilizando uma pilha. A cada posição visitada,
seus vizinhos que podem ser percorridos são adicionados à pilha.

Durante a busca, foi armazenada a posição anterior de cada posição
visitada. Quando o queijo é encontrado, essas informações permitem
reconstruir o caminho desde o queijo até a posição inicial.

O caminho encontrado é então exibido no terminal utilizando o caractere
* para representar as posições percorridas.
