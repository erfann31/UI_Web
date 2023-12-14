from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.db import models


class Reporter(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(1000), MaxValueValidator(5000)])
    dateOfemp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        email_validator = EmailValidator()
        email_validator(self.email)
        if not (1000 <= self.salary <= 5000):
            raise ValidationError("Salary must be between 1,000 and 5,000.")


class News(models.Model):
    CATEGORY_CHOICES = [
        ('economic', 'Economic'),
        ('political', 'Political'),
        ('cultural', 'Cultural'),
        ('sports', 'Sports'),
    ]

    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    short_content = models.TextField()
    content = models.TextField()
    dateOfcreate = models.DateTimeField(auto_now_add=True)
