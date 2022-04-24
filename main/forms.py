from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from click import style
from django import forms
from django.forms import ModelForm, TextInput
from .models import Answer,Question,CustomUser


class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('detail',)
        widgets={
            'detail': TextInput(attrs={
                'class':'form-control',
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Write here...',

            }),
        }

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','detail','tags')
        widgets={
            'title': TextInput(attrs={
                'class':'form-control',
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Title...'

            }),
            'detail': TextInput(attrs={
                'class': "form-control",
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Details...'
            }),
            'tags':TextInput(attrs={
                'class': "form-control",
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Tags...'
            })
        }

class ProfileForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','username','bio','location')
        widgets={
            'first_name': TextInput(attrs={
                'class':'form-control',
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'First Name...'

            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Last Name...'
            }),
            'username':TextInput(attrs={
                'class': "form-control",
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Username...',
                
            }),
            'bio':TextInput(attrs={
                'class': "form-control",
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Bio...',
                
            }),
            'location':TextInput(attrs={
                'class': "form-control",
                'style':'background-color:#202124; color:white; border-color:black;',
                'placeholder':'Location...',
                
            })
        }