from django.db import models

# Create your models here.


class Autores(models.Model):
    autores = models.CharField(max_length=50)

    def __str__(self):
        return str(self.autores)

    class Meta:
        db_table = 'autores_info'


class Obras(models.Model):
    titulo = models.CharField(max_length=150)
    editora = models.CharField(max_length=120)
    foto = models.FileField(upload_to='foto')
    autores = models.ForeignKey(Autores, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)

    class Meta:
        db_table = 'obras_info'