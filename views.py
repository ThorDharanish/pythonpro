from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
 return render(request, "home.html", {})


def services_view(request):
    return render(request, 'registration/index.html')

def contact_us(request):
    return render(request, 'registration/contactus.html')

def about_us(request):
    return render(request, 'registration/aboutus.html')

def f_us(request):
    return render(request, 'registration/f.html')


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})