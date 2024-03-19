
""" import random

from django.db import models

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=128, null=True, default=f'post {int(random.random() * 100)}')
     #photo = models.ImageField('post/imgs/', null=True)
     created_at = models.DateTimeField(auto_now_add=True, null=True)
     updated_at = models.DateTimeField(auto_now=True, null=True)
     is_actual = models.BooleanField(blank=True, null=True) """

from turtle import update
from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    #str fields
    mobile_phone = models.CharField(max_length=12)

    #data fields
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    #related fields
    user = models.OneToOneField(to=User, related_name = 'account', on_delete=models.CASCADE)

    #dunder methods:
    def __str__(self) -> str:
        return f'{self.id} --- {self.mobile_phone}'
    class Meta:
        db_table = 'UserAccount'
        ordering = ['-created_at']
        verbose_name = 'User account'
        verbose_name_plural = 'User accounts'

class Post(models.Model):
    #str fields
     title = models.CharField(max_length=255)

     # File/ Image fields:
     image = models.ImageField(upload_to= 'imgs/posts', null=True, blank=True)
    #bool felds
     is_active = models.BooleanField(default=False)

     #date fields
     created_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)

     #related fields
     user = models.ForeignKey(to=User, related_name = 'posts', on_delete = models.CASCADE)
     categories = models.ManyToManyField(
         to='Category',
         related_name='posts',
         #through="PostCategory",
         #through_fields=("post", 'category),
     )
     #dunder methods
     def __str__(self) -> str:
         return f'{self.id} --- {self.title}'
     class Meta:
         db_table = 'Post'
         ordering = ['-created_at']
         verbose_name = 'Post'
         verbose_name_plural = 'Posts'     

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Post_new(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Post_delete(models.Model):
    created_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='poze', blank=True, null=True)
    text = models.CharField(max_length=1000, default='Nimic', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

 #class PostCategory(models.Model):
    #str fields
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)

    #related fields 
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #class Meta:
        #db_table = 'PostCategory'
        #verbose_name = 'Post-Category'
        #verbose_name_plural = 'Post=Categories'

# And/Or zapros
# values => list of directions
# values_list => lis of corteg
# only => queryset of model's object + get id (default)