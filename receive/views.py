from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from time import ctime
import json
from receive.models import SoundOrigin, ImageOrigin, CurrentOrigin, VoltageOrigin, UpdataTime, RobotOrigin
import base64

def sound(request):
    dict={}
    if request.method == 'POST':
        req = json.loads(request.body)
        #print(req)
        for key,values in req.items():
            time = key
            data = values
            #print (key, values)
        t = UpdataTime.objects.get_or_create(time=time)[0]
        t.save()
        for i in range(0,1000):
            p = SoundOrigin(time=t)
            p.voice = data[i]
            p.save()
        dict['message'] = 'Data log success'
        dict['time'] = str(ctime())
    else:
        dict['message'] = 'Data log fail'
        dict['time'] = str(ctime())     
    j = json.dumps(dict)
    return HttpResponse(j)

def current(request):
    dict={}
    if request.method == 'POST':
        req = json.loads(request.body)
        #print(req)
        for key,values in req.items():
            time = key
            data = values
            #print (key, values)
        t = UpdataTime.objects.get_or_create(time=time)[0]
        t.save()
        for i in range(0,1000):
            p = CurrentOrigin(time=t)
            p.current = data[i]
            p.save()
        dict['message'] = 'Data log success'
        dict['time'] = str(ctime())
    else:
        dict['message'] = 'Data log fail'
        dict['time'] = str(ctime())     
    j = json.dumps(dict)
    return HttpResponse(j)

def voltage(request):
    dict={}
    if request.method == 'POST':
        req = json.loads(request.body)
        #print(req)
        for key,values in req.items():
            time = key
            data = values
            #print (key, values)
        c = UpdataTime.objects.get_or_create(time=time)[0]
        c.save()
        t = VoiceOrigin.objects.get_or_create(index=0)[0]
        t.time = time
        for i in range(0,100):
            p = VoltageOrigin(time=t)
            p.voltage = data[i]
            p.save()
        dict['message'] = 'Data log success'
        dict['time'] = str(ctime())
    else:
        dict['message'] = 'Data log fail'
        dict['time'] = str(ctime())     
    j = json.dumps(dict)
    return HttpResponse(j)

def DAQ_Input(request):
    dict={}
    if request.method == 'POST':
        req = json.loads(request.body)
        #print(req)
        for key,values in req.items():
            time = key
            data = values
            print (time)
        t = UpdataTime.objects.get_or_create(time=time)[0]
        t.save()
        Sound = data['Sound']
        Current = data['Current']
        Voltage = data['Voltage']
        for i in range(0,len(Sound)):
            s = SoundOrigin(time=t)
            s.sound = Sound[i]
            s.save()
        for i in range(0,len(Current)):
            c = CurrentOrigin(time=t)
            c.current = Current[i]
            c.save()
        for i in range(0,len(Voltage)):
            v = VoltageOrigin(time=t)
            v.voltage = Voltage[i]
            v.save()
        dict['message'] = 'Data log success'
        dict['time'] = str(ctime())
    else:
        dict['message'] = 'Data log fail'
        dict['time'] = str(ctime())     
    j = json.dumps(dict)
    return HttpResponse(j)

def CCD_Input(request):
    dict={}
    if request.method == 'POST':
        req = json.loads(request.body)
        #print (req)
        for key,values in req.items():
            time = key
            data = values
            #print (time)
        t = UpdataTime.objects.get_or_create(time=time)[0]
        t.save()
        p = ImageOrigin(time=t)
        p.image = data
        p.save()
        dict['message'] = 'Data log success'
        dict['time'] = str(ctime())
    else:
        dict['message'] = 'Data log fail'
        dict['time'] = str(ctime())
    j = json.dumps(dict)
    return HttpResponse(j)

def Robot_Input(request):
    dict={}
    if request.method == 'POST':
        req = json.loads(request.body)
        Odata =req
        #print (Odata)
        for key,values in Odata.items():
            time = key
            data = values
            print (time)
        t = UpdataTime.objects.get_or_create(time=time)[0]
        t.save()
        p = RobotOrigin.objects.get_or_create(time=t)[0]
        p.robot = data
        p.save()
        dict['message'] = 'Data log success'
        dict['time'] = str(ctime())
    else:
        dict['message'] = 'Data log fail'
        dict['time'] = str(ctime())
    j = json.dumps(dict)
    return HttpResponse(j)

def show(request):
    return render(request, 'receive/show.html')

def current_refresh(request):
    if request.method == 'GET':
        pid = request.GET['currentid']
        context = []
        index = int(pid)
        for i in range(0, 100):
            context.append(CurrentOrigin.objects.order_by('id')[index].current)
            index += 1
        #print(context)
        #print(json.dumps(context))
        return JsonResponse(json.dumps(context), safe=False)

def voltage_refresh(request):
    if request.method == 'GET':
        pid = request.GET['currentid']
        context = []
        index = int(pid)
        for i in range(0, 100):
            context.append(VoltageOrigin.objects.order_by('id')[index].voltage)
            index += 1
        #print(context)
        #print(json.dumps(context))
        return JsonResponse(json.dumps(context), safe=False)

def sound_refresh(request):
    if request.method == 'GET':
        pid = request.GET['currentid']
        context = []
        index = int(pid)
        for i in range(0, 100):
            context.append(SoundOrigin.objects.order_by('id')[index].sound)
            index += 1
        #print(context)
        #print(json.dumps(context))
        return JsonResponse(json.dumps(context), safe=False)

def image_refresh(request):
    if request.method == 'GET':
        pid = request.GET['currentid']
        data = ImageOrigin.objects.order_by('-id')[0]
        context = {}
        context['id'] = data.id
        context['image'] = data.image
        #print(context)
        #print(json.dumps(context))
    return JsonResponse(json.dumps(context), safe=False)

def robot_refresh(request):
    if request.method == 'GET':
        pid = request.GET['currentid']
        data = RobotOrigin.objects.order_by('-id')[0]
        context = {}
        context['id'] = data.id
        context['robot'] = data.robot
        #print(context)
        #print(json.dumps(context))
    return JsonResponse(json.dumps(context), safe=False)

def output(request):
    with open('sound.txt', 'w') as s:
        for data in SoundOrigin.objects.all():
            print(data.time.time, ',' ,data.sound, file=s)
    with open('current.txt', 'w') as s:
        for data in CurrentOrigin.objects.all():
            print(data.time.time, ',' ,data.current, file=s)
    with open('voltage.txt', 'w') as s:
        for data in VoltageOrigin.objects.all():
            print(data.time.time, ',' ,data.voltage, file=s)
    with open('image.txt', 'w') as s:
        for data in ImageOrigin.objects.all():
            print(data.time.time, ',' ,data.image, file=s)
    with open('robot.txt', 'w') as s:
        for data in RobotOrigin.objects.all():
            print(data.time.time, ',' ,data.robot, file=s)
    return HttpResponse('OK')
