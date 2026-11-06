# ADR-008 – Avaliação e Uso Futuro do Padrão de Projeto Facade

**Status:** Aceito  
**Data:** 06/11/2026

## 1. Contexto

O FoodMap utiliza uma arquitetura composta por diferentes tecnologias e fontes de dados, incluindo uma API desenvolvida em C# com ASP.NET Core, um banco de dados relacional MySQL e um banco de dados não relacional MongoDB.

Essa estrutura permite que o sistema trabalhe com diferentes tipos de informações, como dados cadastrais de estabelecimentos, endereços, unidades, alimentos e ingredientes.

Com o crescimento das funcionalidades, surgiu a possibilidade de utilizar o padrão de projeto Facade para simplificar a comunicação entre diferentes componentes da aplicação.

## 2. Problema

A utilização de diferentes fontes de dados pode aumentar a complexidade de determinadas operações, principalmente quando uma funcionalidade precisa consultar ou coordenar informações armazenadas no MySQL e no MongoDB.

Nesse cenário, foi avaliada a possibilidade de implementar uma camada Facade, responsável por centralizar e organizar essas operações, oferecendo uma interface simplificada para os demais componentes do sistema.

Entretanto, é necessário avaliar se essa abstração realmente traria benefícios para a versão atual do FoodMap, considerando a complexidade existente e o estágio de desenvolvimento do projeto.

## 3. Possibilidades de aplicação do Facade

Foram identificados dois possíveis cenários de utilização futura do padrão:

### 3.1. Busca gastronômica

Uma possível `BuscaGastronomicaFacade` poderia centralizar operações relacionadas à pesquisa de alimentos e estabelecimentos, coordenando consultas ao MySQL e ao MongoDB.

Isso permitiria reunir informações de diferentes fontes e disponibilizá-las de maneira organizada para a funcionalidade de busca.

### 3.2. Gerenciamento de unidades

Uma possível `GestaoUnidadeFacade` poderia centralizar operações relacionadas ao cadastro, atualização e exclusão de unidades, coordenando as informações necessárias entre as diferentes fontes de dados.

Essa abordagem poderia reduzir a complexidade dos componentes responsáveis por essas operações.

As classes apresentadas são propostas de evolução arquitetural, não implementações existentes na versão atual do sistema.

## 4. Alternativas consideradas

Foram consideradas duas alternativas:

**Alternativa A – Implementar o padrão Facade na versão atual**

Criar uma camada de abstração para centralizar operações que envolvam diferentes componentes e fontes de dados.

**Alternativa B – Não implementar o padrão Facade nesta versão**

Manter a arquitetura atual, utilizando os serviços e componentes já existentes, e considerar a adoção do padrão somente quando houver necessidade concreta de simplificação ou centralização das operações.

## 5. Decisão

Foi escolhida a **Alternativa B: não implementar o padrão Facade na versão atual do FoodMap**.

A arquitetura existente será mantida, sem a criação de uma camada adicional de Facade neste momento.

A possibilidade de adoção futura do padrão permanecerá aberta, caso o crescimento do sistema gere maior complexidade na comunicação entre componentes ou na integração das diferentes fontes de dados.

## 6. Justificativa técnica

A decisão foi baseada nos seguintes aspectos:

- A arquitetura atual atende às necessidades identificadas para a versão presente do sistema.
- A implementação do Facade adicionaria classes e uma camada de abstração que ainda não demonstram necessidade concreta.
- Nem todas as operações exigem a coordenação de múltiplas fontes de dados.
- A adoção antecipada do padrão poderia aumentar a complexidade de manutenção sem proporcionar benefícios proporcionais.
- A arquitetura poderá evoluir posteriormente, conforme novas funcionalidades e necessidades forem identificadas.

Portanto, optou-se por evitar abstrações prematuras e priorizar a simplicidade da implementação atual.

## 7. Consequências

### Consequências positivas

- Manutenção da simplicidade arquitetural.
- Redução de camadas e classes adicionais.
- Menor complexidade de implementação neste estágio do projeto.
- Liberdade para avaliar a necessidade do padrão conforme o crescimento do sistema.

### Consequências negativas

- Algumas operações futuras poderão exigir coordenação direta entre diferentes serviços e fontes de dados.
- Caso a complexidade aumente, poderá ser necessário refatorar componentes existentes para introduzir uma camada Facade.
- A ausência dessa abstração poderá resultar em maior responsabilidade individual para determinados serviços.

## 8. Possibilidade de evolução futura

A implementação do padrão Facade poderá ser reavaliada em versões futuras do FoodMap, especialmente quando houver necessidade de centralizar operações que envolvam simultaneamente o MySQL e o MongoDB.

Entre as possibilidades estão a criação de uma fachada para buscas gastronômicas e outra para o gerenciamento de unidades e seus respectivos dados.

A adoção deverá ocorrer somente quando representar uma melhoria efetiva na organização, manutenção e evolução da arquitetura do sistema.

---

**Conclusão:** O padrão Facade foi avaliado, mas sua implementação foi adiada. A decisão prioriza a simplicidade da arquitetura atual, sem descartar sua utilização em futuras evoluções do FoodMap.