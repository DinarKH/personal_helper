from django.shortcuts import render, HttpResponse
from . import forms

def test(request):
    msg_form = forms.MessageForm
    return render(request,'userwork/user.html',{
        'form': msg_form,
    })
