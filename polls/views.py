from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "選択肢を選んでください。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    total_votes = sum(c.votes for c in question.choice_set.all())

    # 各選択肢に割合データを追加
    choices = []
    for choice in question.choice_set.all():
        ratio = (choice.votes / total_votes * 100) if total_votes > 0 else 0
        choices.append({
            "text": choice.choice_text,
            "votes": choice.votes,
            "ratio": round(ratio, 1),
        })

    context = {
        "question": question,
        "choices": choices,
        "total_votes": total_votes,
    }
    return render(request, 'polls/results.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後そのままログインさせる
            return redirect('polls:index')  # 登録後の遷移先
    else:
        form = SignUpForm()

    return render(request, 'polls/signup.html', {'form': form})

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

