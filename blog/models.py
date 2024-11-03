from django.db import models
from django.utils.text import slugify
#category should be dynamic
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null= True) #default length is 200 if u need more include max_length parameter
    created_at = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
    #the below method creation is not compulsory but optional, but it is a good practice, if we have to print then it will be useful
    def __str__(self):
        return self.title


class AboutUs(models.Model):
    content = models.TextField()