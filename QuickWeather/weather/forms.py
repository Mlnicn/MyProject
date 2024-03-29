from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form_control',
            'name': 'city','id': 'city',
            'plaseholder': 'Введите Ваш город'
        })}
