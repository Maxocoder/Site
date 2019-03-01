from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import pytz
CHOISES = (
    ('null', '- - - -'),
    ('Петров Василий Иванович', 'Петров Василий Иванович'),
    ('Васильев Петр Игоревич', 'Васильев Петр Игоревич'),
    ('Иванов Константин Петрович', 'Иванов Константин Петрович'),
)


class FormRegistration(forms.Form):
    lastname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    firstname = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    reporting = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    auto = forms.CharField(label='Марка автомобиля', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(required=False, label='E-Mail (необязательно)', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    profi = forms.ChoiceField(label='Выберите специалиста', choices=CHOISES)



    def clean_profi(self):
        data = self.cleaned_data['profi']

        if data == 'null':
            raise ValidationError(_("Выберите специалиста"), code='invalid')
        return data


class FormTime(forms.Form):

    datetime = forms.DateTimeField(label="", initial=datetime.datetime.today(), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text'
    }))

    def clean_datetime(self):
        data = self.cleaned_data['datetime']
        # tzinfo=pytz.UTC
        if data < datetime.datetime.utcnow().replace():
            raise ValidationError(_("Выберите правильную дату"), code='invalid')

        if data.hour > 18 and data.minute > 0:
            raise ValidationError(_("Диагностика длится час, сервис работает до 20:00, пожалуйста, выберите другое "
                                    "время"), code='invalid')

        return data