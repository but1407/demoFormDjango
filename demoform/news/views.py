from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, sendEmail
# Create your views here.


def index(request):
    return HttpResponse('Hello, world')
def add_post(request):
    a= PostForm()
    return render(request, 'news/add_news.html',{'form': a}) 

def save_news(request):
    if request.method == 'POST':
        g= PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Thanh cong')
        return HttpResponse('khong thanh cong')
    return HttpResponse('khong phai post request')
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