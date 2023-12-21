from django.db import models


class Ad(models.Model):
    image_path = models.CharField(max_length=200)

    def __str__(self):
        return self.image_path


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    onclick_function = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title


from django.db import models


class ContextColumn(models.Model):
    column_id = models.CharField(max_length=50)

    def __str__(self):
        return self.column_id


class NavButton(models.Model):
    column = models.ForeignKey(ContextColumn, on_delete=models.CASCADE, related_name='buttons')
    button_id = models.CharField(max_length=50)
    button_text = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    onclick_function = models.CharField(max_length=100)

    def __str__(self):
        return self.button_text


class Context(models.Model):
    column = models.ForeignKey(ContextColumn, on_delete=models.CASCADE, related_name='contexts')
    context_id = models.CharField(max_length=50)
    display_style = models.CharField(max_length=20, default='none')

    def __str__(self):
        return self.context_id


class Box(models.Model):
    context = models.ForeignKey(Context, on_delete=models.CASCADE, related_name='boxes')
    box_type = models.CharField(max_length=20)  # 'circularImage', 'triangleImage', or 'onlyTextBox'
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.box_type + self.text


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
