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
    message=""
    if True:
        #message=request.GET.get('data')+" "
        import os
        #message=message+os.path.abspath(__file__)+" "
        #message=message+os.path.dirname(os.path.abspath(__file__))
        mid=0
        name="admin"
        message=os.path.dirname(os.path.abspath(__file__))+"\\mechanic\\"+str(mid)+"_"+name
    
    return HttpResponse(message)

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

##########################################################

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
            userinit(r3,q.id)
        except Exception as e:
            message="ER-"+str(e) 
    else:
        message="NO-"
        
    return HttpResponse(message)


@csrf_exempt
def direction(request):
    if request.method == "POST":
        message=""
        import googlemaps
        gmaps = googlemaps.Client(key='AIzaSyCx9Nzdo46F8gnQWqZL0swe6kFE0G9JANU')




    return HttpResponse(message)

def getitem(request):
    from minor.models import price
    q=price.objects.all()
    message="OK-"+str(serializers.serialize('json', q))
    return(message)

def getmech(request):
    if request.method == "POST":
        r1=request.POST.get('mechid')
        from minor.models import mechanic
        try:
            q=mechanic.objects.get(id=r1)



@csrf_exempt
def chkaccept(request):
    if request.method == "POST":
        r1=request.POST.get('usrid')
        r2=request.POST.get('trnxid')
        from minor.models import trnx
        try:
            q=trnx.objects.get(id=r2,usrid=r1)
        except trnx.DoesNotExist:
            return "NO-No transaction"
        if q.ack == True:
            from minor.models import rider
            q1=rider.objects.get(id=r1)
            path=os.path.dirname(os.path.abspath(__file__))
            path=path+"\\user\\"+str(r1)+"_"+q1.f_name+"ack.txt"
            try:
                f=open(path,'a+')
                t=datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
                f.write(t+"->"+str(q1)+"\n")
                f.close()
            except Exception as e:
                errlog('uid='+str(uid)+str(e))
            try:
                q.delete()
                message="OK-ACK"
            except Exception as e:
                message="ER-"+str(e)
        elif q.ack == False:
            message="OK-PENDING"

        return(message)




@csrf_exempt
def reqmech(request):
    if request.method == "POST":
        r1=request.POST.get('mechid')
        r2=request.POST.get('usrid')
        r3=request.POST.get('damage')
        r4=request.POST.get('budget')
        r5=request.POST.get('package')
        #split=r5.split('-',r5.count())#starting string p0=no package, p1--p3=small m l,then item id
        
        
        t=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        from minor.models import trnx
        try:
            q=trnx(time=t, usrid=r2, mechid=r1, damage=r3, budget=r4)
            q.save()
            message="OK-"+str(q.id)
            from minor.models import rider
            q1=rider.objects.get(id=r2)
            path=os.path.dirname(os.path.abspath(__file__))
            path=path+"\\user\\"+str(r2)+"_"+q1.f_name+"request.txt"
            f=open(path,"w")
            f.write(r5)
            f.close()
        except Exception as e:
            message="ER-"+str(e)
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

@csrf_exempt
def findmech(request):
    if request.method == "POST":
        #r1=request.GET.get('usrid')
        r2=request.POST.get('long')
        r3=request.POST.get('lat')
        r4=request.POST.get('radius')
        from geopy.distance import vincenty
        latf=vincenty(r3,r3+1.0).meters
        latf=latf*radius
        longf=vincenty(r2,r2+1.0).meters
        longf=longf*radius
        rlat1=float(r3)+float(r4)/latf
        rlat2=float(r3)-float(r4)/latf
        rlon1=float(r2)+float(r4)/longf
        rlon2=float(r2)-float(r4)/longf
        from minor.models import avail
        q=avail.objects.filter(mlat__lte=rlat1)
        q1=q.filter(mlat__gte=rlat2)
        q2=q1.filter(mlon__lte=rlon1)
        q3=q2.filter(mlon__gte=rlon2)
        data = serializers.serialize('json', q3)
        message="OK-"+str(data)

    else:
        message="NO-"
        
    return HttpResponse(message)


def userinit(name, uid): 
    import os
    import sys
    path=os.path.dirname(os.path.abspath(__file__))
    path=path+'\\user\\'+str(uid)+"_"+name
    if not os.path.exists(path):
        os.makedirs(path)
    #t=datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    try:
        f=open(str(path+"\\transactions.txt"),'a+')
        f.close()
    except Exception as e:
        errlog('uid='+str(uid)+str(e))

'''def available(mechid):
    if request.method="GET":
        r1=request.GET.get('mechid')
        from minor.models import avail
        q=avail.objects.get(mechid=r1)
        if q.isavail == True:
            return
'''

###########################################################################

@csrf_exempt
def regmech(request):
    import thread

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

        mechinit(r3,q.id) 
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



@csrf_exempt
def chkreq(request):
    if request.method == "POST":
        r1=request.POST.get('time')
        r2=request.POST.get('mechid')
        try:
            t1=datetime.strptime(r1, '%Y-%m-%d %H:%M:%S')
            
            from minor.models import trnx  
            q=trnx.objects.filter(time__gte=t1)
            q1=q.filter(mechid=r2)
            message="OK-"+str(serializers.serialize('json', q1))
        except Exception as e:
            message="ER-"+str(e)    
    else:
        message="NO-"
        
    return HttpResponse(message)   

def mechinit(name, mid): 
    import os
    import sys
    path=os.path.dirname(os.path.abspath(__file__))+"\\mechanic\\"+str(mid)+"_"+name
    if not os.path.exists(path):
        os.makedirs(path)
    t=datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    try:
        f=open(path+"\\"+t+'.txt','r+')
        f.close()
    except Exception as e:
        errlog('mechid='+str(mid)+str(e))


def errlog(strl):
    import sys,os  
    path=os.path.dirname(os.path.abspath(__file__))+"\\errlog.txt"
    f=open(path,'a+')
    t=datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    f.write(t+"->"+strl+"\n")
    f.close()



#c:\django\mysite\minor