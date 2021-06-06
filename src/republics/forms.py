from .models import Rep
from django import forms
from datetime import date

# https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html


class CreateForm(forms.ModelForm):
    class Meta:
        model = Rep
        fields = ('name', 'slug', 'since', 'type', 'residents', 'lived', 'body', 'img', 'has_animal',
                  'has_3d_printer', 'has_garage', 'has_grill', 'has_internet', 'has_maid', 'has_pool',
                  'has_snooker', 'has_washing_machine')

    def check_date(self):
        if self > date.today():
            raise forms.ValidationError("De volta para o futuro?")

    def clean(self):
        cleaned_data = super().clean()

        residents = cleaned_data.get("residents")
        lived = cleaned_data.get("lived")

        if lived < residents:
            raise forms.ValidationError("O número de pessoas que já moraram deve ser maior "
                                        "ou igual ao número de pessoas que moram atualmente!")

    name = forms.CharField(label="Nome", max_length=255)
    slug = forms.SlugField(label="Slug", max_length=50)
    since = forms.DateField(
        label="Desde",
        validators=[check_date],
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    type = forms.ChoiceField(
        label="Tipo",
        choices=[
            ("1", "Feminina"),
            ("2", "Masculina"),
            ("3", "Mista")
        ]
    )
    residents = forms.DecimalField(label="Moradores", min_value=1)
    lived = forms.DecimalField(
        label="Moraram",
        min_value=1
    )
    body = forms.CharField(label="Descrição", widget=forms.Textarea)
    img = forms.ImageField(label="Imagem")
    has_animal = forms.BooleanField(label="Animal", required=False)
    has_3d_printer = forms.BooleanField(label="Impressora 3D", required=False)
    has_garage = forms.BooleanField(label="Garagem", required=False)
    has_grill = forms.BooleanField(label="Churrasqueira", required=False)
    has_internet = forms.BooleanField(label="Internet", required=False)
    has_maid = forms.BooleanField(label="Empregada/Diarista", required=False)
    has_pool = forms.BooleanField(label="Piscina", required=False)
    has_snooker = forms.BooleanField(label="Sinuca/Bilhar", required=False)
    has_washing_machine = forms.BooleanField(label="Máquina de Lavar", required=False)
