from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
from django.forms import SelectMultiple, MultipleChoiceField, ModelForm
from django.contrib.auth.models import User
#from current_user import CurrentUserMiddleware 

# Create your models here.

class ModelListField(ListField):
	def formfield(self, **kwargs):
		return FormListField(**kwargs)

class ListFieldWidget(SelectMultiple):
	pass

class FormListField(MultipleChoiceField):
	widget = ListFieldWidget

	def clean(self, value):
		return value

class Tag(models.Model):
	tag_name = models.CharField(max_length=20)
	def __unicode__(self):
		return '%s' % (self.tag_name)

class Question(models.Model):
	PUBLISH_CHOICES = (
		('N', 'New'),
		('R', 'Under Review'),
		('P', 'Published'),
	)
	statement = models.TextField()
	#contributedBy = models.CharField(max_length=50)
	#contributedBy = models.ForeignKey('auth.User', default=CurrentUserMiddleware.get_current_user) 
	contributedBy = models.ForeignKey(User) 
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	answer = models.CharField(max_length=1)
	information = models.TextField()
	#tags = models.CharField(max_length=100)
	#tags = models.ManyToManyField(Tag)
	tags = ModelListField(models.ForeignKey('Tag'))
	published = models.CharField(max_length=1, null=True, choices=PUBLISH_CHOICES, default="N")
	#tags = ModelListField(EmbeddedModelField('Tag'))
	def __unicode__(self):
		return '%s' % (self.statement)

class tempQuestion(models.Model):
	statement = models.TextField()
	contributedBy = models.CharField(max_length=50)
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	answer = models.CharField(max_length=1)
	information = models.TextField()
	tags = ModelListField(EmbeddedModelField('Tag'))
	def __unicode__(self):
		return '%s' % (self.statement)
