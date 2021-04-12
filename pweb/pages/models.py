from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.name
