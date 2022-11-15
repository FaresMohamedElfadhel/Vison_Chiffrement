from django import forms
from . import models
class ChiffrementForm(forms.ModelForm):
    class Meta:
        model=models.Chiffrement
        fields=['image_source','image_txt','image_chiffree','txt','width_txt','height_txt','height_source','width_source']
        # widgets = {
        #     'image_source': forms.TextInput(attrs={'class': 'form-control'}),
        #     'image_txt': forms.DateInput(attrs={'class': 'form-control'}),
        #     'image_chiffree': forms.DateInput(attrs={'class': 'form-control'}),
        # }