from django.db import models
from datetime import datetime
# Create your models here.
class agent(models.Model):
    name = models.CharField(max_length=200)
    biodata = models.TextField()
    email= models.EmailField()
    phone= models.CharField(max_length=17)
    Top_saller = models.BooleanField(default=False)
    date_time = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.name
    
    