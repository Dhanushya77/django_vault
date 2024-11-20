from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login),
    path('user_logout',views.user_logout),
    path('register',views.register),
    path('vault',views.vault),
    path('add_files/<id>',views.add_files),
    path('delete_file',views.delete_file),
    
    
]