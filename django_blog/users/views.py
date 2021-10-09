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
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)  # user update form with actual user data
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES, #for image
                                instance=request.user.profile)#prfile update form with actual profile data

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated succesfully!")
            return redirect('profile') # use redirect to avoid message asking if you want to leave in browser
    else:
        u_form = UserUpdateform(instance=request.user)  # user update form with actual user data
        p_form = ProfileUpdateForm(instance=request.user.profile)  # profile update form with actual profile data

    context= {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html',context)