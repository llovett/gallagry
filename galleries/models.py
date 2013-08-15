from django.db import models
from sorl.thumbnail import ImageField
from paypal.standard.ipn.signals import payment_was_successful
from galleries.utils import slugify

class Image(models.Model):
    image = ImageField(upload_to='images')
    gallery = models.ForeignKey('Gallery', verbose_name="Gallery")
    
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0, verbose_name="Price")
    visible = models.BooleanField(default=True, verbose_name="Visible")
    for_sale = models.BooleanField(default=True, verbose_name="For sale")
    sold = models.BooleanField(default=False, verbose_name="Sold")

    title = models.CharField(max_length=255, verbose_name="Title", unique=True)
    title_slug = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True,null=True, verbose_name="Description")

    def __unicode__(self):
        return self.title if not self.description else "%s - %s..."%(self.title,self.description[:100])

    def save(self):
        self.title_slug = slugify(self.title)
        super(Image, self).save()

class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title", unique=True)
    title_slug = models.CharField(max_length=255, unique=True, null=True)
    preview_image = ImageField(upload_to='images', verbose_name="Thumbnail", blank=True, null=True)
    description = models.TextField(blank=True,null=True, verbose_name="Description")
    background_image = models.ForeignKey('settings.BackgroundImage', verbose_name="Background image", blank=True, null=True)
    colorscheme = models.ForeignKey('settings.ColorScheme', verbose_name="Color scheme", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Galleries"

    def __unicode__(self):
        return self.title

    def save(self):
        self.title_slug = slugify(self.title)
        super(Gallery, self).save()

def payment_complete(sender, **kwargs):
    ipn_obj = sender
    image_id = int(ipn_obj.item_number)
    
    try:
        image = Image.objects.get(id=image_id)
        image.for_sale = False
        image.sold = True
        image.save()
    except Image.DoesNotExist:
        pass

payment_was_successful.connect(payment_complete)
