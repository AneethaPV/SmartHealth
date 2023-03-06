import json
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from health.models import *


def logins(request):
    return render(request,"loginindex.html")


def adminlogin(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']

    try:
        ob=login.objects.get(username=username,password=password)
        if ob.usertype=='admin':
            return HttpResponse('''<script> alert("Welcome to Admin Homepage"); window.location='/home' </script>''')
        else:
            return HttpResponse('''<script> alert("Invalid"); window.location='/' </script>''')
    except Exception as e:
        return HttpResponse('''<script> alert("Invalid"); window.location='/' </script>''')



def home(request):
    return render(request,"Home.html")


def view_user(request):
    ob=user.objects.all()
    return render(request,"ViewUser.html",{'val':ob})


def view_nutritionist(request):
    ob = nutritionist.objects.all()
    return render(request,"ViewNutritionist.html",{'val':ob})


def add_nutritionist(request):
    return render(request,"AddNutritionist.html")


def add_nutritionist1(request):
    image=request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(image.name,image)

    name = request.POST['textfield']

    email = request.POST['textfield2']
    mobile = request.POST['textfield3']
    gender = request.POST['select1']
    qualification = request.POST['textfield4']
    experience = request.POST['textfield5']
    license = request.POST['textfield6']
    ob=nutritionist()
    ob.name=name
    ob.image=image
    ob.email = email
    ob.mobile = mobile
    ob.gender = gender
    ob.qualification = qualification
    ob.experience = experience
    ob.license = license
    ob.save()
    return HttpResponse('''<script> alert("Added successfully"); window.location='/view_nutritionist' </script>''')



def view_notification(request):
    ob=notification.objects.all()
    return render(request,"ViewNotification.html",{'val':ob})


def add_notification(request):
    return render(request,"AddNotification.html")


def add_notification1(request):
    notifications = request.POST['textfield']
    time = request.POST['textfield1']
    ob=notification()
    ob.notification=notifications
    ob.time=time
    ob.save()
    return HttpResponse('''<script> alert("Added successfully"); window.location='/view_notification' </script>''')


def delete_notification(request,id):
    ob=notification.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted successfully"); window.location='/view_notification' </script>''')



def edit_notification(request,id):
    ob=notification.objects.get(id=id)
    request.session['nid']=id
    return render(request,"EditNotification.html",{'val':ob})


def edit_notification1(request):
    notifications = request.POST['textfield']
    time = request.POST['textfield1']
    ob=notification.objects.get(id=request.session['nid'])
    ob.notification=notifications
    ob.time=time
    ob.save()
    return HttpResponse('''<script> alert("Updated successfully"); window.location='/view_notification' </script>''')


def view_healthblog(request):
    ob=healthblog.objects.all()
    return render(request,"ViewHealthBlog.html",{'val':ob})


def add_healthblog(request):
    return render(request,"AddHealthBlog.html")


def add_healthblog1(request):
    blog = request.POST['textfield']
    ob=healthblog()
    ob.blog=blog
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script> alert("Added successfully"); window.location='/view_healthblog' </script>''')



def edit_healthblog(request,id):
    ob=healthblog.objects.get(id=id)
    request.session['hid']=id
    return render(request,"EditHealthBlog.html",{'val':ob})



def edit_healthblog1(request):
    blog = request.POST['textfield']
    ob=healthblog.objects.get(id=request.session['hid'])
    ob.blog=blog
    ob.save()
    return HttpResponse('''<script> alert("Updated successfully"); window.location='/view_healthblog' </script>''')


def delete_healthblog(request,id):
    ob=healthblog.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted successfully"); window.location='/view_healthblog' </script>''')


def view_feedback(request):
    ob=feedback.objects.all()
    return render(request,"ViewFeedback.html",{'val':ob})


def reply_feedback(request,id):
    request.session['fid']=id
    return render(request,"ReplyFeedback.html")


def reply_feedback1(request):
    reply=request.POST['textfield']
    ob=feedback.objects.get(id=request.session['fid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script> alert("Replied successfully"); window.location='/view_feedback' </script>''')




























#######################################################webservice###########################################



def logincode(request):
    username = request.POST['username']
    password = request.POST['password']
    ob = login.objects.get(username=username, password=password)
    if ob is None:
        data = {"task": "invalid"}
    else:
        data = {"task": "valid","id":ob.id}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def reg(request):
  try:
    print (request.POST)
    name=request.POST['name']
    email=request.POST['email']
    mobile = request.POST['mobile']
    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST['gender']
    lob = login()
    lob.username = username
    lob.password = password
    lob.usertype = 'user'
    lob.save()
    userob=user()
    userob.name=name
    userob.email=email
    userob.mobile=mobile
    userob.gender=gender
    userob.lid=lob
    userob.save()
    data = {"task":"success","lid":userob.lid.id}
    r = json.dumps(data)
    return HttpResponse(r)
  except Exception as e:
      data = {"task": "incorrect format"}
      r = json.dumps(data)
      return HttpResponse(r)


def hinfo(request):
  # try:
    print (request.POST)
    lid = request.POST['lid']
    dob1=request.POST['dob']
    height1=request.POST['height']
    cweight1 = request.POST['cweight']
    gweight1 = request.POST['gweight']
    medcond1 = request.POST['medcond']
    print(lid,dob1,height1,cweight1,gweight1,medcond1,"=================================")
    hob=healthdetails()
    hob.dob=dob1
    hob.height=height1
    hob.cweight=cweight1
    hob.gweight=gweight1
    hob.bmi=0
    hob.medcond = medcond1
    hob.lid=login.objects.get(id=lid)
    hob.save()
    data = {"task":"success"}
    r = json.dumps(data)
    return HttpResponse(r)
  # except Exception as e:
  #     data = {"task": "incorrect format"}
  #     r = json.dumps(data)
  #     return HttpResponse(r)
