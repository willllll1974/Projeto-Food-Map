# ADR-010 – Atualização da Tecnologia do Backend


## 1. Contexto

Durante as primeiras etapas do desenvolvimento do FoodMap, o backend foi documentado utilizando Python e PyMongo para realizar a comunicação com o MongoDB.

Com a evolução do projeto, a estrutura da API passou por mudanças e o backend passou a ser desenvolvido em C#, utilizando ASP.NET Core e .NET 8.

Essa alteração também modificou a maneira como a aplicação realiza a comunicação com os bancos de dados, acompanhando a nova estrutura adotada pela equipe.

## 2. Problema

A documentação inicial do projeto já não representava completamente a tecnologia utilizada na versão mais recente do FoodMap.

A utilização de Python e PyMongo estava registrada nas decisões anteriores, mas a implementação atual passou a utilizar outra linguagem e outros recursos para desenvolver a API e acessar os dados.

Por isso, foi necessário atualizar o registro das decisões arquiteturais para que a documentação acompanhasse a evolução do código-fonte.

## 3. Alternativas consideradas

Foram consideradas duas possibilidades:

**Alternativa A – Manter a tecnologia anterior:** continuar utilizando Python e PyMongo como base para o desenvolvimento do backend.

**Alternativa B – Adotar a nova estrutura:** utilizar C# com ASP.NET Core para desenvolver a API e os recursos de acesso aos bancos de dados.

## 4. Decisão

A equipe adotou a **Alternativa B**, utilizando C# e ASP.NET Core (.NET 8) no desenvolvimento do backend do FoodMap.

A comunicação com o MongoDB passou a utilizar o driver próprio da tecnologia para .NET, substituindo a utilização anteriormente documentada do PyMongo.

Essa mudança representa uma atualização da estrutura de desenvolvimento da API e dos mecanismos utilizados para acessar os dados.

## 5. Justificativa

A atualização foi realizada para acompanhar a nova estrutura definida para o projeto.

O uso de C# com ASP.NET Core permite desenvolver a API utilizando os recursos do ecossistema .NET, enquanto o driver do MongoDB possibilita realizar as operações necessárias diretamente pela aplicação.

Com isso, a equipe passou a trabalhar com uma estrutura de backend diferente daquela registrada nas primeiras decisões do projeto.

## 6. Consequências

A mudança permitiu atualizar a tecnologia utilizada no backend e adequar a comunicação com os bancos de dados à nova implementação.

Por outro lado, também foi necessário adaptar o código e revisar a documentação que ainda fazia referência à estrutura anterior.

Além disso, decisões antigas, como a utilização do PyMongo registrada na ADR-003, passaram a representar o histórico do projeto, e não a implementação atual.

## 7. Evolução futura

A estrutura atual poderá receber novas melhorias conforme o desenvolvimento do FoodMap avançar.

