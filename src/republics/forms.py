from .models import Rep
from django import forms

# https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html


class CreateForm(forms.ModelForm):
    class Meta:
        model = Rep
        fields = ('name', 'slug', 'body', 'img', 'has_animal', 'has_3d_printer', 'has_garage',
                  'has_grill', 'has_internet', 'has_maid', 'has_pool', 'has_snooker', 'has_washing_machine')

    name = forms.CharField(label="Nome", max_length=255, required=True)
    slug = forms.SlugField(label="Slug", max_length=50, required=True)
    body = forms.CharField(label="Descrição", widget=forms.Textarea, required=True)
    img = forms.ImageField(label="Imagem")
    has_animal = forms.BooleanField(label="Animal")
    has_3d_printer = forms.BooleanField(label="Impressora 3D")
    has_garage = forms.BooleanField(label="Garagem")
    has_grill = forms.BooleanField(label="Churrasqueira")
    has_internet = forms.BooleanField(label="Internet")
    has_maid = forms.BooleanField(label="Empregada/Diarista")
    has_pool = forms.BooleanField(label="Piscina")
    has_snooker = forms.BooleanField(label="Sinuca/Bilhar")
    has_washing_machine = forms.BooleanField(label="Máquina de Lavar")
