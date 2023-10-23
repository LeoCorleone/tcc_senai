from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def adm(request):
    return render(request, 'adm.html')
