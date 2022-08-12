'''
from django.db import models

class apiRoom(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class apiMessage(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return self.user

class apiCsvUpload(models.Model):
    file_name = models.FileField(upload_to='csv')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
'''