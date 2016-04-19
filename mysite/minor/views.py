from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
#from django.contrib.gis import GeoIP
from django.core import serializers
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from django.db import models
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect
#from django.core.context_processors import csrf 
# Create your views here.
@csrf_exempt
def postdata(request):
    if request.method == "POST":
        data=request.POST.get('data')
    return HttpResponse(data)

def index(request):
    message=""
    if request.method == 'GET':    
        geolocator = Nominatim()
        try:
            if request.GET.get('long') and request.GET.get('lat'):
                latit=request.GET.get('lat')
                longi=request.GET.get('long')
                location = geolocator.reverse( "{}, {}".format(latit, longi))
                message = "OK-"+location.address+"--"+str(location.latitude)+"--"+str(location.longitude)
            else:
                addr = request.GET.get('address')
                location = geolocator.geocode(addr)
                message= "OK-"+location.address
                #location.address+"###"+str(location.latitude+"###"+str(location.longitude)+"###"+str(location.raw)  
        except GeocoderTimedOut:
            message="Timeout-"
       # except Exception as f:
        #    message="ER-"+str(f)
            
        
    return HttpResponse(message)



@csrf_exempt
def regrider(request):
    
    if request.method == "POST":
        r1=request.POST.get('username')
        r2=request.POST.get('password')
        r3=request.POST.get('fname')
        r4=request.POST.get('lname')
        r5=request.POST.get('lon')
        r6=request.POST.get('lat')
        from minor.models import rider
        try:
            q=rider(usrname=r1, password=r2, f_name=r3, l_name=r4, home_lon=r5, home_lat=r6)
            q.save()
            message="OK-"+str(q.id)
        except Exception as e:
            message="ER-"+str(e) 
    else:
        message="NO-"
        
    return HttpResponse(message)


@csrf_exempt
def regmech(request):
    if request.method == "POST":
        r1=request.POST.get('username')
        r2=request.POST.get('password')
        r3=request.POST.get('name')
        r4=request.POST.get('regtype')
        r5=request.POST.get('regid')
        r6=request.POST.get('lon')
        r7=request.POST.get('lat')
        r8=request.POST.get('phone')
        r9=request.POST.get('email')
        r10=request.POST.get('address')
        r11=request.POST.get('shopname')
        from minor.models import mechanic
        try:
            q=rider(usrname=r1, password=r2, name=r3, reg_type=r4, reg_id=r5, mlon=r6, mlat=r7, phone=r8, email=r9, address=r10, shop=r11)
            q.save()
            message="OK-"+str(q.id)
        except Exception as e:
            message="ER-"+str(e) 
    else:
        message="NO-"
        
    return HttpResponse(message)


@csrf_exempt
def reqmech(request):
    if request.method == "POST":
        r1=request.POST.get('mechid')
        r2=request.POST.get('usrid')
        r3=request.POST.get('damage')
        t=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        from minor.models import trnx
        try:
            q=trnx(time=t, usrid=r2, mechid=r1)
            q.save()
            message="OK-"+str(q.id)
        except Exception as e:
            message="ER-"+str(e)
    else:
        message="NO-"
    return HttpResponse(message)

def chkreq(request):
    if request.method == "GET":
        r1=request.GET.get('time')
        t1=datetime.strptime(r1, '%Y-%m-%d %H:%M:%S')
        r2=request.GET.get('mechid')
        t=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        from minor.models import trnx
    else:
        message="NO-"
        
    return HttpResponse(message)


@csrf_exempt
def loginusr(request):
    if request.method == "POST":
        r1=request.POST.get('username')
        r2=request.POST.get('password')
        from minor.models import rider
        try:
            q=rider.objects.get(usrname=r1)
            if q.password == r2:
                message="OK-"+str(q.id)
            else:
                message="OK-PASSWORD"
        except Exception as e:
            message="ER-"+str(e) 
    else:
        message="NO-"
        
    return HttpResponse(message)

def findmech(request):
    if request.method == "GET":
        #r1=request.GET.get('usrid')
        r2=request.GET.get('long')
        r3=request.GET.get('lat')
        r4=request.GET.get('radius')
        rlat1=float(r3)+float(r4)/110
        rlat2=float(r3)-float(r4)/110
        rlon1=float(r2)+float(r4)/100
        rlon2=float(r2)-float(r4)/100
        from minor.models import mechanic
        q=mechanic.objects.filter(mlat__lte=rlat1)
        q1=q.filter(mlat__gte=rlat2)
        q2=q1.filter(mlon__lte=rlon1)
        q3=q2.filter(mlon__gte=rlon2)
        data = serializers.serialize('json', q3)
        message="OK-"+str(data)

    else:
        message="NO-"
        
    return HttpResponse(message)
       
@csrf_exempt
def loginmech(request):
    if request.method == "POST":
        r1=request.POST.get('username')
        r2=request.POST.get('password')
        from minor.models import mechanic
        try:
            q=mechanic.objects.get(usrname=r1)
            if q.password == r2:
                message="OK-"+str(q.id)
            else:
                message="OK-PASSWORD"
        except Exception as e:
            message="ER-"+str(e) 
    else:
        message="NO-"
        
    return HttpResponse(message)







    

        
 
