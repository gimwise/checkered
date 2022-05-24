from django import forms
from brands.models import Brand
from user.models import User

class RequestForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['admit']
        labels = {
            '수락 여부'
        }
