from django.urls import path
from .views import brand

urlpatterns = [
    path('', brand, name='index'),
]


from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("single/", views.single_page, name="single"),
    path("contact/", views.contact, name="contact"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

