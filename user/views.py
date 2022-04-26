from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@method_decorator(csrf_exempt)
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:main')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form' : form})
