from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    url = models.CharField(max_length = 200)


class Tags(models.Model):
    tag = models.CharField(max_length = 250)

    def __str__(self):
        return self.tag