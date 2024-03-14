from django.urls import path
from .views import IndexClass,LoginClass,ViewUser,view_product,Addpost

app_name = 'Login'
urlpatterns = [
    path("",IndexClass.as_view(), name='login.index'),
    path("log/",LoginClass.as_view(), name='login.index'),
    path("user-view/",ViewUser.as_view(), name='userview'),
    path("product-view/",view_product, name='product-view'),
    path("add-post/",Addpost.as_view(), name='add-post'),
    
    
    
    
    
    
]