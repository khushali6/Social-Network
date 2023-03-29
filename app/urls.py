from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),  
    path('connection',views.connection,name='connection'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('profile',views.profile,name='profile'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    

    
]
