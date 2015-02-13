from django import forms
from djangotoolbox.fields import ListField
from django.forms import SelectMultiple, MultipleChoiceField, ModelForm
from models import Question, tempQuestion
from models import Tag

class QuestionForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(QuestionForm,self).__init__(*args, **kwargs)
		self.fields['tags'].widget.choices = [(i.pk, i) for i in Tag.objects.all()]
		#self.fields['contributedBy'].required = False
		#self.fields['contributedBy'].widget.attrs['readonly'] = True

	class Meta:
		model = Question


class tempQuestionForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(tempQuestionForm,self).__init__(*args, **kwargs)
		self.fields['tags'].widget.choices = [(i.pk, i) for i in Tag.objects.all()]
		if self.instance.pk:
			self.fields['tags'].initial = self.instance.tags

	class Meta:
		model = tempQuestion
