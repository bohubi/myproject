from django.shortcuts import render
from polls.models import Question
from django.http.response import HttpResponse


def index(request):
    question_list = Question.objects.all()
    question_count = question_list.count()
    context = {'questions': question_list, 'question_count': question_count}

    return render(request, "polls/index.html", context)


'''latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text + "  " + str(q.pub_date) for q in latest_question_list])
    return HttpResponse(output)'''


def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    return render(request, "polls/detail.html", {'question': q})


def vote(request, HttpRequest, question_id):
    cid = request.POST.get("choice")
    c = Choice.objects.get(id=cid)
    c.votes += 1
    c.save()
    return HttpResponseRedirect(redirect_to=reverse('results', args=[question_id]))


def results(request, question_id):
    q = Question.objects.get(id=question_id)
    return HttpResponse('showing results')
