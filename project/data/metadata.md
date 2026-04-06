# Dataset de Contratos Públicos em Portugal  
Este dataset contém o histórico de contratos públicos em Portugal.  
Abaixo encontra-se a descrição técnica das colunas e a sua utilidade para análise de redes (*Network Science*).

---

## 1. Descrição das Colunas (Metadata)

| Coluna                         | Descrição                                                                 | Relevância no Estudo                                      |
|--------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------|
| Objeto do Contrato            | Descrição textual do serviço ou bem adquirido.                           | Análise de texto/NLP para temas.                          |
| Tipo de Procedimento          | Método de contratação (ex: Ajuste Direto, Concurso Público).             | Investigar transparência e concorrência.                  |
| CPV / CPV Designação          | Código comum europeu para categorias de produtos/serviços.               | Filtrar a rede por setores (ex: TI, Construção).          |
| Entidade(s) Adjudicante(s)    | Nome da entidade pública que compra (ex: Município).                     | Nó (*Buyer*).                                             |
| Entidade(s) Adjudicatária(s)  | Nome da empresa ou fornecedor que venceu o contrato.                     | Nó (*Supplier*).                                          |
| Preço Contratual              | Valor monetário total do contrato (sem IVA).                             | Peso da Aresta (*Edge Weight*).                           |
| Data de Celebração            | Data oficial da assinatura do contrato.                                  | Análise Temporal (Evolução 3 anos).                       |
| Local de Execução             | Localidade/Distrito/Concelho onde o serviço é prestado.                  | Filtrar monopólios por Município.                         |
| Lista de Fornecedores         | Empresas que participam em consórcios/agrupamentos.                      | Detetar *Co-bidding* e parcerias fixas.                   |
| Estado                        | Condição do contrato (Fechado, em execução, etc.).                       | Filtragem de dados válidos.                               |
| groupMembers                  | IDs ou nomes de membros de um grupo económico.                           | Identificar redes de empresas "irmãs".                    |

---

## 2. Mapeamento para Construção do Grafo

Para transformar este CSV numa rede, mapeia as colunas da seguinte forma:

| Componente de Rede | Coluna do Dataset               | Tipo de Dado | Nota Técnica                                                        |
|--------------------|--------------------------------|--------------|---------------------------------------------------------------------|
| Source (Origem)    | Entidade(s) Adjudicante(s)     | String       | Representa os "Hubs" públicos da rede.                             |
| Target (Destino)   | Entidade(s) Adjudicatária(s)   | String       | Representa as empresas fornecedoras.                               |
| Weight (Peso)      | Preço Contratual               | Float        | Define a força da ligação (volume de € movimentado).               |
| Timestamp          | Data de Celebração             | DateTime     | Permite criar "Slices" temporais para ver a evolução.              |
| Attributes         | Local de Execução              | String       | Atributo da aresta para isolar o grafo de um município.            |
| Co-occurrence      | Lista de Fornecedores          | List/String  | Usado para criar arestas entre empresas (*Co-bidding*).            |