from django import forms

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Have an Answer? ', max_length=1000)

class AskForm(forms.Form):
    QuestionTitle = forms.CharField(label='Title', max_length=100)
    QuestionText = forms.CharField(label='Question', max_length=1000)
    UserText = forms.CharField(label='Username', max_length=100)

class LoginForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(label='Password', max_length=1000)

class newUserForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(label='Password', max_length=100)
    FirstName = forms.CharField(label='FirstName', max_length=100)
    LastName = forms.CharField(label='LastName', max_length=100)
