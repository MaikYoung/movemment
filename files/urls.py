from django.urls import path

from files.views import UploadFileAPIView

urlpatterns = [
    path('image', UploadFileAPIView.as_view()),
    ]