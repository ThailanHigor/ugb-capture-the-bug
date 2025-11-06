from django.db import models

class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição", blank=True, default="")
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    image = models.ImageField("Imagem", upload_to="products/", null=True, blank=True)
    active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]