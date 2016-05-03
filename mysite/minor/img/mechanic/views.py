from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect
#from django.core.context_processors import csrf 
# Create your views here.
@csrf_exempt
def postdata(request):
    if request.method == "POST":
        data=request.POST.get('data')
    return HttpResponse(data)

