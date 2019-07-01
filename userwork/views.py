from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import MessageForm
from .models import Message


def head(requset):
    return HttpResponse('ok')

def userProfile(request):
    msg_obj = Message.objects.all()
    print(msg_obj)
    if request.method == 'POST':
        msg_form = MessageForm(data=request.POST)
        if msg_form.is_valid():
            msg_form.save()
            return HttpResponseRedirect('./')
    return render(request,'userwork/user.html',{
        'form': MessageForm,
        'obj': msg_obj,
    })
