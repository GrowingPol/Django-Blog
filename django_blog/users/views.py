from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #save changes to database
            username = form.cleaned_data.get('username') #get username to post it in an alert
            messages.success(request, f'Your Account has been created!') #Account created feedback
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required #its used to demand a user
def profile(request):
    return render(request, 'users/profile.html')