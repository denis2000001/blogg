from django.db import models
from brands.models import Brand

POST_TYPE_CHOICES = (
    ('Mechanics', 'Mechanics'),
    ('Avomatick', 'Avomatick')
)


class Model(models.Model):
    name = models.CharField(max_length=20)
    engine = models.TextField(max_length=100)
    hp = models.IntegerField(null=True)
    nm = models.IntegerField(null=True)
    KPP = models.CharField(choices=POST_TYPE_CHOICES, max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)

def str(self):
    return self.name
