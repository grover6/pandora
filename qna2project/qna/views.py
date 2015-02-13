# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from qna.models import Question, Tag
from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django_mongodb_engine.contrib import MongoDBManager


def index(request):
	return HttpResponse("Hello Kids, you are at question and asnwer site. simple and sweet.")

def askq(request):
	try:
		if 'q_count' in request.session:
			q_count = request.session['q_count'] 
		else:
			q_count = 0


		if request.method == 'POST':
			q_count = request.session['q_count'] + 1
	
	
		request.session['q_count'] = q_count
		q = Question.objects.all()[q_count:q_count+1]
		#q = Question.objects.raw({'tags' : {'tag_name' : 'Doremon'}})[q_count:q_count+1]
		template = loader.get_template('qna/askq.html')
		c = {}
		c.update(csrf(request))
		c.update({'question': q})
		#context = RequestContext(csrf(request), {
		#	'question': q,
		#})
	except Question.DoesNotExist:
		raise Http404
	#return render(request, 'qna/askq.html', context)
	return render_to_response("qna/askq.html", c)


def tags(request):
	try:
		t = Tag.objects.all()
		c = {}
		#c.update(csrf(request())
		c.update({'tags': t})
	except Tag.DoesNotExit:
		raise Http404
	return render_to_response("qna/tags.html", c)

def images(request, image):
	render_to_response("qna/" + image,{})

def qfortag(request, tag):
	try:
		sessiontag = "q_count_" + tag.strip()
		if sessiontag in request.session:
			q_count = request.session[sessiontag] 
		else:
			q_count = 0

		objects = MongoDBManager()

		if request.method == 'POST':
			q_count = request.session[sessiontag] + 1

		tag = tag.strip()
	
		request.session[sessiontag] = q_count
		#q = Question.objects.all()[q_count:q_count+1]
		#q = Question.objects.raw_query({'tags' : {'tag_name' : 'Doremon'}})[q_count:q_count+1]
		#working - q = Question.objects.filter(answer__exact=1)
		c = {}
		c.update(csrf(request))
		t = Tag.objects.get(tag_name=tag)
		c.update({'tag': t})
		if t:
			q = Question.objects.filter(published__exact='P').filter(tags=t.id)[q_count:q_count+1]
			if not q:
				q_count = 0
				q = Question.objects.filter(published__exact='P').filter(tags=t.id)[q_count:q_count+1]
				request.session[sessiontag] = q_count
				
			c.update({'question': q})

	except Question.DoesNotExist:
		raise Http404
	except Tag.DoesNotExist:
		#raise Http404
		c.update({'ErrorMessage': 'no such tag!' + tag})
	return render_to_response("qna/qfortag.html", c)
