import builtins
import sys
import django
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("จารุวิทย์ คำพันธ์ 66114540131")

def request_info_view(request):
    print("=== HttpRequest Information ===")
    print(f"Method: {request.method}")
    print(f"Path: {request.path}")
    print(f"Full Path: {request.get_full_path()}")
    print(f"Scheme: {request.scheme}")
    print(f"Host: {request.get_host()}")
    print(f"User Agent: {request.META.get('HTTP_USER_AGENT', '')}")
    print(f"Remote Address: {request.META.get('REMOTE_ADDR')}")
    print(f"GET Parameters: {request.GET}")
    print(f"POST Data: {request.POST}")
    print(f"Cookies: {request.COOKIES}")
    print(f"Headers:")
    for header, value in request.headers.items():
        print(f"  {header}: {value}")
        return HttpResponse("HttpRequest information printed to console.")

def hello_view(request):
    if request.method == "GET":
        name = request.GET.get('name', 'Guest')
        return HttpResponse(f"สวัสดี, {name}!")
    else:
        return HttpResponse("โปรดใช้วิธี GET ในการร้องขอข้อมูล")
    
def info_view(request):
    python_version = sys.version.split()[0]
    django_version = django.get_version()
    message = f"Python version: {python_version}<br>Django version: {django_version}"
    return HttpResponse(message)
    
def hello(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        
        print(f"ชื่อ: {name}")
        print(f"อีเมล: {email}")
        
        return HttpResponse(f"helo {name}, ขอบคุณที่ส่งข้อมูลของคุณ!")
    
    return render(request, "myapp/form.html")

def test_post(request):
    return render(request, "myapp/test.html")  # แสดงฟอร์ม HTML สำหรับการกรอกข้อมูล