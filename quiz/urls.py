from django.urls import path
from . import views
from quiz.views import get_question, create_question,test_post,home

urlpatterns = [
    path('', views.home, name='home'),
    path('question', views.get_question),
    path('question/create', views.create_question, name='create_question'),
    path('question/TestPost', views.test_post),

]
