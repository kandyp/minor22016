from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect
#from django.core.context_processors import csrf 
# Create your views here.


@csrf_exempt
def setmech(request):   
    if request.method == 'POST':
            mid = request.POST.get('mechid')
            from minor.models import mechanic
            try:
                q=mechanic.objects.get(id=mid)
                name=q.name
                imagePath = os.path.dirname(os.path.abspath(__file__))+"\\mechanic\\"+str(mid)+"_"+name+str(mid)+".jpg"
                destination = open(imagePath, 'wb+')
                for chunk in request.FILES['image'].chunks():
                        destination.write(chunk)
                destination.close()
            except mechanic.DoesNotExist:
                return HttpResponse("NO-invalid mechanic")
    
    return HttpResponse("OK-")

def getmech(request):
    if request.method == "GET":
        r1=request.GET.get('mechid')
        from minor.models import mechanic
        try:
            q=mechanic.objects.get(id=r1)
            name=q.name
        except mechanic.DoesNotExist:
            return "ER-invalid mid"
        try:
            file_path = os.path.dirname(os.path.abspath(__file__))+"\\mechanic\\"+str(mid)+"_"+name+"\\"+str(mid)+".jpg"
            fsock = open(file_path,"r")
            file_name = os.path.basename(file_path)
            response = HttpResponse(fsock)
            response['Content-Disposition'] = 'attachment; filename=' + file_name            
        except IOError:
            response = HttpResponseNotFound()

    return response

@csrf_exempt
def getdata(request):
    if request.method == "GET":
        data=request.GET.get('data')
    return HttpResponse(data)

@csrf_exempt
def setuser(request):
    return response

def getuser(request):
    if request.method == "GET":
        r1=request.GET.get('usrid')