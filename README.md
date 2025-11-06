# 🐞 UGB - Capture the Bug - 23

### Descrição
O front-end consome a API de produtos e percebe problemas graves:

1. Mesmo quando algo dá errado, a API retorna **status 200 OK**  
2. Ao tentar retornar uma lista de produtos, a API lança erro

### Objetivo
Corrigir a API para que:

1. Retorne **status HTTP correto** em caso de erro  
2. Retorne a lista de produtos
3. A API seja consistente e previsível com seus STATUS CODES