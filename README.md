# 🐞 UGB - Capture the Bug - 21

### Descrição
O sistema de produtos deve ser acessado apenas por **usuários autenticados**.  
No entanto, atualmente qualquer visitante consegue acessar a página de cadastro ou edição de produtos e até salvar dados indevidamente. O sistema deveria permitir ver a lista sem autenticação mas cadastrar e editar somente autenticado.

### Objetivo
Corrigir as views para que apenas usuários logados possam acessar:

1. Cadastro de produtos  
2. Edição de produtos  
3. Listagem se necessário  (sem autenticar) 