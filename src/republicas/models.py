from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-criado",)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("republicas:detail", kwargs={"slug": self.slug})
