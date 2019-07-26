from django.db import models
from faker import Faker
#
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

for i in range(1, 10, 1):
    myfake = Faker()
    blogger = Blog()
    blogger.title = myfake.name
    blogger.pub_date = myfake.date
    blogger.body = myfake.text