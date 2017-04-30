from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone

from polls import forms
from polls.models import Question, Choice
from django.http.response import HttpResponse, HttpResponseRedirect
from polls.forms import Myform



def index(request):
    question_list = Question.objects.all()
    question_count = question_list.count()
    if request.method == 'GET':
        form = Myform()
        context = {"questions":question_list, "question_count":question_count,"form":form}
        return render(request, "polls/index.html", context)
    elif request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_name']
            q = Question(question_text=question_text, pub_date=timezone.now())
            q.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully added a poll")

            return redirect(request, "polls:index")
            #return render(request, "polls/ok.html")
        else:
            messages.add_message(request, messages.WARNING, "There was an error in your form")
            context = {"questions":question_list, "question_count":question_count,"form":form}
            return render(request, "polls/index.html", context)
    else:
        return render(request, "polls/oops.html")



'''latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text + "  " + str(q.pub_date) for q in latest_question_list])
    return HttpResponse(output)'''


def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    return render(request, "polls/detail.html", {'question': q})


def vote(request, question_id):
    choice_id = request.POST.get("choice")
    choice = Choice.objects.get(id=choice_id)
    choice.votes += 1
    choice.save()
    context = {"choice":choice, "question":Question.objects.get(id=question_id)}
    #return HttpResponse("%s has %d votes" %(choice, choice.votes))
    #return HttpResponseRedirect(redirect_to=reverse('results', args=[question_id]))
    return render(request, "polls/vote.html", context)


def results(request, question_id):
    q = Question.objects.get(id=question_id)
    return HttpResponse('showing results')

def itworks(request, stuff,more,araboo):
    context= [stuff,more,araboo]
    return render(request, "polls/itworks.html", {'cont':context})
        #HttpResponse("<h1> It Works!</h1><h1>Stuff is %s </h1><h2>more is %s</h2><h2>anything is %s</h2>" %(stuff,more,araboo))

def todo(request):
    pass

def add_question(request):
    if request.method == 'GET':
        form = Myform()
        context = {"form":form}
        return render(request, "polls/add_question.html", context)
    elif request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_name']
            q = Question(question_text=question_text, pub_date=timezone.now(), owner=request.user)
            q.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully added a poll")
            return redirect('polls:index')
            #return render(request, "polls/ok.html")
        else:
            messages.add_message(request, messages.WARNING, "There was an error in your form")
            context = {'form': form}
            return render(request, "polls/add_question.html", context)
    else:
        return render(request, "polls/oops.html")



def edit_question(request, question_id):
    question = Question.objects.get(id=question_id)
    add_choice_form = forms.ChoiceForm(initial={'question':question})
    if request.method == "GET":
        form = forms.QuestionForm(instance=question)
        context = {
            "question" : question,
            "form": form,
            "choice_form": add_choice_form
        }
        return render(request, "polls/edit_question.html",context)

    elif request.method == "POST":
        form = forms.QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Edit successful")
            return redirect('polls:edit_question', question_id=question_id)
            # return render(request, "polls/ok.html")
        else:
            messages.add_message(request, messages.WARNING, "Something is wrong")
            context = {'question': question,
                       'form': form ,
                       "choice_form": add_choice_form}
            return render(request, "polls/edit_question.html", context)


def add_choice(request):
    form = forms.ChoiceForm(request.POST)
    if form.is_valid():
        choice = form.save()
        return redirect('polls:edit', question_id= choice.question.id)
        # return redirect('/polls/question/%s/edit'%(choice.question.id))
    else:
        return redirect ("polls:index")


def delete_question(request, question_id):
    if request.method == "POST":
        question = Question.objects.get(id=question_id)
        if question.owner == request.user:
            question.delete()
            messages.add_message(request, messages.WARNING, "Question Gone!")
            return redirect("polls:index")
        else:
            return redirect("polls:oops")
    else:
        return redirect("polls:index")


def delete_choice(request, choice_id):
    if request.method == "POST":
        choice = Choice.objects.get(id=choice_id)
        choice.delete()
        messages.add_message(request, messages.WARNING, "Choice Gone!")
        return redirect("polls:edit", choice.question.id)
    else:
        return redirect("polls:detail")



def edit_choice(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    if request.method == "GET":
        form_obj = forms.ChoiceForm(instance=choice)
        context = {
            "choice" : choice,
            "form": form_obj,
        }
        return render(request, "polls/edit_choice.html",context)

    elif request.method == "POST":
        form = forms.ChoiceForm(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Edit successful")
            return redirect('polls:edit', question_id=choice.question.id)
            # return render(request, "polls/ok.html")
        else:
            messages.add_message(request, messages.WARNING, "Something is wrong")
            context = {'choice': choice,
                       'form': form ,
                       }
            return render(request, "polls/edit_choice.html", context)

def signin(request):
    if request.method == 'GET':
        form = forms.SigninForm()
        context = { 'form' : form }
        return render(request, "polls/signin.html", context)
    else:
        form = forms.SigninForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, "Invalid form data, try again")
            context = {'form': form}
            return render(request, "polls/signin.html", context)
        # form is valid, so, proceed
        username = form.data.get("username")
        password = form.data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.add_message(request, messages.WARNING, "Invalid userid/password")
            context = {'form': form}
            return render(request, "polls/signin.html", context)
        # user is authenticated
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "You are now logged in")
        return redirect("polls:index")


def register(request):
    if request.method == 'GET':
        form = forms.SignupForm()
        context = {'form': form}
        return render(request, "polls/register.html", context)
    else:
        form = forms.SignupForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, "Invalid form data, try again")
            context = {'form': form}
            return render(request, "polls/register.html", context)
        # form is valid, so, proceed
        password =form.data.get("password")
        user = form.save()
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "User Created")
        return redirect("polls:register")

def use_api(request):
    import requests
    # url = "http://api.github.com/events"
    # r = requests.get(url)
    # events = r.json()
    # context = {'events': events}
    return render(request, "polls/use_api.html", {})


def use_api2(request):
    import requests
    code = request.GET.get("code")
    url = "https://api.instagram.com/oauth/access_token"
    r = requests.post(url, data={
        'client_id':'29c4170223c24304b159d0d3b4546579',
        'client_secret':'3628fbe4f4af4badade334945ee2ba62',
        'grant_type':'authorization_code',
        'redirect_uri' : 'http://localhost:8000/polls/use_api2/',
        'code': code,
    })
    # print("code is" + code)
    return render(request, "polls/use_api2.html", {"code":code, "r":r, "u":r.json()})

# def InstaUser(AbstractBaseUser):
#     access_token =

def maps(request):
    return render(request, "polls/maps.html", {})