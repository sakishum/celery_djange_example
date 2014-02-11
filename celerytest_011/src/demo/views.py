# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from tasks import add


def index(request):
    errors = []
    print request.method
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        task = add.delay(a, b)
        return render(request, 'success.html', {'task':task})
    return render(request, 'index.html', {'errors':errors})
