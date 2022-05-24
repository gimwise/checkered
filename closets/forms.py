from django import forms
from .models import Closet, Category
from user.models import User

class ClosetForm(forms.ModelForm):

    class Meta:
        model = Closet
        fields = ['cname', 'photo', 'detail', 'category', ]
        labels ={
            'cname' : '이름',
            'photo' : '사진',
            'detail' : '부가 정보',
            'category' : '카테고리',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) # pop the 'user' from kwargs dictionary
        super(ClosetForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user))

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']
        labels = {
            'category_name' : '카테고리 이름',
            'description' : '설명',
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args,**kwargs)