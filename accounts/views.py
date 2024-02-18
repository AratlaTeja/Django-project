from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']    #Teja
        email = request.POST['email']          #teja123@gmail.com
        password1 = request.POST['password']   #teja.1234
        password2 = request.POST['password2']  #teja.1234

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username exists.....! try with another name')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('The email is already taken, Try another one')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()  # send the data to the database : Table : user
                    return redirect('login')
        else:
            print('Password did not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':    # if the condition is true it should enter into the if condition
        username = request.POST['username']   # teja
        password = request.POST['password']   # teja.1234

        user = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, user)
            print('Login Successfull..!')
            return redirect('showProducts')

        else:
            print('Invalid Credentials..!')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logout From Website..!')
        return redirect('login')