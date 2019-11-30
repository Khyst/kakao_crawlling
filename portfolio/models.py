from django.db import models

# Create your models here.
class Portfolio(models.Model):
    img_id = models.IntegerField(default="1")
    title = models.CharField(max_length=255)
    image = models.ImageField('Label', upload_to='images/')
    description = models.CharField(max_length=1000)

    """for i in range(1, 10, 1):
        print(1)"""
    
    def  __str__(self):
        return self.title

