from django.db import models
from sorl.thumbnail import ImageField
from colorful.fields import RGBColorField
import datetime

class ColorScheme(models.Model):
    title = models.CharField(max_length=200, default="Color scheme from %s"%datetime.datetime.now().strftime("%d/%m/%Y at %I:%M %p"))
    background_color = RGBColorField(verbose_name="Background color")
    foreground_color = RGBColorField(verbose_name="Foreground color")
    link_color = RGBColorField(verbose_name="Normal link color")
    rollover_color = RGBColorField(verbose_name="Rollover link color")
    use_for_mainpage = models.BooleanField(default=True, verbose_name="Use this on the main page")
    use_for_galleries = models.BooleanField(default=True, verbose_name="Use this on gallery pages")
    use_for_blog = models.BooleanField(default=True, verbose_name="Use this on blog pages")

    def __unicode__(self):
        return self.title

    def save(self):
        if self.use_for_mainpage:
            other_schemes = ColorScheme.objects.exclude(id=self.id)
            for scheme in other_schemes:
                scheme.use_for_mainpage = False
                scheme.save()
        if self.use_for_galleries:
            other_schemes = ColorScheme.objects.exclude(id=self.id)
            for scheme in other_schemes:
                scheme.use_for_galleries = False
                scheme.save()
        if self.use_for_blog:
            other_schemes = ColorScheme.objects.exclude(id=self.id)
            for scheme in other_schemes:
                scheme.use_for_blog = False
                scheme.save()
        super(ColorScheme,self).save()

class BackgroundImage(models.Model):
    background_image = models.ImageField(upload_to='images',width_field='full_width',height_field='full_height')
    use_for_mainpage = models.BooleanField(default=True, verbose_name="Use this on the main page")
    use_for_galleries = models.BooleanField(default=True, verbose_name="Use this on galleries page")
    use_for_blog = models.BooleanField(default=True, verbose_name="Use this on blog pages")
    full_width = models.IntegerField(default=0,editable=False)
    full_height = models.IntegerField(default=0,editable=False)
    title = models.CharField(max_length=500,blank=True,null=True)

    def __unicode__(self):
        return self.title if self.title else self.background_image.name

    def save(self):
        if self.use_for_mainpage:
            other_imgs = BackgroundImage.objects.exclude(id=self.id)
            for img in other_imgs:
                img.use_for_mainpage = False
                img.save()
        if self.use_for_galleries:
            other_imgs = BackgroundImage.objects.exclude(id=self.id)
            for img in other_imgs:
                img.use_for_galleries = False
                img.save()
        if self.use_for_blog:
            other_imgs = BackgroundImage.objects.exclude(id=self.id)
            for img in other_imgs:
                img.use_for_blog = False
                img.save()
        super(BackgroundImage,self).save()
