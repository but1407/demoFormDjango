from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexClass.as_view(), name='index' ),
    path("save/", views.SaveNewsClass.as_view(), name='save_post'),
    path("email/", views.email_view, name='email'),
    path("receive/", views.receive, name='receive'),
    
    
    
]