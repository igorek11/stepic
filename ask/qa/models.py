from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True) 
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User,related_name='author')
	likes = models.ManyToManyField(User,related_name='likes')
	#__str__(self):
	#	return (self.)
	class Meta: 
		db_table = 'Question'
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	question =models.ForeignKey(Question) 
	author = models.ForeignKey(User)
	class Meta: 
		db_table = 'Answer'


