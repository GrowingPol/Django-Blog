from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm,UserUpdateform,ProfileUpdateForm
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
    u_form = UserUpdateform()#user update form
    p_form = ProfileUpdateForm()#profile update form

    context= {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html',context)