from django.db import models
from sorl.thumbnail import ImageField

class ImageFrame(models.Model):
    image = ImageField(upload_to='images')
    
    pos_x = models.IntegerField(default=0, verbose_name="X Position")
    pos_y = models.IntegerField(default=0, verbose_name="Y Position")
    width = models.IntegerField(default=100, verbose_name="Width")
    height = models.IntegerField(default=100, verbose_name="Height")
    geometry = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0, verbose_name="Price")
    visible = models.BooleanField(default=True, verbose_name="Visible")

    title = models.CharField(max_length=500, verbose_name="Title")
    description = models.TextField(blank=True,null=True, verbose_name="Description")

    def __unicode__(self):
        return self.title if not self.description else "%s - %s..."%(self.title,self.description[:100])

    def save(self):
        self.geometry = "%dx%d"%(self.width,self.height)
        super(ImageFrame,self).save()
