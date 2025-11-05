# 🐞 UGB - Capture the Bug - 04

### Descrição  
O time de vendas está desesperado!
O projeto até executa porém, eles tentam cadastrar novos produtos pelo formulário, a página até confirma o envio... mas **nada aparece no banco de dados**.  
Nenhum erro é mostrado, nenhum aviso..
Também não consigo ver a lista de todos os produtos cadastrados.

---

### Seu objetivo  
Investigue o código e descubra **por que os produtos não estão sendo salvos**.  

Verifique:
- Se o `form.is_valid()` está sendo usado corretamente  
- Se há algum passo faltando no processo de salvamento do formulário ou varíavel incorreta  
- E se o redirecionamento acontece antes do salvamento  
