# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# from t8 import views as t8_views
from t9 import views as t9_views
from t10 import views as t10_views

urlpatterns = [
    # Your existing URL patterns
    path('', t10_views.main_view, name='index'),
    path('search/', t10_views.search_view, name='search'),
    path('admin/', admin.site.urls),
    # path('atashfeshan/', t8_views.atashfeshan_view, name='atashfeshan'),
    path('create_data/', t9_views.create_data, name='create_data'),
    path('2/', t9_views.get_political_news, name='2'),
    path('3/', t9_views.get_filtered_journalists, name='3'),
    path('4/', t9_views.get_news_by_keyword, name='4'),
    path('5/', t9_views.update_short_titles, name='5'),
    path('6/', t9_views.delete_sports_2014_news, name='6'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
