# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from t8 import views

urlpatterns = [
    # Your existing URL patterns
    path('', views.index_view, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
