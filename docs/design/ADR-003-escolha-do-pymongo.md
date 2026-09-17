# ADR-003 — Escolha do PyMongo para acesso ao MongoDB

## Contexto

Durante o desenvolvimento do FoodMap, a equipe precisou definir como a aplicação Django realizaria o acesso aos dados de comidas armazenados no MongoDB.

Como os dados das comidas são armazenados em uma base MongoDB, foi necessário utilizar uma ferramenta capaz de realizar a comunicação entre a aplicação e o banco de dados.

A equipe já possuía familiaridade com o MongoDB e com o PyMongo, o que facilitou sua utilização no desenvolvimento da aplicação.



## Decisão

A equipe decidiu utilizar o PyMongo para realizar o acesso aos dados armazenados no MongoDB.

A escolha foi motivada principalmente pela familiaridade da equipe com a ferramenta e pela necessidade de realizar a comunicação entre a aplicação Django e o banco de dados MongoDB de forma direta.

Além disso, o PyMongo permite trabalhar diretamente com a estrutura de documentos e coleções utilizada pelo MongoDB, atendendo às necessidades do FoodMap.

## Consequência

A utilização do PyMongo permite que a aplicação Django acesse diretamente a coleção `comidas` do MongoDB e obtenha os dados necessários para disponibilização pela API.

Essa abordagem também permite trabalhar diretamente com a estrutura dos documentos armazenados no MongoDB, incluindo informações como ingredientes, classificações e características alimentares.

Como consequência, o acesso aos dados de comidas é realizado pelo PyMongo, sem a utilização do Django ORM para essa parte específica da aplicação.

## Commit

36906e8 - Documenta escolha do Pymongo