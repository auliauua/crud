from django.forms import ModelForm
from django import forms
from untirta.models import Dosen


class FormDosen(ModelForm):
    class Meta:
        model = Dosen 
        fields = '__all__'

        widgets = {
            'nip' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }