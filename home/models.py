from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name
