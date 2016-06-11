from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.criado_em = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
