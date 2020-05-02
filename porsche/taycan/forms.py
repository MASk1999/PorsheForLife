from django import forms
from .models import owners

class car_registration(forms.Form):
    chass_num = forms.CharField(max_length=20, label='Chassis Number')
    car_model = forms.CharField(max_length=10, label='Car Model')
    color = forms.CharField(max_length=10, label='Colour')

class owner_registration(forms.ModelForm):

    class Meta:
        model = owners
        fields = ['name', 'gender', 'phone', 'address', 'email', 'car_owned']    
