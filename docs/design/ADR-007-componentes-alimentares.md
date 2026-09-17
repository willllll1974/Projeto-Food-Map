# ADR-007 — Representação dos componentes alimentares

## Contexto

Durante o desenvolvimento do FoodMap, a equipe precisou definir como seriam representados os componentes alimentares presentes nas comidas cadastradas.

Como a aplicação possui filtros relacionados a características alimentares e componentes que podem estar presentes nos alimentos, era necessário organizar essas informações de forma que a API pudesse utilizá-las nas consultas.

## Decisão

A equipe decidiu armazenar os componentes presentes na comida por meio de campos específicos, utilizando a convenção `contem_*`.

Entre os componentes representados estão `contem_gluten`, `contem_leite`, `contem_ovo`, `contem_soja`, `contem_amendoim`, `contem_castanhas`, `contem_peixe`, `contem_frutos_do_mar` e `contem_gergelim`.

A equipe optou por registrar somente os componentes que estão presentes na comida, evitando a criação de um campo separado para cada componente indicando explicitamente sua ausência.

## Alternativa descartada

A utilização de campos negativos específicos, como `sem_gluten`, `sem_leite` e outros campos semelhantes, não foi adotada.

A equipe optou por trabalhar com a presença dos componentes por meio dos campos `contem_*`, deixando para a API a interpretação da ausência desses campos durante a realização dos filtros.

## Consequência

Os documentos das comidas armazenam somente os componentes alimentares presentes.

Essa estrutura permite que a API realize filtros de acordo com a presença ou ausência dos componentes, utilizando os dados existentes nos documentos do MongoDB.

Como consequência, a aplicação mantém uma estrutura de dados mais alinhada à informação efetivamente cadastrada para cada comida, enquanto a lógica de filtragem fica responsável por interpretar a ausência de determinado componente.
    
## Commit

ab99d30 - Documenta a representação dos componentes alimentares