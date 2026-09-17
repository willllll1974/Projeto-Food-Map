# ADR-002 — Escolha do MongoDB para os dados do registro das comidas

## Decisão

A equipe decidiu utilizar o MongoDB para armazenar os dados relacionados às comidas do FoodMap.

A escolha foi motivada pela familiaridade que a equipe já possuía com a ferramenta e pela pertinência de um banco de dados não relacional ao tipo de informação trabalhada pela aplicação. O FoodMap tem como objetivo auxliar na localização de restaurantes e na identificaçaõ de opções de alimentaçaõ específicas em restaurantes específicos, considerando diferentes necessidades alimentares dos usuários.

## Alternativa descartada

Não houve uma alternativa específica de banco de dados não relacional avaliada pela equipe antes da escolha do MongoDB.

A decisão foi tomada principalmente com base na familiaridade da equipe com a ferramenta, na pertinência do modelo não relacional para os dados trabalhados pelo FoodMap e no conhecimento adquirido sobre bancos de dados não relacionais em outra disciplina.

## consequência

A opção do MongoDB viabilizou o armazenamento dos dados de refeições em documentos, o que tornou mais simples a organização de atributos como ingredientes, classificação e as necessidades alimentares dos usuários.

## Commit

6b7805c - Documenta a escolha do MongoDB