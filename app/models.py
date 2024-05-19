from django.db import models

# Create your models here.
# model is a thing by which we definne the database
# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=200)
    date=models.DateField()

    def __str__(self):
        return self.name