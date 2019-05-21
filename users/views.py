import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'vidyaConnect.settings'
import django
django.setup()
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,redirect,render_to_response
from django.urls import reverse
from .forms import CustomUserCreationForm, ProfileForm, CustomUserCreationForm2
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser,Profile

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
"""def SignUp(request):
    form = CustomUserCreationForm()
    if request.POST:
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request,'signup.html',{'form': form})"""

def homeView(request):
        return render(request, 'home.html', {})
def home(request):
    return render(request, 'home.html', {})
def VChome(request):
    return render(request, 'VChome.html', {})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userLL = CustomUser.objects.get(username=username)
        last_login = userLL.last_login
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if last_login==None:
                    return HttpResponseRedirect(reverse("profile"))
                else:
                    return HttpResponseRedirect(reverse("VChome"))
        else:
            return render(request,'base.html')
    return render(request, 'login.html')

class LoginRedirectView(generic.View):
    def get(self, request, *args, **kwargs):
        obj=CustomUser.objects.get(username=self.request.user.username)
        flag=obj.flag
        print(flag)
        if flag == 'first':
            obj.flag='notFirst'
            obj.save()
            return HttpResponseRedirect(reverse("profile"))
        else:
            return HttpResponseRedirect(reverse("home"))

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile=profile_form.save(commit=False)
            profile.user=request.user
            profile.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'profile_form': profile_form
    })