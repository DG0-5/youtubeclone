from django.shortcuts import render, redirect
from django.conf import settings 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm

User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method ==  'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, Your Account has been Created Successfully')
            new_user = authenticate(
                username=form.cleaned_data['email'], 
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'user/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, 'Invalid Email Address')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are Logged In!')
            return redirect('index')
        else:
            messages.warning(request, 'Invalid Username or Password')
            
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')