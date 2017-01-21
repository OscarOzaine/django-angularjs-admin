from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class RangeParameter(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    gpio = models.CharField(max_length=255, blank=True, default='')
    max = models.TextField()
    max_value = models.TextField()
    #min = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    min = models.TextField()
    min_value = models.TextField()
    range_id = models.IntegerField()
    sensor_id = models.IntegerField()
    
    owner = models.ForeignKey('auth.User', related_name='rangeparameters', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        'owner',
        ordering = ( 'created',)


class Snippet(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('owner', 'created',)


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     ''' Creates a token whenever a User is created '''
#     if created:
#         Token.objects.create(user=instance)

# owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
# highlighted = models.TextField()

# class InternalUser(User):
#     #first_name = models.CharField(max_length=55)
#     #last_name = models.CharField(max_length=55)
#     #username = models.CharField(max_length=35)
#     #password = 
#     """docstring for User"""
#     def __init__(self, arg):
#         super(User, self).__init__()
#         self.arg = arg
#         #ordering = ['-id']
#         app_label = 'internal'
#         db_table = 'users'

# class Chain(models.Model):
#     """ High-level retail chain model"""
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)
#     slogan = models.CharField(max_length=500)
#     founded_date = models.CharField(max_length=500)
#     website = models.URLField(max_length=500)


# class Store(models.Model):
#     """ Store location model.  Foreign key to Chain."""
#     chain = models.ForeignKey(Chain)
#     number = models.CharField(max_length=20)
#     address = models.CharField(max_length=1000)
#     opening_date = models.DateTimeField(default=timezone.now)

#     # Business hours in a 24 hour clock.  Default 8am-5pm.
#     business_hours_start = models.IntegerField(
#         default=8,
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(23)
#         ]
#     )
#     business_hours_end = models.IntegerField(
#         default=17,
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(23)
#         ]
#     )


# class Employee(models.Model):
#     """ Location employee model.  Foreign key to Store."""
#     store = models.ForeignKey(Store)
#     number = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     hired_date = models.DateTimeField(default=timezone.now)

#     