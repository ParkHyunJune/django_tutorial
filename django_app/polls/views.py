from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # latest_question_list 라는 키로 위 쿼리셋을 전달
    # polls/index.html 를 이용해 render 한결과를 리턴
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = '. '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're votion on question %s." % question_id)
