from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404

from polls.models import Question, Choice


# Create your views here.

def index(request):
    # question.choice_set
    # Choice.object.filter(question=question)


    # get_list_or_404 를 사용한 경우
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date')[:5])

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
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
    # question_id가 pk인 question 객체를 가져와
    # context라는 이름을 가진 dic에 'question'이라는 키 값으로 위 변수를 할당
    # 이후 'polls/detail.html'과 context를 랜더한 결과를 리턴
    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist as e:
    #     raise Http404('Question does not exitst')
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    # detail.html 파일을 약간 수정해서 results.html을 만들고
    # 질문에 대한 모든 선택사항의 선택수(votes)를 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    # request의 method가 POST방식일 때,
    if request.method == 'POST':
        # 전달받은 데이터중 'choice'키에 해당하는 값을
        # HttpResponse에 적절히 돌려준다
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            # message프레임워크를 사용
            # 지금 모르셔도 됩니다
            # request에 메시지를 저장해놓고 해당 request에 대한
            # response를 돌려줄 때 메시지를 담아 보낸다
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice",
            )
            return redirect('polls:detail', question_id)
    else:
        return HttpResponse("You're voting on question %s." % question_id)
