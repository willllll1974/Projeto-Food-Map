## **🍽️ FoodMap**

📖 Sobre o projeto

O FoodMap é uma aplicação desenvolvida com o objetivo de organizar e facilitar a consulta de informações relacionadas a alimentos, restaurantes, ingredientes e características alimentares.

Durante o desenvolvimento do projeto, a equipe precisou tomar diversas decisões relacionadas à arquitetura da aplicação, tecnologias utilizadas, persistência dos dados e modelagem das informações.

Para registrar essas decisões e seus respectivos motivos, foi elaborado um Caderno de Design baseado em Architecture Decision Records (ADRs).

tilizada como ferramenta de apoio à organização, revisão e aprimoramento textual da documentação.

🏛️ Arquitetura e decisões

As principais decisões técnicas do FoodMap foram documentadas através das seguintes ADRs:

ADR

Decisão

Área

🟣 001

Interface Web com React

Frontend

🟢 002

Escolha do MongoDB

Banco de Dados

🔵 003

Escolha do PyMongo

Backend

🟠 004

Associação entre comida e restaurante

Modelagem

🟡 005

Estrutura dos ingredientes

Modelagem

🔴 006

Criação do restauranteId

Mapeamento

🟤 007

Representação dos componentes alimentares

Dados

<br><br>

🧩 ADR-001

Interface Web com React

📌 Contexto

Era necessário definir uma tecnologia para desenvolver a interface web do FoodMap, permitindo organizar o frontend em componentes e realizar a integração com a API.

✅ Decisão

A equipe optou pela utilização do React para o desenvolvimento da interface.

A escolha permite trabalhar com componentes reutilizáveis, organização modular e uma estrutura que facilita a evolução do frontend.

❌ Alternativa descartada

Foi considerada a utilização do padrão MVC para a interface web, porém essa abordagem não foi adotada.

📈 Consequência

A camada de apresentação passou a ser estruturada através de componentes React, mantendo o frontend separado da implementação interna da API.

Isso permite que frontend e backend evoluam de maneira mais independente.

🧩 ADR-002

Escolha do MongoDB

📌 Contexto

O projeto precisava de uma solução para realizar a persistência das informações sobre comidas e demais dados utilizados pelo sistema.

✅ Decisão

A equipe escolheu o MongoDB como banco de dados.

A decisão foi influenciada principalmente pela familiaridade da equipe com a tecnologia e pela facilidade de utilização.

O MongoDB utiliza um modelo orientado a documentos, permitindo trabalhar com estruturas flexíveis semelhantes a JSON através do formato BSON.

💭 Alternativa

Não foi definida uma alternativa específica para comparação direta. A escolha foi baseada principalmente na familiaridade da equipe e na adequação do modelo de documentos às necessidades do projeto.

📈 Consequência

Os dados passaram a ser persistidos utilizando o modelo de documentos do MongoDB, influenciando diretamente a modelagem das informações e as operações realizadas pela API.

🧩 ADR-003

Escolha do PyMongo

📌 Contexto

Após a escolha do MongoDB, era necessário definir como a aplicação desenvolvida em Python realizaria a comunicação com o banco de dados.

✅ Decisão

Foi adotado o PyMongo como biblioteca de comunicação entre a aplicação Python e o MongoDB.

Através dele, a aplicação consegue realizar operações como:

🔎 Consultas

➕ Inserções

✏️ Atualizações

📄 Manipulação de documentos

📈 Consequência

A camada responsável pelo acesso aos dados utiliza o PyMongo para realizar a comunicação com as coleções do MongoDB.

A coleção comidas, por exemplo, pode ser acessada pela aplicação através dessa camada.

🧩 ADR-004

Associação entre comida e restaurante

📌 Contexto

Era necessário estabelecer uma relação entre uma comida e o restaurante responsável por aquele alimento.

✅ Decisão

Foi definido o uso do campo:

restauranteId

Esse identificador permite estabelecer uma correspondência entre determinado alimento e o estabelecimento ao qual ele pertence.

🎯 Objetivo

A utilização do identificador evita a necessidade de repetir todas as informações do restaurante dentro de cada documento de comida.

Dessa forma, os dados permanecem mais organizados e a duplicação de informações é reduzida.

📈 Consequência

A API consegue utilizar o identificador para localizar e relacionar corretamente os alimentos aos respectivos estabelecimentos.

🧩 ADR-005

Estrutura dos ingredientes

📌 Contexto

Era necessário definir como os ingredientes dos alimentos seriam armazenados no banco de dados.

A equipe poderia criar uma estrutura independente para os ingredientes ou armazená-los diretamente junto à comida.

✅ Decisão

Foi decidido armazenar os ingredientes como uma lista dentro do próprio documento da comida.

Exemplo conceitual:

{
  "nome": "Pizza",
  "ingredientes": [
    "farinha",
    "queijo",
    "molho de tomate"
  ]
}

❌ Alternativa descartada

A criação de uma estrutura ou coleção separada para os ingredientes foi considerada, mas não adotada.

Para as necessidades identificadas no FoodMap, essa alternativa acrescentaria complexidade sem uma necessidade clara que justificasse a separação.

📈 Consequência

Os ingredientes permanecem diretamente associados ao alimento, tornando sua organização e recuperação mais simples.

🧩 ADR-006

Criação do restauranteId

📌 Contexto

Durante o desenvolvimento do FoodMap, a equipe identificou que a criação de um identificador próprio para cada restaurante seria um elemento essencial para o funcionamento e para os objetivos do projeto.

Por esse motivo, a necessidade do restauranteId foi discutida pela equipe antes de sua implementação.

✅ Decisão

Foi definida a criação e adoção do campo:

restauranteId

O identificador permite diferenciar os estabelecimentos e estabelecer uma referência própria para cada restaurante cadastrado.

🎯 Objetivos

A utilização do restauranteId possui dois objetivos principais:

📍 Mapeamento dos estabelecimentos

Permitir o mapeamento correto dos restaurantes ao redor da cidade, identificando cada estabelecimento de maneira individual.

🥗 Correspondência com as características alimentares

Estabelecer a correspondência entre os restaurantes, alimentos e ingredientes, facilitando a localização de opções alimentares para usuários que possuem restrições relacionadas a determinados componentes.

🚫 Alternativas

Não foram consideradas alternativas para essa decisão.

O restauranteId foi definido como um elemento essencial para o projeto, e a discussão realizada pela equipe esteve relacionada à necessidade e à adoção desse recurso, e não à escolha entre diferentes alternativas.

📈 Consequência

O restauranteId passou a funcionar como uma referência fundamental para o relacionamento entre os estabelecimentos e os alimentos.

Com isso, o FoodMap consegue organizar melhor o mapeamento dos restaurantes e estabelecer correspondências necessárias para suas consultas relacionadas a alimentos e restrições alimentares.

🧩 ADR-007

Representação dos componentes alimentares

📌 Contexto

O FoodMap possui informações relacionadas às características e componentes presentes nos alimentos.

Era necessário definir uma forma padronizada de representar essas informações para permitir consultas e filtros.

✅ Decisão

A equipe adotou a convenção:

contem_*

Alguns exemplos utilizados são:

contem_gluten
contem_leite
contem_ovo
contem_soja
contem_amendoim
contem_castanhas
contem_peixe
contem_frutos_do_mar
contem_gergelim

💡 Funcionamento

Os campos representam os componentes presentes no alimento.

Assim, a aplicação pode utilizar essas informações para realizar filtros relacionados às características alimentares.

❌ Alternativa descartada

Também foi considerada a utilização de campos negativos, como:

sem_gluten
sem_leite

Porém, a equipe optou por registrar os componentes através do padrão contem_*.

📈 Consequência

Os documentos armazenam diretamente os componentes presentes nos alimentos, permitindo que a API interprete essas informações durante as consultas e filtros.

🔗 Relação entre as ADRs

As decisões registradas não funcionam de maneira isolada. Elas formam uma estrutura relacionada dentro do FoodMap.

                    🍽️ FOODMAP
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     🖥️ React         🗄️ MongoDB       🏪 Restaurantes
        │                │                │
        │             PyMongo        restauranteId
        │                │                │
        └────────────────┼────────────────┘
                         │
                     🍔 Comidas
                         │
              ┌──────────┴──────────┐
              │                     │
        🥕 Ingredientes       🥗 Componentes
              │                     │
           ADR-005                ADR-007

A arquitetura pode ser compreendida da seguinte maneira:

React → responsável pela interface web.

Python + PyMongo → responsáveis pela aplicação e comunicação com o banco.

MongoDB → responsável pela persistência dos dados.

restauranteId → estabelece referências entre estabelecimentos e alimentos.

Ingredientes → armazenados diretamente nos documentos das comidas.

contem_* → representa os componentes alimentares utilizados nas consultas e filtros.

🛠️ Tecnologias

Tecnologia

Utilização

⚛️ React

Interface web

🐍 Python

Desenvolvimento da aplicação

🍃 MongoDB

Banco de dados

🔌 PyMongo

Comunicação com o MongoDB

🎯 Objetivo das decisões

O conjunto das ADRs permite registrar não apenas quais tecnologias e estruturas foram utilizadas, mas também por que determinadas decisões foram tomadas durante o desenvolvimento.

Essa documentação facilita:

📚 Compreensão da arquitetura

🔍 Consulta das decisões realizadas

🛠️ Manutenção do sistema

🔄 Evolução futura do projeto

👥 Comunicação entre os integrantes da equipe

🧠 Compreensão do contexto técnico do FoodMap

Dessa maneira, o Caderno de Design funciona como um histórico técnico do projeto, permitindo compreender o caminho percorrido pela equipe durante o desenvolvimento.

📌 Conclusão

As ADRs documentam as principais decisões que contribuíram para a construção do FoodMap.

Desde a escolha do React para a interface e do MongoDB para persistência, passando pela comunicação através do PyMongo, até a modelagem de restaurantes, alimentos, ingredientes e componentes alimentares, cada decisão possui uma função dentro da estrutura do sistema.

O restauranteId, em especial, representa uma decisão fundamental para o mapeamento dos estabelecimentos e para a correspondência entre restaurantes, alimentos e características relacionadas às restrições alimentares.

Assim, o Caderno de Design permite visualizar não apenas o que foi desenvolvido, mas também o contexto e os motivos por trás das principais decisões técnicas do FoodMap.

🤖 Uso de Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio à organização, revisão e aprimoramento textual da documentação. As decisões técnicas, definições da aplicação e desenvolvimento do projeto permanecem sob responsabilidade da equipe.
