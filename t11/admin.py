from django.contrib import admin

from t11.models import NewsItem, MenuItem, CarouselItem, Context, NewsCategory, ContextColumn, Box, NavButton

# Register your models here.
admin.site.register(NewsItem)
admin.site.register(MenuItem)
admin.site.register(ContextColumn)
admin.site.register(Box)
admin.site.register(NavButton)
admin.site.register(CarouselItem)
admin.site.register(Context)
admin.site.register(NewsCategory)
