from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from accounts.models import CustomUser
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        age = request.POST.get('age')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password1 == password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken.')
            else:
                # Correct way to create a CustomUser
                user = CustomUser.objects.create(username=fullname, email=email, phone_number=phone_number, age=age)
                user.set_password(password1)  # Set the user's password correctly
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Attempt to get the user by email
            user = CustomUser.objects.get(email=email)

            # Use the standard authenticate function with username and password
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/')  # Replace 'home' with the appropriate URL name for the home page
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
                return render(request, 'login.html')
        except ObjectDoesNotExist:
            messages.error(request, 'User does not exist')

    return render(request, 'login.html')

def custom_logout(request):
    auth.logout(request)
    return redirect("/")