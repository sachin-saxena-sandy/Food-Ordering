from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    email = models.CharField(max_length=122, blank=True)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=122)
    img = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    desc = models.CharField(max_length=255)
  

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.name
