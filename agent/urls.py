from django.urls import path
from .views import agentview


urlpatterns = [
    
    path('agent/', agentview.as_view(), name='agent'),
]