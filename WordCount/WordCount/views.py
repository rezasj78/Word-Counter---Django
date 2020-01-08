from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    full = str(request.GET['fulltext'])
    key = (request.GET['word'])
    textlist = full.split()
    cou = 0
    for i in textlist:
        if i.lower() == key.lower():
            cou += 1

    return render(request, 'count.html', {'text': full, "count": cou, "fullcount": len(textlist)})

def about(request):
    return render(request, "about.html")
