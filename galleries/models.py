from django.db import models
from sorl.thumbnail import ImageField

class Image(models.Model):
    image = ImageField(upload_to='images')
    gallery = models.ForeignKey('Gallery', verbose_name="Gallery")
    
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0, verbose_name="Price")
    visible = models.BooleanField(default=True, verbose_name="Visible")
    for_sale = models.BooleanField(default=True, verbose_name="For sale")

    title = models.CharField(max_length=500, verbose_name="Title")
    description = models.TextField(blank=True,null=True, verbose_name="Description")

    def __unicode__(self):
        return self.title if not self.description else "%s - %s..."%(self.title,self.description[:100])

class Gallery(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    preview_image = ImageField(upload_to='images', verbose_name="Thumbnail", blank=True, null=True)
    description = models.TextField(blank=True,null=True, verbose_name="Description")
    background_image = models.ForeignKey('settings.BackgroundImage', verbose_name="Background image", blank=True, null=True)
    colorscheme = models.ForeignKey('settings.ColorScheme', verbose_name="Color scheme", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Galleries"

    def __unicode__(self):
        return self.title
