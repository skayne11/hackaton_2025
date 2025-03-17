# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat_response, name="chatbot"),
    path("upload_file/", views.upload_txt_file, name="upload_file"),
]