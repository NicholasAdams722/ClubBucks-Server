from django.db import models

class ItemTypes(models.Model):
    item_type = models.CharField(max_length=255)