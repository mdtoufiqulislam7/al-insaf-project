from django.db import models
from agent.models import agent

# Create your models here.
class visadata(models.Model):
    class packegType(models.TextChoices):
        Umara = "FullPackeg"
        visa = 'just_visa'
    class airticket(models.TextChoices):
        sv = 'sv'
        qt= 'qt'
        gf = 'gf'
        bg = 'bf'    
        
    agent = models.ForeignKey(agent,on_delete=models.DO_NOTHING,related_name='agents')
    slag = models.CharField(max_length=12,unique=True)
    datetime = models.CharField(max_length=15)
    packegtype = models.CharField(max_length=50,choices=packegType.choices, default=packegType.Umara)
    airticket = models.CharField(max_length=20,choices=airticket.choices,default=airticket.sv)
    totalhaji = models.TextField()
    parcost= models.TextField()
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.slag
    
    