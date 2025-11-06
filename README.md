# 🐞 UGB - Capture the Bug - 06

### Descrição
O formulário de edição de produtos parece funcionar perfeitamente, ele abre, mostra os dados e até exibe a mensagem de sucesso. Mas o preço **nunca atualiza!**  

### Seu objetivo
Corrigir a view responsável pelo formulário de edição para que o produto seja **realmente atualizado** ao salvar.

### Dicas
- Verifique o uso do `ModelForm` e se a instância do objeto está sendo passada corretamente.
- Teste o formulário e confira se todos os campos são atualizados corretamente.
- Fique atento ao método `form.save()` e ao parâmetro `instance`.

