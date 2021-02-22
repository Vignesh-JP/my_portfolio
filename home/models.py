from django.db import models

# Create your models here.
class Contact(models.Model):
    user_name    = models.CharField(max_length=100)
    user_email   = models.EmailField(default="")
    user_subject = models.CharField(max_length=300)
    user_msg     = models.TextField()