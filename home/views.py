from django.utils.decorators import decorator_from_middleware
from django.shortcuts import render
from .mymiddleware import SimpleMiddleware
def index(request):
    print('view is running')
    return render(request,'index.html')
@decorator_from_middleware(SimpleMiddleware)
def getdata(request):
    print('getdata view is running')
    return render(request,'index1.html')
