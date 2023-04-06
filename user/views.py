from django.shortcuts import render

# Create your views here.


from django.shortcuts import  render, redirect
from .form import NewUserForm
from django.contrib.auth import login 
from django.contrib import messages

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("register_page")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


from django.shortcuts import  render, redirect
from .form import NewUserForm
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # admin
            password = form.cleaned_data.get('password') # admin
            user = authenticate(username=username, password=password) # returns user object
            print(user, user.__dict__)
            if user:
                login(request, user) # database save
                return redirect("login_request")
            else:
                return redirect("home_page")
        else:
            return redirect("login_request")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    return redirect("login_request")
