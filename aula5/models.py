from django.db import models

# Create your models here.

    


#class Categoria

#class Post

#class Comentario

class Carrinho(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = self.produto_set.all().aggregate(models.sum('preco'))
        return total['preco__sum']


#class Produto(models.Model):
    