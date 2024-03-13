from django.urls import path
from .views import IndexClass,LoginClass,ViewUser,view_product

urlpatterns = [
    path("",IndexClass.as_view(), name='login.index'),
    path("log/",LoginClass.as_view(), name='login.index'),
    path("user-view/",ViewUser.as_view(), name='userview'),
    path("product-view/",view_product, name='product-view'),
    
    
    
    
    
    
]