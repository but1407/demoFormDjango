from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index' ),
    path("add/", views.add_post, name='add_post'),
    path("save/", views.save_news, name='save_post'),
    path("email/", views.email_view, name='email'),
    path("receive/", views.receive, name='receive'),
    
    
    
]