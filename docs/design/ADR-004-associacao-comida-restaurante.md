# ADR-004 — Associação da comida ao restaurante por meio do restauranteId

## Contexto

Durante o desenvolvimento do FoodMap, a equipe precisou definir como os dados de cada comida seriam relacionados aos restaurantes cadastrados na aplicação.

Como uma comida é disponibilizada por um restaurante específico, era necessário manter uma identificação que permitisse relacionar cada registro de comida ao restaurante correspondente.

A equipe já possuía familiaridade com a utilização de identificadores para relacionar dados em sistemas de banco de dados.

## Decisão

A equipe decidiu utilizar o campo `restauranteId` para identificar o restaurante ao qual cada comida pertence.

Dessa forma, cada comida possui uma referência ao restaurante responsável por disponibilizá-la, permitindo que os dados sejam relacionados e que a aplicação consiga realizar filtros utilizando essa identificação.

O `restauranteId` é gerenciado pelo sistema MVC .NET e utilizado pelo Django para realizar os filtros necessários na consulta dos dados de comidas.

## Alternativa descartada

Não houve uma estrutura alternativa específica formalmente avaliada pela equipe além desta para realizar a associação entre comida e restaurante.

A equipe adotou o `restauranteId` por já possuir familiaridade com esse tipo de estrutura de relacionamento em bancos de dados e por ela atender à necessidade de identificar de forma objetiva o restaurante responsável por cada comida.

## Consequência

A utilização do `restauranteId` permite identificar de forma objetiva a qual restaurante cada comida pertence.

Essa estrutura também possibilita que a API realize consultas e filtros utilizando a identificação do restaurante, facilitando a obtenção das comidas associadas a um estabelecimento específico.

Como consequência, cada registro de comida mantém sua associação com um único restaurante por meio do campo `restauranteId`.

## Commit

16091f8 — Documenta associação entre comida e restaurante