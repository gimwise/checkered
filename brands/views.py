from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import BrandRequestForm, BrandInfoForm
from .models import Brand
# Create your views here.

class BrandAdmitCreateView(generic.CreateView):
    model = Brand
    context_object_name = 'brand'
    template_name = 'brands/request.html'
    success_url = '/main'
    form_class = BrandRequestForm

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

class BrandUpdateView(generic.UpdateView):
    model = Brand
    context_object_name = 'brand'
    form_class = BrandInfoForm
    template_name = 'brands/brand_info.html'
    success_url = '/main'

    def get_object(self):
        brand = Brand.objects.get(admin__username = self.kwargs['pk'])
        return brand

class BrandListView(generic.ListView):
    template_name = 'brands/brand_list.html'
    context_object_name = "brand_list"
    def get_queryset(self):
        return Brand.objects.filter(admit = True)