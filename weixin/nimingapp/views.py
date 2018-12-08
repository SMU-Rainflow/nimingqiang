from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
import time
from nimingapp.models import Message
# Create your views here.
def index(request):
	if(request.method=='GET'):
		t1 =time.localtime()
		data =str(t1.tm_year)+'年'+str(t1.tm_mon)+'月'+str(t1.tm_mday)+'日  '+str(t1.tm_hour)+':'+str(t1.tm_min)+':'+str(t1.tm_sec)
		Data=Message.objects.all()
		# sex =Data.sex
		# mess = Data.mess
		# year=Data.year
		context={
			'Data':Data,
			'time':data,
		}
		return render(request,'index.html',context)
	

def send(request):
	 return render(request,'send.html')

def recive(request):
	if(request.method=='POST'):
		t1 =time.localtime()
		data1 =str(t1.tm_year)+'年'+str(t1.tm_mon)+'月'+str(t1.tm_mday)+'日  '+str(t1.tm_hour)+':'+str(t1.tm_min)+':'+str(t1.tm_sec)
		sex0 = request.POST['sex']
		year0 = request.POST['year']
		mess0 = request.POST['mess']
		time0 = data1 
		newObj = Message(sex = sex0,year = year0,mess =mess0,time=time0)
		newObj.save()
		t1 =time.localtime()
		data =str(t1.tm_year)+'年'+str(t1.tm_mon)+'月'+str(t1.tm_mday)+'日  '+str(t1.tm_hour)+':'+str(t1.tm_min)+':'+str(t1.tm_sec)
		Data=Message.objects.all()
		Data=Message.objects.all()
		# sex =Data.sex
		# mess = Data.mess
		# year=Data.year
		context={
			'Data':Data,
			'time':data,
		}

		return render(request,'index.html',context)
