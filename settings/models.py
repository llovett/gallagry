from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from colorful.fields import RGBColorField
from django.core.files.base import ContentFile
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
        if self.use_for_mainpage or self.use_for_galleries or self.use_for_blog:
            other_schemes = ColorScheme.objects.exclude(id=self.id)
            for scheme in other_schemes:
                if self.use_for_mainpage:
                    scheme.use_for_mainpage = False
                if self.use_for_blog:
                    scheme.use_for_blog = False
                if self.use_for_galleries:
                    scheme.use_for_galleries = False
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
        if self.use_for_blog:
            others = BackgroundImage.objects.filter(use_for_blog=True).exclude(id=self.id)
            for o in others:
                o.use_for_blog = False
                o.save()
        if self.use_for_galleries:
            others = BackgroundImage.objects.filter(use_for_galleries=True).exclude(id=self.id)
            for o in others:
                o.use_for_galleries = False
                o.save()
        if self.use_for_mainpage:
            others = BackgroundImage.objects.filter(use_for_mainpage=True).exclude(id=self.id)
            for o in others:
                o.use_for_mainpage = False
                o.save()

        old_bgimage = self.background_image
        super(BackgroundImage,self).save()
        if old_bgimage != self.background_image:
            # Make a sane version of the background image, for display as background
            # TODO: is there a more efficient way of doing this, instead of saving two HUGE
            # images to disk, and storing one of them entirely in memory for awhile?
            sane_image = get_thumbnail(self.background_image,
                                       "2880x1800",
                                       upscale=False,
                                       progressive=True,
                                       quality=50)
            self.background_image.save(sane_image.name, ContentFile(sane_image.read()), True)
            super(BackgroundImage,self).save()
