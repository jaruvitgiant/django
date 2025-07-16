from django.contrib import admin
from django.urls import path ,include
from . import views
from myapp.views import home ,request_info_view ,hello_view, info_view,hello,test_post

urlpatterns = [
    path('',views.home),
    path('info',views.info_view),
    path('hello-viwe',views.hello_view),
    path('hello',views.hello),
    path('test-post',views.test_post),
    # path('quiz', include('quiz.urls')),
    
    ]