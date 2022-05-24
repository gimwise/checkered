from django.shortcuts import render
from closets.models import Closet, Category
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home/main.html'
    context_object_name = "closet_list"

    def get_queryset(self):
        return Closet.objects.filter(user = self.request.user)

def intro(request) :
    return render(request, 'home/intro.html')

def detail(request, closet_id):
    closet = Closet.objects.get(id = closet_id)
    context={'closet' : closet}
    return render(request, 'closets/detail.html', context)

