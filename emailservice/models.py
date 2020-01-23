from django.db import models

# Create your models here.
class MailList(models.Model):
    time = models.DateTimeField()
    email_subject = models.TextField()