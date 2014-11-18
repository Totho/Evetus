from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings 
# Create your models here.
class TimeStampModel(models.Model):

	created = models.DateTimeField(auto_now=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Category(models.Model):

	name = models.CharField(max_length=50)
	slug = models.SlugField(editable=False)

	def save (self,*args,**kwargs):
		if not self.id:
			self.slug=slugify(self.name)
		super(category,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.name


class Event (TimeStampModel):

	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(editable=False)
	summary = models.TextField(max_length=255)
	content = models.TextField()
	category =models.ForeignKey(Category)
	place = models.CharField(max_length=50)
	start = models.DateTimeField()
	finish = models.DateTimeField()
	imagen = models.ImageField(upload_to ='events')#---
	is_free = models.BooleanField(max_digits=5,decimal_places=2, default=0.00)
	views = models.PositiveIntegerField(default=0)
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL)

	def save (self,*args,**kwargs):
		if not self.id:
			self.slug = slungify(self.name)
		super(Event,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.name


class Assistant(TimeStampModel):

	assistant = models.ForeingnKey(settings.AUTH_USER_MODEL)
	event = models.ManyToManyField(Event)

	attended = models.BooleanField(default = False)
	has_paid = models.BooleanField(default = False)

	def  __unicode__(self):
		return "%s %S " % (self.assistant.username , self.event.name)

class Comments (TimeStampModel):

	user = models.ForeingnKey(settings.AUTH_USER_MODEL)
	event = models.ForeingnKey(Event)

	content = models.TextField()

	def __unicode__(self):
		return "%s %s " % (self.user.username , self.event.name)