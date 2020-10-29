from django.contrib.auth.models import Group
from django.db import models
from django.db.models.fields.files import ImageField
import os
# Create your models here.

# get media filename and Extention
def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_upload_path(instance, filepath):

    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{filename}{ext}"
    return f"products/{instance.title}{final}"
    





# model for '"behdashti"' products

class Behdashti(models.Model):

    title    = models.CharField(max_length=30)
    caption  = models.TextField(max_length=100, default='تویح مختصر و مفید')
    detail   = models.TextField(max_length=400, default='توضیحات کامل')
    price    = models.IntegerField()
    thumbnail= models.ImageField(upload_to=media_upload_path, null=True, blank=False)


    def __str__(self):
        return self.title



class Tebi(models.Model):

    title     = models.CharField(max_length=30)
    caption   = models.TextField(max_length=100, default='تویح مختصر و مفید')
    detail    = models.TextField(max_length=400, default='توضیحات کامل')
    price     = models.IntegerField()
    thumbnail = models.ImageField(upload_to=media_upload_path, null=True, blank=False)


    def __str__(self):
        return self.title

    