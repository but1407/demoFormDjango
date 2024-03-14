from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.

from django.views import  View

class IndexClass(View):
    def get(self, request):
        return HttpResponse("<h1>Xin chao</h1>")
class LoginClass(View):
    def get(self, request):
        return render(request,  'login/login.html' )
    def post(self,request):
        user_name = request.POST.get('username')
        matkhau = request.POST.get('password')
        my_user = authenticate(username=user_name, password=matkhau)
        if my_user is None:
            return HttpResponse("Khong ton tai tai khoan")
        login(request,my_user)
        return redirect('/admin/')
class ViewUser(LoginRequiredMixin,View):
    login_url='/login/log/'
    def get(self,request):
        return HttpResponse('Day la  User')
    def post(self,request):
        pass
@decorators.login_required(login_url='/login/log/')
def view_product(request):
    return HttpResponse('Xem san pham')

class Addpost(LoginRequiredMixin,View):
    login_url='/login/log/'
    def get(self,request):
        f = PostForm
        return render(request, 'login/add_post.html',{'form':f})
    def post(self,request):
        f= PostForm(request.POST)
        
        if not f.is_valid():
            return HttpResponse('nhap sai du lieu')
        print(request.user.get_all_permissions())
        if not request.user.has_perm('login.add_post'):
            f.save()
            return HttpResponse('OK')
        return HttpResponse('ban khong co quyen')
        