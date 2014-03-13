import datetime
from django.db import models
from django.utils import timezone


class Poll(models.Model):
	question = models.CharField(max_length=100) 
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question

	def was_published_recently(self):
		now = timezone.now()
		# Polls whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=100)
	vote = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text
# Create your models here.
