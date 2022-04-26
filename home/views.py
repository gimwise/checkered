from django.shortcuts import render
from closets.models import Closet, Category

# Create your views here.

def main(request) :
    current_user = request.user.id
    closet_list = Closet.objects.filter(id=current_user)
    context = {'closet_list' : closet_list}
    return render(request, 'home/main.html', context)

def intro(request) :
    return render(request, 'home/intro.html')
