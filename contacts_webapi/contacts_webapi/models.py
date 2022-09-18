from django.db import models

class Contact(models.Model):
    id = models.PositiveIntegerField(editable=False)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
