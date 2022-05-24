from django import forms
from .models import Brand
from user.models import User

class BrandRequestForm(forms.ModelForm):
    class Meta :
        model = Brand
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(BrandRequestForm, self).__init__(*args, **kwargs)

class BrandInfoForm(forms.ModelForm):
    class Meta :
        model = Brand
        fields = ['site', 'photo', 'description']