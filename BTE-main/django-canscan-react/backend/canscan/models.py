from django.db import models

# Create your models here.


class canscan(models.Model):
    # what are the models?
    Recycling_type = models.CharField(max_length=120)
    Green_points_earned = models.CharField(max_length=120)
    Bin_opened = models.CharField(max_length=120)
   
    def _str_(self):
        return self.title
