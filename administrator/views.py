from django.shortcuts import render, get_object_or_404, redirect
from user.models import User
from closets.models import Closet, Category
from django.views import generic
from brands.models import Brand
from brands.forms import BrandRequestForm
from .forms import *
# Create your views here.

class brandListView(generic.ListView):
    template_name = 'admin/request_admit.html'
    context_object_name = "request_list"

    def get_queryset(self):
        return Brand.objects.all()

class BrandAdmitAcceptView(generic.UpdateView):
    model = Brand
    context_object_name = 'brand'
    form_class = RequestForm
    template_name = 'admin/accept.html'
    success_url = '/admin'

    def get_object(self):
        brand = Brand.objects.get(admin=self.kwargs['pk'])
        return brand

    def form_valid(self, form):
        form.instance.admit = True
        return super().form_valid(form)


class UserListView(generic.ListView):
    template_name = 'admin/user_list.html'
    context_object_name = "user_list"

    def get_queryset(self):
        return User.objects.filter(is_superuser = False)

class DeleteUserView(generic.DeleteView):
    model = User
    context_object_name = 'user'
    success_url = '/main'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

