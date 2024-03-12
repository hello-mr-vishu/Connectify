from django.db import models

# Create your models here.
class PDF(models.Model):
    name=models.CharField(max_length=20,default="NewChat")
    pdf=models.FileField(upload_to='files/')

    def __str__(self):
        return self.name