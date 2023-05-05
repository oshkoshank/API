from django.db import models

# Create your models here.
class Content(models.Model):
    content_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=10000,null=False, blank=False, default='')

    def __str__(self):
        return self.content_name
    
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=10000,null=False, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.ManyToManyField(Content,related_name='categories')

    def __str__(self):
        return self.title