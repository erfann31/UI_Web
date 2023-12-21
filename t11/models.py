from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.title


class Context(models.Model):
    # Represents a context column
    column_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Context - {self.column_id}"


class ContextItem(models.Model):
    # Represents individual items within each context column
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='context_images/')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title


class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    link = models.URLField()

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
