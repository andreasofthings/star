from django.db import models

# Create your models here.

class UpDown(models.Model):
  absolute_url = models.CharField(max_length=256)
  up = models.IntegerField(default=0)
  down = models.IntegerField(default=0)

  def score(self):
    return self.up - self.down

  def __unicode__(self):
    return "%s: %s"%(self.absolute_url, self.score())
