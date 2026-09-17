# ADR-005 — Armazenamento dos ingredientes na comida

## Contexto

Durante o desenvolvimento do FoodMap, a equipe precisou definir como as informações dos ingredientes seriam armazenadas nos dados de cada comida.

Como o sistema é voltado para a consulta de comidas e suas características, era necessário manter os ingredientes associados diretamente às comidas às quais pertencem.

## Decisão

A equipe decidiu armazenar os ingredientes diretamente no documento de cada comida, utilizando uma lista de ingredientes.

A escolha foi feita porque o FoodMap é uma aplicação específica para o cadastro e consulta de comidas, tornando mais simples manter os ingredientes junto às informações da própria comida.

## Alternativa descartada

A equipe não adotou uma estrutura separada para armazenar os ingredientes, pois considerou que essa separação seria desnecessária para a proposta do FoodMap e tornaria a estrutura dos dados mais complexa.

## Consequência

Os ingredientes ficam armazenados junto aos demais dados de cada comida no MongoDB.

Essa estrutura facilita a consulta das informações de uma comida, pois seus ingredientes podem ser obtidos diretamente no mesmo documento, sem a necessidade de buscar essas informações em uma estrutura separada.

## Commit

28145bc - Documenta estrutura dos ingredientes