from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    # Campos del modelo
    id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=200)

    # Función estándar para presentar info
    def __str__(self):
        return self.nombre


class Hashtag(models.Model):
    # Campos del modelo
    id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=200)

    # Función estándar para presentar info
    def __str__(self):
        return self.nombre

class Entry(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title + " (" + self.autor.first_name + " " + self.autor.last_name + ")"
    
class Post(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title + " (" + self.autor.first_name + " " + self.autor.last_name + ")"
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Posteo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
