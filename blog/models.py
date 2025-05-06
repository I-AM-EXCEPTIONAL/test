

# Create your models here.
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField



# Create your models here.

# Category model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return self.title


#year model
class Year(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title

# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    web_url = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    batch = models.ManyToManyField(Year)
    image = models.ImageField( upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)




    def __str__(self):
        return self.title

