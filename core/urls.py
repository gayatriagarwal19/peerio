from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup', views.signup, name= 'signup'),  
    path('upload', views.upload, name= 'upload'),  
    path('settings', views.settings, name= 'settings'),  
    path('signin', views.signin, name= 'signin'),  
    # path('signin', views.signin, name= 'signin'),  
]

