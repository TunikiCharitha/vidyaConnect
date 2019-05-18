from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/home/',views.home, name='home'),
    path('profile/',views.update_profile,name='profile'),
    #path('users/login/', views.login_user, name='login'),
    path('login/done/', views.LoginRedirectView.as_view(), name='login_redirect'),
    #path('signup/signup2/', views.signup2.as_view(), name='signup2'),
]