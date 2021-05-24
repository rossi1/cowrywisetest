from django.urls import path

from . import views as sample_app_views

urlpatterns = [
    path("", sample_app_views.UUIDAPIView.as_view(), name="uuid_list")
]
