from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(blank=True, max_length=255)
    main_text = models.CharField(blank=True, max_length=1024)
    data = models.DateField(blank=True)