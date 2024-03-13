from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, sendEmail
from django.views import View
# Create your views here.

class IndexClass(View):
    def get(self,request):
        return HttpResponse('Hello, world')


    

class SaveNewsClass(View):
    def get(self,request):
        a= PostForm()
        return render(request, 'news/add_news.html',{'form': a}) 
    def post(self,request):
            g= PostForm(request.POST)
            if g.is_valid():
                g.save()
                return HttpResponse('Thanh cong')
            return HttpResponse('khong thanh cong')
    
def email_view(request):
    b= sendEmail()
    return render(request,'news/email.html', {'f':b} )
def receive(request):
    if request.method == 'POST':
        m = sendEmail(request.POST)
        if m.is_valid():
            title= m.cleaned_data['title']
            email = m.cleaned_data['email']
            content = m.cleaned_data['content']
            cc = m.cleaned_data['cc']
            return render(request,'news/print_email.html',{
                'title':title,
                'email':email,
                'content':content,
                'cc':cc,
            })
        return HttpResponse('failed')
    return HttpResponse('superfailed')