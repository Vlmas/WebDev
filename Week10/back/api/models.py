from django.db import models

class ProductItem(models.Model):
    name = models.CharField(max_length=96)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=512, default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
        }
    
class Category(models.Model):
    name = models.CharField(max_length=96)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }