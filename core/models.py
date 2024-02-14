from django.db import models

class TimeStampModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Restaurant(TimeStampModel):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)

  def __str__(self):
    return f"{self.name} - {self.address}"
