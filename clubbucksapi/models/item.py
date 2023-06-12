from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.ForeignKey('ItemTypes', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images')
    quantity = models.IntegerField()