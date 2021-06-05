from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from os import path
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return path.join(upload_to, filename)


class Rep(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    since = models.DateField(default=timezone.now, null=True, blank=True)
    type = models.CharField(
        choices=[
            ("1", "Feminina"),
            ("2", "Masculina"),
            ("3", "Mista")
        ],
        max_length=10
    )
    residents = models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to=path_and_rename, null=True)
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


