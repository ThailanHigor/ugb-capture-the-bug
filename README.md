# 🐞 UGB - Capture the Bug - 13

### Descrição
O front-end do sistema envia dados via API para criar ou buscar produtos.  
No entanto, sempre que envia um POST com o campo `preco`, a API retorna um erro:

```json
{"detail": "Unknown field 'preco'."}
```