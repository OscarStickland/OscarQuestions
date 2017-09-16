from django import forms

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Have an Answer? ', max_length=1000)

class AskForm(forms.Form):
    QuestionTitle = forms.CharField(label='Title', max_length=100)
    QuestionText = forms.CharField(label='Question', max_length=1000)

class LoginForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(label='Password', max_length=1000)
