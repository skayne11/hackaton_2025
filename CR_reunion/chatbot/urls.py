# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ecrit/", views.chat_page_ecrit, name="chatbot_e"),
    path("vocal/", views.chat_page_vocal, name="chatbot_v"),
    path("file/", views.chat_page_file, name="file"),
]