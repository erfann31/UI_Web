# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from t8 import views

urlpatterns = [
    # Your existing URL patterns
    path('', views.main_view, name='index'),
    path('atashfeshan/', views.atashfeshan_view, name='atashfeshan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
