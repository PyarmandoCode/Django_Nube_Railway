from django.db import models


class Departamentos(models.Model):
    departamento_nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.departamento_nombre
