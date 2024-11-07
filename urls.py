from django.urls import path, include
from .views import authView, home, services_view,contact_us,about_us,f_us

urlpatterns = [
    path('f/', f_us, name='f'),
    path('aboutus/', about_us, name='aboutus'),
 path('contactus/', contact_us, name='contactus'),
 path('services/', services_view, name='services'),
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
]