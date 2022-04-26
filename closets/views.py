from django.shortcuts import render
from user.models import User

# Create your views here.

def closet_list(request):
    user_list = User.objects.filter(auth=0)
    current_user = request.user
    context = {'user_list' : user_list,
               'current_user' : current_user
               }
    return render(request, 'closets/closet_list.html', context)