from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
