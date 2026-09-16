# Aula 5 - Orientação a Objetos e UML

## Questão 1 - Relações de herança

As classes podem ser organizadas em diferentes hierarquias de herança.

A primeira hierarquia é formada por `Pessoa` e `Funcionario`. A classe
`Funcionario` pode herdar de `Pessoa`, pois um funcionário é uma pessoa.
Dessa forma, `Funcionario` herdaria os atributos `nome` e `idade`.

A partir de `Funcionario`, podem ser criadas as subclasses `Garçom`,
`Chefe de cozinha` e `Gerente`. Essas classes herdariam os atributos
`nome`, `idade`, `salario` e `carga_horaria`.

Outra hierarquia pode ser formada pela classe `Iguaria (comida)`, que
representa uma comida de forma geral. As classes `Pizza` e `Bolo` podem
herdar de `Iguaria`, recebendo os atributos `nome` e `preco`. A classe
`Pizza` possui ainda o atributo `borda_recheada`, enquanto `Bolo` possui
o atributo `formato`.

Também é possível considerar `Pizzaria` como uma especialização de
`Restaurante`, pois uma pizzaria é um tipo específico de restaurante.
Nesse caso, `Pizzaria` herdaria os atributos `nome`, `endereco` e
`telefone` de `Restaurante` e possuiria seu próprio atributo `rodizio`.

Portanto, as principais hierarquias podem ser representadas como:

- `Pessoa` -> `Funcionario` -> `Garçom`
- `Pessoa` -> `Funcionario` -> `Chefe de cozinha`
- `Pessoa` -> `Funcionario` -> `Gerente`
- `Iguaria` -> `Pizza`
- `Iguaria` -> `Bolo`
- `Restaurante` -> `Pizzaria`

A herança permite reutilizar atributos comuns e acrescentar
características específicas nas subclasses.

## Questão 2 - Relação entre Restaurante e Iguaria

A relação entre `Restaurante` e `Iguaria` não deve ser representada por
herança, pois uma iguaria não é um restaurante. O relacionamento mais
adequado é uma relação de agregação, pois um restaurante oferece ou
mantém um conjunto de iguarias.

Uma possibilidade seria adicionar à classe `Restaurante` um atributo
como:

`iguarias: list[Iguaria]`

Esse atributo armazenaria os objetos correspondentes às comidas
oferecidas pelo restaurante.

Assim, um restaurante poderia possuir várias iguarias, como pizzas e
bolos. Essas iguarias poderiam ser representadas por instâncias de
`Pizza`, `Bolo` ou outras subclasses de `Iguaria`.

No diagrama UML, essa relação pode ser representada por uma agregação
entre `Restaurante` e `Iguaria`, com um restaurante associado a zero ou
mais iguarias.

## Questão 3 - Tipos dos argumentos

### argumento1

O tipo mais adequado seria `list[Iguaria]`.

O método `anotar_pedido(argumento1)` representa o registro de um pedido,
que pode conter várias comidas. Por isso, uma lista de objetos
`Iguaria` permite representar os diferentes itens de um pedido.

### argumento2

O tipo mais adequado seria `Iguaria`.

O método `preparar(argumento2)` pertence ao `Chefe de cozinha` e recebe
uma comida que deverá ser preparada. Como `Pizza` e `Bolo` são subclasses
de `Iguaria`, uma instância de `Iguaria` permite representar diferentes
tipos de comida.

### argumento3

O tipo mais adequado seria `Funcionario`.

O método `demitir(argumento3)` pertence ao `Gerente` e representa a
demissão de um funcionário. Portanto, o argumento deve receber uma
instância de `Funcionario`, podendo também representar qualquer uma de
suas subclasses, como `Garçom` ou `Chefe de cozinha`.
