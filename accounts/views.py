from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people = [
        {"name":"readul","email":"readul@gmail.com", "age":30},
        {"name":"akash", "email":"akash@gmail.com", 'age':40},
        {"name":"sagor", "email":"sagor@gmail.com", "age":60},
              ]
    
    return  render(request, "home/index.html",context= {"peoples":people})


def success_page(request):
    return HttpResponse("<h1>Hi, welcome to success page</h1>")