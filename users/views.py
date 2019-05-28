import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'vidyaConnect.settings'
import django
django.setup()
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, logout
from .models import CustomUser,Profile, Subscription
from django.contrib.auth.views import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.decorators.cache import never_cache
from django.views.generic import UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import SubscriptionForm

import dns.resolver
import socket
import smtplib

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        username = request.POST['username']
        if len(username)<6:
            messages.error(request, 'Username should be minimum 6 characters')
            return redirect('signup')
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            if email_verify(to_email):
                return HttpResponse('<h3>Please confirm your email address to complete the registration</h3>')
            else:
                messages.error(request, 'Email address doesn\'t exist')
                return redirect('signup')
    else:
        form = CustomUserCreationForm
    return render(request, 'signup.html', {'form': form})

def email_verify(to_email):
    #MS record for target domain in order to start email verification process
    records = dns.resolver.query('emailhippo.com', 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    #verifying email
    host = socket.gethostname() #Get local server hostname
    server = smtplib.SMTP() #SMTP lib setup (use debug level for full output)
    server.set_debuglevel(0)

    server.connect(mxRecord)# SMTP Conversation
    server.helo(host)
    server.mail('vanithakunta29@gmail.com')
    code, message = server.rcpt(str(to_email))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        return True
    else:
        return False

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

"""class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'"""

def homeView(request):
        return render(request, 'home.html', {})
def home(request):
    if request.method=="POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SubscriptionForm()
        return render(request, 'home.html', {'form': form})

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
            """messages.success(request,_('Incorrect username or password'))
            return render(request,'base.html')
            messages.add_message(request, messages.SUCCESS, 'Incorrect username or password')"""
            messages.error(request, 'Invalid login')
            return redirect('login')
            #return render(request, 'login.html')
    return render(request, 'login.html')

class LoginRedirectView(generic.View):
    def get(self, request, *args, **kwargs):
        obj = CustomUser.objects.get(username=self.request.user.username)
        flag = obj.flag
        print(flag)
        if flag == 'first':
            obj.flag = 'notFirst'
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
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'profile_form': profile_form
    })
class SubscriptionView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    form_class = SubscriptionForm
    template_name = 'subscribe.html'
    success_message = 'You are now subscribed!'
    success_url = reverse_lazy('home')
