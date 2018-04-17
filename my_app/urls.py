from django.urls import path

from my_app.views import MicroService

urlpatterns = [
    path('', MicroService.as_view())
]