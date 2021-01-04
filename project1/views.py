from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Person


def index(request):
    latest_question_list = Person.objects.order_by('id')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def index1(request):
    #从数据库中取5条数据，按照id排序
    latest_question_list = Person.objects.order_by('id')[:5]
    #遍历上面的5条数据，取每条数据的first_name，追加到output后面
    output = ', '.join([q.first_name for q in latest_question_list])
    return HttpResponse(output)

def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % (question_id))

#def detail(request, question_id,second_id):
#    return HttpResponse("You're looking at question %s.%s" % (question_id, second_id))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)