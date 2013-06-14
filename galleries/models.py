from django.db import models
from sorl.thumbnail import ImageField

class Image(models.Model):
    image = ImageField(upload_to='images')
    gallery = models.ForeignKey('Gallery', verbose_name="Gallery")
    use_as_preview = models.BooleanField(default=True, verbose_name="Use this image as a preview for the gallery")
    
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0, verbose_name="Price")
    visible = models.BooleanField(default=True, verbose_name="Visible")
    for_sale = models.BooleanField(default=True, verbose_name="For sale")

    title = models.CharField(max_length=500, verbose_name="Title")
    description = models.TextField(blank=True,null=True, verbose_name="Description")

    def __unicode__(self):
        return self.title if not self.description else "%s - %s..."%(self.title,self.description[:100])

    def save(self):
        if self.use_as_preview:
            other_imgs = Image.objects.exclude(id=self.id)
            for img in other_imgs:
                img.use_as_preview = False
                img.save()
        super(Image,self).save()

class Gallery(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    description = models.TextField(blank=True,null=True, verbose_name="Description")

    def __unicode__(self):
        return self.title
