from django.conf import settings
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("uuid/", include(("cowrywise.sample_app.urls", "sample_app"), namespace='sample_app'))
]
