from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")
def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,'user_add.html')
def tpl(request):
    name="韩超发方法"
    roles=["管理员","CEO","保安"]
    user_info={"name":"郭智","salary":100000,'role':"CTO"}
    data_list=[
        {"name":"郭智","salary":100000,'role':"CTO"},
        {"name":"李白","salary":100000,'role':"CTO"},
        {"name":"王维","salary":100000,'role':"CTO"}
    ]
    return render(request,"tpl.html",{"n1":name,"n2":roles,"n3":user_info,"n4":data_list})
def weather(req):
    import requests
    res=requests.get("https://api.open-meteo.com/v1/forecast?latitude=30.67&longitude=104.07&current=temperature_2m" )
    data_list=res.json()
    print(data_list)
    return render(req,"weather.html",{"weather_list":data_list})
def something(request):
    return redirect("https://www.baidu.com")

def login(request):
    if request.method=="GET":
        return render(request,"login.html")

    username=request.POST.get("user")
    password=request.POST.get("pwd")
    if username=="root" and password=="123":
        return redirect("http://www.chinaunicom.com.cn/")

    return render(request,"login.html",{"error_msg":"用户名或密码错误！"})
from app00.models import UserInfo,Department
def orm(request):
   '''Department.objects.create(title="销售部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="运营部")
    UserInfo.objects.create(name="张三",password="123",age=18)
    UserInfo.objects.create(name="李四",password="666",age=29)
    UserInfo.objects.create(name="王五",password="666",age=39)
    return HttpResponse("成功")
'''
   #删除
   #UserInfo.objects.filter(id=3).delete()
   #Department.objects.all().delete()

   #获取数据
   #获取符合条件的所有数据
   '''data_list=UserInfo.objects.all()
   print(data_list)
   for user in data_list:
       print(user.id,user.name,user.password,user.age)

   data_list=UserInfo.objects.filter(id=1)
   print(data_list)

   row_obj=UserInfo.objects.filter(id=1).first()
   print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)
   return HttpResponse("成功")
'''

   #4.更新数据
   UserInfo.objects.filter(id=2).update(age=999)
   UserInfo.objects.filter(name="李四").update(age=888)
   return  HttpResponse("成功")

def info_list(request):
    #获取数据库所有的用户信息
    data_list=UserInfo.objects.all()
    #渲染返回给用户
    return render(request,"info_list.html",{"data_list":data_list})
def info_add(request):
    if request.method=="GET":
        return render(request,"info_add.html")
    # 获取用户提交的数据
    user=request.POST.get("user")
    pwd=request.POST.get("pwd")
    age=int(request.POST.get("age"))
    # 添加到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)
    # 自动跳转
    return redirect("/info/list/")

def info_delete(request):
    id=request.GET.get("nid")
    UserInfo.objects.filter(id=id).delete()
    return redirect("/info/list/")

