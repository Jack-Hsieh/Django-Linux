from django.db import models

from django.utils import timezone #導入時間

from django.contrib.auth.models import User

# Create your models here.
# 建置後台消息管理系統要有的內容部分


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title

class Pricing(models.Model):
	title = models.CharField(max_length=20)
	price = models.CharField(max_length=20)
	content_1 = models.CharField(max_length=20)
	content_2 = models.CharField(max_length=20, blank=True)
	content_3 = models.CharField(max_length=20, blank=True)
	conten_4 = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.title


class About(models.Model):
	photo = models.URLField(blank=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	email = models.EmailField(max_length=70) #Email setting

	def __str__(self):
		return self.title


class Request(models.Model):
	datetime = models.DateTimeField(default=timezone.now)
	username = models.CharField(max_length=100)
	email = models.EmailField(max_length=70)
	comment = models.TextField(max_length=100)
