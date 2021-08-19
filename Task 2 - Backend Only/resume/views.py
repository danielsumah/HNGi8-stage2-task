from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages


# Create your views here.

def home_view(request):
    form = MessageForm()

    if request.method == "POST":
        data = request.POST
        form = MessageForm(data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message has been Sent to Daniel')
            print("messaged saved")
            return HttpResponseRedirect("/")
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'resume/index.html', context)
