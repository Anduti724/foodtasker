from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from coreapp.forms import UserForm ,RestorantForm

from django.contrib.auth import authenticate ,login 
from django.contrib.auth.models import User

# Create your views here.
def home (request):
    return redirect(restorant_home)
@login_required(login_url=('/restorant/sign_in/'))
def restorant_home (request):
    return render(request ,'restorant/home.html',{})
def restorant_sign_up (request):

    user_form=UserForm()
    restorant_form=RestorantForm()
    if request.method=="POST":
        user_form=UserForm(request.POST)
        restorant_form=RestorantForm(request.POST, request.FILES)
        if user_form.is_valid()and restorant_form.is_valid():
            new_user=User.objects.create_user(**user_form.cleaned_data)
            new_restorant=restorant_form.save(commit=False)
            new_restorant.user=new_user
            new_restorant.save()
            login(request,authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]

                
            ))
            return redirect(restorant_home)
            

    return render(request ,'restorant/sign_up.html',
    {
        "user_form":user_form,
    "restorant_form":restorant_form}
    )

