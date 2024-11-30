from django.urls import path
from .views import index,chat_response

urlpatterns = [
    path('', index, name='index'),
    path('response/', chat_response, name='response'),
]
