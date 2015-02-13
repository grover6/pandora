from django.contrib import admin 
from models import Question, tempQuestion, Tag
from .forms import QuestionForm, tempQuestionForm

class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	readonly_fields = ('contributedBy',)
        list_display = ('statement','contributedBy','option1','option2','option3','option4','answer')
	#list_display_links = ('statement',)
        #list_editable = ('option1','option2','option3','option4','answer','information','tags')
	
	def __init__(self, model, admin_site):
		super(QuestionAdmin,self).__init__(model, admin_site)

	def save_model(self, request, obj, form, change):
		obj.contributedBy = request.user
		obj.save()

	def get_form(self, request, obj=None, **kwargs):
		self.exclude = []
		if not request.user.is_superuser:
			self.exclude.append('published')
		return super(QuestionAdmin, self).get_form(request, obj, **kwargs)

class tempQuestionAdmin(admin.ModelAdmin):
	form = tempQuestionForm
	
	def __init__(self, model, admin_site):
		super(tempQuestionAdmin,self).__init__(model, admin_site)

admin.site.register(Tag)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question)
#admin.site.register(tempQuestion, QuestionAdmin)

