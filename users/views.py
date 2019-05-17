import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'vidyaConnect.settings'
import django
django.setup()
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.urls import reverse
from .forms import CustomUserCreationForm, NameForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def homeView(request):
    if request.method=='POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("VChome"))
        else:
            print(form.errors)
            #return render(request, 'home2.html',{})
    else:
        form = NameForm()
        return render(request, 'home.html', {'form': form})
def VChome(request):
    return render(request, 'base.html', {})