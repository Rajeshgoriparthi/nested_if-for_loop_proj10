from django.shortcuts import render

# Create your views here.
def for_loop(request):
    doc={'name':'Rajesh'}
    return render(request,'for_loop.html',doc)