from django.shortcuts import render

# Create your views here.
def nested_if(request):
    d={'a':20,'b':300,'c':40}
    return render(request,'nested_if.html',d)
