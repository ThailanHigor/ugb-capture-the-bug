# 🐞 UGB - Capture the Bug - 17

### Descrição
O setor administrativo quer cadastrar produtos com categorias definidas e preços positivos.  
Porém, o formulário apresenta vários problemas:

1. O campo **categoria** aparece vazio, mesmo com categorias cadastradas no banco.  
2. O formulário está aceitando dados inválidos como a questão do preço negativo.  
3. Não existe validação para impedir que **preço seja menor que zero**.

O formulário funciona parcialmente, mas o sistema aceita produtos com valores inválidos ou sem categoria.  
Isso causa problemas na listagem e no processamento de produtos.

### Objetivo
Corrigir o formulário e a view para que:

- A lista de categorias apareça corretamente  
- O formulário valide os dados 
- Preço negativo não seja permitido  
