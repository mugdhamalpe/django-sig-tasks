from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == "POST" :
        number = request.POST.get("number")
        if(int(number) > 0 and int(number) < 500):
            result = [n for n in range(1, int(number)+1)]
            return render(request, 'number.html', { "resnumber": result })
        else:
            return render(request, 'invalid.html', {})
    else:
        return render(request, 'input.html', {})

