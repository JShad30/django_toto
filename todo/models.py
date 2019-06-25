from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False) #Blank here means that the filed will not be nullable. If set to true a nullable field would be allowed
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name