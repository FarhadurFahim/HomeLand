from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.conf import settinngs

# Create your models here.
class  Post(models.Model):
		author = models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		text = models.TextField()
		picture = models.ImageField("Image",upload_to="media/")
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null = True)

		#user = models.OneToOneField(User)

		def publish(self):
			self.published_date = timezone.now()
			self.save()

		def  __str__(self):
			return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	name = models.CharField(max_length=30)
	#email = models.emailFiled()
	contactNo = models.CharField(max_length=11, default="")
	address = models.CharField(max_length=200, default="")
	bio = models.TextField(blank=True)
	#picture = models.ImageField(blank=True)

	def __unicode__(self):
		return self.user.username
