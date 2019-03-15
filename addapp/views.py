from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def add(request):
    operation = request.POST["op"]
    try:
        v1=request.POST["t1"]
        v2=request.POST["t2"]
        i=int(v1)
        j=int(v2)
    except(ValueError):
        return render(request,'input.html')
    if operation=="add":
        z=i+j
        return HttpResponse("sum is: "+str(z))
    elif operation=="sub":
        z = i - j
        return HttpResponse("sub is: " + str(z))
    elif operation=="mul":
        z = i * j
        return HttpResponse("mul is: " + str(z))
    elif operation=="div":
        try:
            z = i / j
            return HttpResponse("div is: " + str(z))
        except(ZeroDivisionError):
            return render(request,'input.html')
