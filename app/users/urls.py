from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', csrf_exempt(RegisterView.as_view())),
    path('login', csrf_exempt(LoginView.as_view())),
    path('user', csrf_exempt(UserView.as_view())),
    path('logout', csrf_exempt(LogoutView.as_view())),
]
