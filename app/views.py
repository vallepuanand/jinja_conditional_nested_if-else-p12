from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':12,'b':21,'c':40}
    return render(request,'conditional.html',d)