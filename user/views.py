from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login

from user.forms import MyUserCreationForm

def register(request):

    if request.method == 'GET':
        form = MyUserCreationForm()
        context = {
            'form':form
        }
        return render(request, 'user/register.html', context)
    
    else:

        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse('blog_index'))
