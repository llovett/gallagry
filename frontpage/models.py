from django.db import models

class GalleryLinkPosition(models.Model):
    pos_x = models.IntegerField(default=0, verbose_name="X Position")
    pos_y = models.IntegerField(default=0, verbose_name="Y Position")
    rotation = models.DecimalField(max_digits=8,decimal_places=5, default=0, verbose_name="Rotation")
    is_default = models.BooleanField(default=True, verbose_name="Make this the default gallery link position")

    def save(self):
        if self.is_default:
            for other in GalleryLinkPosition.objects.exclude(id=self.id):
                other.is_default = False
                other.save()
        super(GalleryLinkPosition, self).save()

    def __unicode__(self):
        return "gallery at (%d,%d) rotated %f"%(self.pos_x,self.pos_y,self.rotation)

class BlogLinkPosition(models.Model):
    pos_x = models.IntegerField(default=0, verbose_name="X Position")
    pos_y = models.IntegerField(default=0, verbose_name="Y Position")
    rotation = models.DecimalField(max_digits=8,decimal_places=5, default=0, verbose_name="Rotation")
    is_default = models.BooleanField(default=True, verbose_name="Make this the default blog link position")

    def save(self):
        if self.is_default:
            for other in BlogLinkPosition.objects.exclude(id=self.id):
                other.is_default = False
                other.save()
        super(BlogLinkPosition, self).save()

    def __unicode__(self):
        return "blog at (%d,%d) rotated %f"%(self.pos_x,self.pos_y,self.rotation)
