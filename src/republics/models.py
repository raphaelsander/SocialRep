from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Rep(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='images/', null=True)
    # Has in a republic
    has_animal = models.BooleanField(default=False)
    has_3d_printer = models.BooleanField(default=False)
    has_garage = models.BooleanField(default=False)
    has_grill = models.BooleanField(default=False)
    has_internet = models.BooleanField(default=False)
    has_maid = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_snooker = models.BooleanField(default=False)
    has_washing_machine = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("republics:detail", kwargs={"slug": self.slug})
