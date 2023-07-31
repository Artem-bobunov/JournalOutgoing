from django.forms import *
from .models import journal

class FormInputJournal(ModelForm):
    class Meta:
        model = journal
        fields = "__all__"
        widgets = {
                    'res_ni':Select(attrs={'class': 'form-control'}),
                    'dateReg':TextInput(attrs={'class': 'form-control','type': 'date','format':'%d.%m.%Y'}),
                    'numberInput': TextInput(attrs={'class': 'form-control'}),
                    'res_nm': TextInput(attrs={'class': "form-control"}),
                    'adresat': TextInput(attrs={'class': "form-control"}),
                    'content': TextInput(attrs={'class': "form-control"}),
                    'executor': TextInput(attrs={'class': "form-control"}),
                    'note': TextInput(attrs={'class': "form-control"}),
        }
