from django.shortcuts import render, get_object_or_404, redirect
from user.models import User
from closets.models import Closet, Category
from django.views import generic
from .models import Closet
from .forms import *
from django.db.models import Q

# Create your views here.

class DetailView(generic.DetailView):
    template_name = 'closets/detail.html'
    queryset = Closet.objects.all()
    context_object_name = 'closet'

class userListView(generic.ListView):
    template_name = 'closets/user_list.html'
    context_object_name = "user_list"
    def get_queryset(self):
        return User.objects.filter(~Q(id = self.request.user.id), auth = 0, is_superuser = False)

def otherCloset(request, pk):
    closet = Closet.objects.filter(user_id = pk)
    context={'closet' : closet}
    return render(request, 'closets/other_closet.html', context)

class closetUpdateView(generic.UpdateView):
    model = Closet
    context_object_name = 'closet'
    form_class = ClosetForm
    template_name = 'closets/closet_update.html'
    success_url = '/main'

    def get_object(self):
        closet = get_object_or_404(Closet, pk=self.kwargs['pk'])
        return closet

class ClosetCreateView(generic.CreateView):
    model = Closet
    context_object_name = 'closet'
    template_name = 'closets/closet_new.html'
    success_url = '/main'
    form_class = ClosetForm

    def get_form_kwargs(self):
        kwargs = super(ClosetCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user # pass the 'user' in kwargs
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class deleteClosetView(generic.DeleteView):
    model = Closet
    context_object_name = 'c'
    success_url = '/main'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class categoryListView(generic.ListView):
    template_name = 'closets/view_category.html'
    context_object_name = "category_list"
    def get_queryset(self):
        return Category.objects.filter(user_id = self.request.user)

class deleteCategoryView(generic.DeleteView):
    model = Category
    context_object_name = 'c'
    success_url = '/main'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CategoryCreateView(generic.CreateView):
    model = Category
    context_object_name = 'category'
    template_name = 'closets/create_category.html'
    success_url = '/closets/category'
    form_class = CategoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)