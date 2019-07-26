from blog.models import Blog
from faker import Faker


for i in range(1, 10, 1):
    myfake = Faker()
    blogger = Blog()
    blogger.title = myfake.name
    blogger.pub_date = myfake.date
    blogger.body = myfake.text