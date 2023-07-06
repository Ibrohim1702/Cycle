from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.CharField(max_length=128)

    def __str__(self):
        return self.name