# ADR-006 — Classificação das comidas

## Contexto

Durante o desenvolvimento do FoodMap, a equipe precisou definir como seriam organizadas as características e categorias das comidas cadastradas.

Uma mesma comida pode apresentar mais de uma característica, como ser vegetariana, vegana, sobremesa, bebida, lanche, entre outras. Essas informações precisavam ficar estruturadas para facilitar a organização e as consultas realizadas pela aplicação.

## Decisão

A equipe decidiu utilizar o campo `classificacoes` como uma lista de classificações associadas a cada comida.

Essa estrutura permite que uma mesma comida possua múltiplas classificações, mantendo suas características organizadas no próprio documento e facilitando a realização de filtros relacionados ao tipo e às características alimentares.

## Alternativa descartada

Não houve uma estrutura alternativa específica formalmente avaliada pela equipe antes da adoção do campo `classificacoes`.

A equipe optou por utilizar uma lista de classificações porque uma mesma comida pode possuir diferentes características, sendo necessário permitir que essas informações fossem armazenadas de forma organizada no documento.

## Consequência

Cada comida pode possuir várias classificações, como `vegano`, `vegetariano`, `bebida`, `sobremesa`, `lanche` e outras definidas pelo projeto.

Essa estrutura permite que a API utilize essas classificações durante as consultas e filtros das comidas.

## Commit

Será preenchido após o commit desta ADR.