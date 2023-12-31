
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name= 'refresh'),
    path('api/',include('registation.urls')),
    path('api/',include('agent.urls')),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
