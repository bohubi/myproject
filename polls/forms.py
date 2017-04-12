from django import forms
from django.contrib.auth.models import User

from polls.models import Question, Choice


class Myform(forms.Form):
    question_name = forms.CharField(max_length=200, min_length=1, required=True)


    #name = forms.CharField(max_length=200, min_length=1, required=True)
    # telephone_number = forms.CharField(max_length=8, min_length=8, required=True, help_text="enter digits only")
    # email= forms.EmailField()
    # gender= forms.ChoiceField(choices=[(None,"Select a gender"),("M","Male"),("F","Female")])
    # agree=forms.BooleanField(required=True, label="I agree on the terms and conditions")

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]

class ChoiceForm (forms.ModelForm):
    class Meta:
        model= Choice
        fields= ["question", "choice_text"]
        labels = {
            'question': 'choose a question',
            'choice_text' : 'Enter a choice'
        }
        widgets = {'question' : forms.HiddenInput}

class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'username', 'password'}
        widgets = {'password': forms.PasswordInput}


