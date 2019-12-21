from django import  forms

from . models import Absen

class AbsenForm(forms.ModelForm):
    class Meta:
        model = Absen
        fields = [
            'nama_depan',
            'nama_belakang',
            'kelas',
            'jurusan',
            'alamat',
        ]

        widgets = {
            'nama_depan': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'masukan nama depan',
            }),

            'nama_belakang': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'masukan nama belakang',
            }),

            'kelas': forms.Select(attrs={
                'class':'form-control',

            }),

            'jurusan': forms.Select(attrs={
                'class':'form-control',
            }),

            'alamat': forms.Textarea(attrs={
                'class':'form-control',
                'paleholder':'masukan alamat',
            }),
        }
