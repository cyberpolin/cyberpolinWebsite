from django.db import models
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
from PIL import Image

import time

#d = time.strftime("%d")
m = time.strftime("%m")
Y = time.strftime("%Y")
fs = FileSystemStorage(location='static/'+Y+'/'+m)


class Tags(models.Model):
    tag = models.CharField(max_length=250)

    def __str__(self):
        return self.tag


class Tipo(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo


class Media(models.Model):
    title = models.CharField(max_length=100, null = True)
    alt = models.CharField(max_length=100, null = True)
    caption = models.CharField(max_length=100, null = True)
    description = models.CharField(max_length=100, null = True)
    date = models.DateField(auto_now_add=True)
    latlon = models.CharField(max_length=50, null = True)
    file = models.ImageField()

    def save(self):

        if not self.id and not self.file:
            return

        super(Media, self).save()

        image = Image.open(self.file)
        (width, height) = image.size

        "Max width and height 800"
        if (800 / width < 800 / height):
            factor = 800 / height
        else:
            factor = 800 / width

        size = ( width / factor, height / factor)
        image2 = image.resize(size, Image.ANTIALIAS)
        image.save(self.file.path)
        image2.save(self.file.path+'_thumb')

    def __str__(self):
        return str(self.file)


class Publicacion(models.Model):
    slug = models.SlugField()
    titulo = models.CharField(max_length=250)
    texto = models.TextField()
    tipo = models.ForeignKey(Tipo, default=2)
    fecha = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    img = models.ImageField(storage=fs)

    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.titulo) #Or whatever you want the slug to use
        super(Publicacion, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo + ' ' + str(self.pk)

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    url = models.URLField()
    img = models.FileField(storage = fs)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title