from django.db import models
from sorl.thumbnail import ImageField

class ImageFrame(models.Model):
    image = ImageField(upload_to='upload')
    
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)

    title = models.CharField(max_length=500)
    description = models.TextField(blank=True,null=True)
