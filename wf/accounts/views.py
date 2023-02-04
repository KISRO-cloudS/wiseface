from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistrationForm



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
           
            form.save() 
            messages.success(request, f'registration successful.')
            return redirect('login')
    else:
    
        form = UserRegistrationForm()
       

    context = {'form': form,

    }
    return render(request, 'accounts/register.html', context)


def logout(request):
	return render(request,'accounts/logout.html', {})




