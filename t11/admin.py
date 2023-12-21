from django.contrib import admin

from t11.models import NewsItem, MenuItem, ContextItem, CarouselItem, Context, NewsCategory

# Register your models here.
admin.site.register(NewsItem)
admin.site.register(MenuItem)
admin.site.register(ContextItem)
admin.site.register(CarouselItem)
admin.site.register(Context)
admin.site.register(NewsCategory)
