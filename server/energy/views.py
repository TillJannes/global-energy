from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm


def home(request: HttpRequest):
    return render(request, template_name="home.html")

def upload(request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
    submitted = False
    if request.method == 'POST':
        form = DocumentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/upload?submitted=True")
    else:
        form = DocumentForm()
        if "submitted" in request.GET:
            submitted = True
    return render(request=request, template_name='upload.html', context={
        'form': form,
        "submitted": submitted,
    })

def insert(request: HttpRequest):
    pass
