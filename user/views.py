from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm, FollowForm
from .models import *
from django.views import generic
from closets.models import Closet

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home/main.html'
    context_object_name = "closet_list"

    def get_queryset(self):
        return Closet.objects.filter(user = self.request.user)

class intro(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/intro.html')

class SignupView(generic.CreateView):
    template_name = 'user/signup.html'
    success_url = '/user/login/'
    form_class = UserForm

# class FollowCreateView(generic.View):
#     form_class = FollowForm
#     success_url = '/closets/ours'
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.user = self.request.user
#         obj.following = User.objects.get(admin=self.kwargs['pk'])
#         return super(FollowCreateView, self).form_valid(form)

class FollowView:
    def follow(request, pk):
        follow = User.objects.get(pk=pk)
        user = request.user

        if request.method == 'POST':
            try :
                mark = Follow()
                mark.user = user
                mark.following = follow
                mark.save()
            except:
                mark = Follow.objects.get(user=user, following=follow)
                mark.delete()
        return render(request, 'home/main.html')

class FollowerListView(generic.ListView):
    template_name = 'user/follower_list.html'
    context_object_name = "f_list"
    def get_queryset(self):
        return Follow.objects.filter(following = self.request.user)