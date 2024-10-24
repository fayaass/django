from django.shortcuts import render,redirect
from django.http import HttpResponse
def fun1(req):
    print("hai")
    a={11,12}
    return HttpResponse("welcome")
def fun2(req):
    return HttpResponse("hello")
def task(req,salary,year):
    if year>5:
        bonus=(salary/100*5)
        return HttpResponse(bonus)
    else:
        return HttpResponse('year of service lessthan 5')
def task1(req,city):
    if city=='Delhi':
        return HttpResponse('Red fort')
    elif city=='Agra':
        return HttpResponse('Taj mahal')
    elif city=='Jaipur':
        return HttpResponse('Jal mahal')
    else:
        return HttpResponse('invalid input')
def task2(req,num):
    n=num%10
    if n%3==0:
        return HttpResponse('divisible by 3')
    else:
        return HttpResponse('not divisible by 3')
    
def task3(req,day):
    if day==1:
        return HttpResponse('sunday')
    elif day==2:
        return HttpResponse('monday')
    elif day==3:
        return HttpResponse('tuesday')
    elif day==4:
        return HttpResponse('wednesday')
    elif day==5:
        return HttpResponse('thursday')
    elif day==6:
        return HttpResponse('friday')
    elif day==7:
        return HttpResponse('saturday')
    else:
        return HttpResponse('invalid')

def task4(req,cost):
    if cost>100000:
        return HttpResponse(cost*0.15)
    elif cost>50000 and cost<=100000:
        return HttpResponse(cost*0.10)
    else:
        return HttpResponse(cost*0.05)

def task5(req,unit):
    if unit<=100:
        return HttpResponse(unit*0)
    elif unit>100 and unit<=200:
        return HttpResponse((unit-100)*5)
    else:
        return HttpResponse((unit-200)*10+500)

        # Create your views here.

def demo(req):
    a={'name':'abc','age':22},{'name':'bbb','age':22},{'name':'ccc','age':22}
    return render(req,'demo.html',{'data':a})


users=[{'id':'21','name':'aaa','age':22,'email':'aaa@gmail'},{'id':'22','name':'bbb','age':23,'email':'bbb@gmail'},{'id':'23','name':'ccc','age':24,'email':'ccc@gmail'}]

def display(req):
    return render(req,'display_user.html',{'users':users})

def user_reg(req):
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        users.append({'id':id,'name':name,'age':age,'email':email})
        return redirect(display)
    else:
        print(req.method)
        return redirect(display)



    