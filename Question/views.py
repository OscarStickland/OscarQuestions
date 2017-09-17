from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AnswerForm, AskForm, LoginForm
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:20]
    context = {'question_list': question_list}
    return render(request, 'question/index.html', context)

def ask(request):
    print('In ask')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            question_title = form.cleaned_data['QuestionTitle']
            question_text = form.cleaned_data['QuestionText']

            query = Question(question_title=str(question_title), question_text=str(question_text), pub_date=timezone.now())
            query.save()

            return HttpResponse('Thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AskForm()



    context = {'form': form,}

    return render(request, 'question/ask.html', context)

def admin(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/question/login/')
    question_list = Question.objects.all()

    context = {'question_list': question_list}
    return render(request, 'question/admin.html', context)

def delete(request, question_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/question/login/')
    
    if(get_object_or_404(Question, id=question_id) == False):
        return HttpResponseRedirect(reverse('question:admin', args=()))

    Question.objects.filter(id=question_id).delete()
    context = {'question_id': question_id,
               'HttpResponseRedirect' : HttpResponseRedirect}

    return render(request, 'question/delete.html', context)

def question(request, question_id):
    question_object = Question.objects.get(id=question_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            answer = form.cleaned_data['answer']

            query = Answer(question=question_object, answer_text=answer)
            query.save()

            return HttpResponse('Thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnswerForm()



    context = {'question_object': question_object,
               'q': question_object,
               'form': form,
               }

    return render(request, 'question/question.html', context)

