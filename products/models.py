from django.db import models

class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição", blank=True)
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    discount = models.DecimalField("Desconto", max_digits=5, decimal_places=2, default=0)
    active = models.BooleanField("Ativo", default=True)

    def __str__(self):
        return self.name
