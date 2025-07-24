from django.db import models

class ProductReview(models.Model):
    video_url = models.URLField()
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)

    aff_link_1 = models.URLField(blank=True, null=True)
    aff_link_2 = models.URLField(blank=True, null=True)
    aff_link_3 = models.URLField(blank=True, null=True)
    aff_link_4 = models.URLField(blank=True, null=True)
    aff_link_5 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.video_url
