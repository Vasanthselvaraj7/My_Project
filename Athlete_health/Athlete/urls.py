from django.urls import path
from . import views


urlpatterns = [
    path('athlete', views.athlete_dashboard, name='athlete'),
    path('accounts/login/signup', views.athlete_signup, name='signup'),
    path('accounts/login/', views.athlete_signin, name='signin'),
    path('logout', views.athlete_logout, name='logout')
]
