# 🐞 UGB - Capture the Bug - 14

### Descrição
O front-end tenta atualizar produtos existentes via API, usando um PUT para `/api/products/<id>/`.  
Mas, ao invés de atualizar o produto, a API **cria um novo** com os mesmos dados.  
Isso está gerando duplicações e confusão no banco.

### Objetivo
Fazer o PUT atualizar e não criar.