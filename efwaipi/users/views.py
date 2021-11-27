from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
#only login user could see profile page
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #including encryption for the password
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users_act/register.html', {'form': form}) 

# @ is to add functionalities to a function
@login_required
def profile(request):
    return render(request, 'users_act/profile.html')

@login_required
def dashboard(request):
    return render(request, 'users_act/dashboard.html')
    
@login_required
def helpdesk(request):
    return render(request, 'users_act/helpdesk.html')

# def data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize
