from .models import Rep
from django import forms


class CreateForm(forms.ModelForm):
    class Meta:
        model = Rep
        fields = ('name', 'body', 'slug', 'img', 'has_animal', 'has_3d_printer', 'has_garage',
                  'has_grill', 'has_internet', 'has_maid', 'has_pool', 'has_snooker', 'has_washing_machine')
