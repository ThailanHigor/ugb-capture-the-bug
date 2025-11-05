# 🐞 UGB - Capture the Bug - 01

### Descrição
O endpoint `/api/products/` deveria listar todos os produtos cadastrados no banco.
Mas algo está quebrado — ele retorna 404.

### Seu objetivo
Corrigir o projeto para que o endpoint funcione e retorne uma lista JSON de produtos, assim:

```json
[
  {"id": 1, "name": "Caneta", "price": "3.50"},
  {"id": 2, "name": "Caderno", "price": "15.00"}
]
