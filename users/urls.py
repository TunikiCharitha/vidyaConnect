from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/home/',views.home, name='home'),
    path('profile/',views.update_profile,name='profile'),
    path('VChome/',views.VChome, name='VChome'),
    #path('login/',views.login, name='login'),
    #path('users/login/', views.login_user, name='login'),
    path('login/done/', views.LoginRedirectView.as_view(), name='login_redirect'),
    #path('signup/signup2/', views.signup2.as_view(), name='signup2'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
]