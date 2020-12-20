from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.
class BlogPost(models.Model):
  title = models.Charfield(max_lenght=50)
  slug=models.Slugfield
