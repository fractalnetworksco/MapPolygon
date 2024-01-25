from django.contrib.gis.db import models as gis_models
from fractal_database.models import ReplicatedModel

# Create your models here.

"""
class Polygon(models.Model):
    polygon=gis_models.PolygonField()

class CustomerPolygon(models.Model):
    polygon=models.ForeignKey(Polygon,on_delete=models.CASCADE,blank=True,null=True)
    customer=models.ManyToManyField(Customer)
"""


class ServiceArea(ReplicatedModel):
    polygon = gis_models.PolygonField()
