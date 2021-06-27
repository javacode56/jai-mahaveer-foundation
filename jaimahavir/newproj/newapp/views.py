from django.shortcuts import render,redirect
from django.http import HttpResponse
from newapp.forms import UserProfileInfoForm,UserForm,DonorProfileInfoForm
from newapp import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ( View,TemplateView,
                                    ListView, DetailView,
                                    CreateView, DeleteView,
                                    UpdateView)
from . import models

# Create your views here.

@login_required
def user_logout(request):
    #log out the user

    logout(request)

    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered=False
    if request.method=="POST":
        #get info from both forms it appears as one form to the user on .html page
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #save user form to database
            user=user_form.save()
            #hash password

            user.set_password(user.password)
            #upadte it with previous password
            user.save()

            #now we will with extra info!

            profile=profile_form.save(commit=False)

            #set on to one relationship between user form and userprofileinfo form
            profile.user=user

            #check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            #return redirect(reverse('payment:process'))
            registered=True

        else:
            print(user_form.errors,profile_form.errors)


    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    context={'user_form':user_form,'profile_form':profile_form,'registered':registered}

    return render(request,'newapp/register.html',context)


def index(request):
    return render(request,'newapp/index.html')

def user_login(request):
    if request.method=='POST':

        #first get the username and password supplied
        username=request.POST.get('username')
        password=request.POST.get('password')
        # django built-in authentication function:

        user=authenticate(username=username,password=password)

        if user:
            #check it is active account
            if user.is_active:
                #login the user in.
                login(request,user)
                #send user to index page
                #return HttpResponseRedirect('member_detail.html')
                return member_detail(request)
            else:
                #if account is not active
                return HttpResponse('your account is not active')
        else:
            print('some tried to login and failed')
            print("thet used username: {} and password: {}".format(username,password))
            return HttpResponse('invalid login deatils supplied')
    else:
        #nothing has been provided for username/password
        return render(request,'newapp/login.html',{})




def member_detail(request):
    return render(request,'newapp/member_detail.html')


def success_update(request):
    return render(request,'newapp/success_update.html')

class MemberUpadteView(UpdateView):
    fields=('address','amount','profile_pic')
    model=models.UserProfileInfo

    template_name = 'userprofileinfo_form.html'
    success_url = '/success_update/'








def donate(request):
    registered=False
    if request.method=="POST":
        #get info from both forms it appears as one form to the user on .html page

        profile_form=DonorProfileInfoForm(data=request.POST)

        if profile_form.is_valid():
            #save user form to database

            #hash password


            #upadte it with previous password


            #now we will with extra info!

            profile=profile_form.save()
            profile.save()
            #set on to one relationship between user form and userprofileinfo form


            #check if they provided a profile picture


            

            #return redirect(reverse('payment:process'))
            registered=True

        else:
            print(profile_form.errors)


    else:
        profile_form=DonorProfileInfoForm()

    context={'profile_form':profile_form,'registered':registered}

    return render(request,'newapp/donate.html',context)
