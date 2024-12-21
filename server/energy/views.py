from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm


def home(request: HttpRequest):
    return HttpResponse("Moin, welcome to global energy.")

def upload(request: HttpRequest):
    if request.method == 'POST':
        form = DocumentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('energy-home')
    else:
        form = DocumentForm()
    return render(request=request, template_name='upload.html', context={
        'form': form
    })
