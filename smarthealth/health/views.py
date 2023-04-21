import json
from datetime import datetime
from time import strftime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from health.models import *

from django.core.mail import send_mail
import random

from smarthealth.pp import predict


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
    ob.image=fp
    ob.email = email
    ob.mobile = mobile
    ob.gender = gender
    ob.qualification = qualification
    ob.experience = experience
    ob.license = license
    ob.save()
    return HttpResponse('''<script> alert("Added successfully"); window.location='/view_nutritionist' </script>''')


def edit_nutritionist(request,id):
    ob=nutritionist.objects.get(id=id)
    request.session['hid']=id
    return render(request,"EditNutritionist.html",{'val':ob})


def edit_nutritionist1(request):
    try:
        image = request.FILES['file']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)
        name = request.POST['textfield']
        email = request.POST['textfield2']
        mobile = request.POST['textfield3']
        gender = request.POST['select1']
        qualification = request.POST['textfield4']
        experience = request.POST['textfield5']
        license = request.POST['textfield6']
        ob=nutritionist.objects.get(id=request.session['hid'])
        ob.name = name
        ob.image = fp
        ob.email = email
        ob.mobile = mobile
        ob.gender = gender
        ob.qualification = qualification
        ob.experience = experience
        ob.license = license
        ob.save()
        return HttpResponse('''<script> alert("Updated successfully"); window.location='/view_nutritionist' </script>''')
    except Exception as e:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        mobile = request.POST['textfield3']
        gender = request.POST['select1']
        qualification = request.POST['textfield4']
        experience = request.POST['textfield5']
        license = request.POST['textfield6']
        ob = nutritionist.objects.get(id=request.session['hid'])
        ob.name = name
        ob.email = email
        ob.mobile = mobile
        ob.gender = gender
        ob.qualification = qualification
        ob.experience = experience
        ob.license = license
        ob.save()
        return HttpResponse('''<script> alert("Updated successfully"); window.location='/view_nutritionist' </script>''')



def delete_nutritionist(request,id):
    ob=nutritionist.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted successfully"); window.location='/view_nutritionist' </script>''')




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
    image = request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)
    caption=request.POST['textfield2']
    blog = request.POST['textfield']
    ob=healthblog()
    ob.caption=caption
    ob.blog=blog
    ob.image=fp
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script> alert("Added successfully"); window.location='/view_healthblog' </script>''')



def edit_healthblog(request,id):
    ob=healthblog.objects.get(id=id)
    request.session['hid']=id
    return render(request,"EditHealthBlog.html",{'val':ob})



def edit_healthblog1(request):
    try:
        image = request.FILES['file']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)
        caption = request.POST['textfield2']
        blog = request.POST['textfield']
        ob=healthblog.objects.get(id=request.session['hid'])
        ob.caption=caption
        ob.blog=blog
        ob.image=fp
        ob.save()
        return HttpResponse('''<script> alert("Updated successfully"); window.location='/view_healthblog' </script>''')
    except Exception as e:
        caption = request.POST['textfield2']
        blog = request.POST['textfield']
        ob = healthblog.objects.get(id=request.session['hid'])
        ob.caption = caption
        ob.blog = blog
        ob.save()
        return HttpResponse('''<script> alert("Updated successfully"); window.location='/view_healthblog' </script>''')




def delete_healthblog(request,id):
    ob=healthblog.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted successfully"); window.location='/view_healthblog' </script>''')



def view_foodcalories(request):
    ob=foodcalories.objects.all()
    return render(request,"ViewFoodcalories.html",{'val':ob})


def add_foodcalories(request):
    return render(request,"AddFoodcalories.html")


def add_foodcalories1(request):
    image = request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)
    food=request.POST['textfield']
    calories = request.POST['textfield2']
    proteins = request.POST['textfield3']
    carbs = request.POST['textfield4']
    fats = request.POST['textfield5']
    fiber = request.POST['textfield6']
    quantity=request.POST['select1']
    ob=foodcalories()
    ob.food=food
    ob.calories=calories
    ob.proteins = proteins
    ob.carbs = carbs
    ob.fats = fats
    ob.calories = calories
    ob.fiber=fiber
    ob.image=fp
    ob.save()
    return HttpResponse('''<script> alert("Added successfully"); window.location='/view_foodcalories' </script>''')



def delete_foodcalories(request,id):
    ob=foodcalories.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("Deleted successfully"); window.location='/view_foodcalories' </script>''')




def view_review(request):
    ob=nutritionist.objects.all()
    return render(request,"ViewReview.html",{'val':ob})



def search(request):
    nutri=request.POST['select']
    ob1=reviewrating.objects.filter(nid__id=nutri)
    ob=nutritionist.objects.all()
    return render(request,"ViewReview.html",{'val1':ob1,'n':int(nutri),'val':ob})

def view_feedback(request):
    ob=feedback.objects.all()
    return render(request,"ViewFeedback.html",{'val':ob})


def reply_feedback(request,id):
    request.session['fid']=id
    return render(request,"ReplyFeedback.html")


def reply_feedback1(request):
    reply2=request.POST['textfield']
    ob=feedback.objects.get(id=request.session['fid'])
    ob1=user.objects.get(id=ob.id)
    mail = ob1.email
    print(mail,"++++++++++++++++++++++")
    send_mail('FEEDBACK REPLY', "FEEDBACK REPLY IS  -" + str(reply2), 'aneethawork@gmail.com', [mail], fail_silently=False)
    messages.info(request, "reply sent to your registered email address !!!")
    return HttpResponse('''<script> alert("Replied successfully"); window.location='/view_feedback' </script>''')




# def forgot_password(request):
#     if 'submit' in request.POST:
#         uname=request.POST['username']
#         g=login.objects.get(username=uname)
#         if g is not None:
#             a=random.randint(0000,9999)
#             g.password=(str(a))
#             g.save()
#             send_mail('FEEDBACK REPLY', "YOUR NEW PASSWORD IS  -" +str(a), 'email@gmail.com',[mail], fail_silently=False)
#             messages.info(request,"Password sent to your registered email address !!!")
#             return redirect('loginn')
#         else:
#             print('error==========')
#             messages.info(request,"Invalid Username or Email Adress!!!")
#             return redirect('forgot_password')
#
#     return render(request,'forgot_password.html')





def graph(request,id):
    ob = medicalcondition.objects.filter(lid__id=id)
    c=[]
    s=[]
    p=[]
    for i in ob:

        c.append(int(i.cholestrol))
        s.append(int(i.diabetes))
        p.append(int(i.pressure))
        i.d=str(i.date)
    return render(request, "Graph.html", {'val': ob,"c":c,"p":p,"s":s})




































#######################################################webservice###########################################



def logincode(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        ob = login.objects.get(username=username, password=password)
        if ob is None:
            data = {"task": "invalid"}
        else:
            data = {"task": "valid","id":ob.id}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except Exception as e:
        data = {"task": "incorrect format"}
        r = json.dumps(data)
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
  try:
    print (request.POST)
    lid = request.POST['lid']
    dob1=request.POST['dob']
    height1=request.POST['height']
    cweight1 = request.POST['cweight']
    diabetes1 = request.POST['diabetes']
    cholestrol1 = request.POST['cholestrol']
    pressure1 = request.POST['pressure']
    hd = request.POST['hd']
    print(lid,dob1,height1,cweight1,"=================================")
    hob=healthdetails()
    hob.dob=dob1
    hob.height=height1
    hob.cweight=cweight1
    hob.bmi=(int(cweight1)/(int(height1)*int(height1)))*10000
    hob.hd=hd
    hob.lid=login.objects.get(id=lid)
    hob.save()
    mob=medicalcondition()
    mob.date=datetime.today()
    mob.diabetes=diabetes1
    mob.cholestrol=cholestrol1
    mob.pressure=pressure1
    mob.lid = login.objects.get(id=lid)
    mob.save()
    data = {"task":"success"}
    r = json.dumps(data)
    return HttpResponse(r)
  except Exception as e:
      print(e,"kkkkkkkkkkkkkkkkkk")
      data = {"task": "incorrect format"}
      r = json.dumps(data)
      return HttpResponse(r)


def viewprofile(request):
    id=request.POST['lid']
    print(id)
    i=user.objects.get(lid=id)
    data=[]
    row={"name":i.name,"email":i.email,"mobile":i.mobile,"gender":i.gender,"id":i.lid.id}
    data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)


def updateprofile(request):
    id = request.POST['lid']
    name=request.POST['name']
    email=request.POST['email']
    mobile = request.POST['mobile']
    gender = request.POST['gender']
    i = user.objects.get(lid=id)
    i.name=name
    i.email=email
    i.mobile=mobile
    i.gender=gender
    i.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)


def viewhealth(request):
    id=request.POST['lid']
    print(id)
    i=healthdetails.objects.get(lid=id)
    data=[];
    row={"dob":str(i.dob),"height":i.height,"cweight":i.cweight,"bmi":i.bmi,"id":i.lid.id}
    data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)


def updatehealth(request):
    id = request.POST['lid']
    height=request.POST['height']
    cweight=request.POST['cweight']
    # hd=request.POST['hd']
    bmi = (int(cweight) / (int(height) * int(height))) * 10000
    i = healthdetails.objects.get(lid=id)
    i.height=height
    i.cweight=cweight
    i.bmi=bmi
    # i.hd=hd
    i.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)



def addrem(request):
  try:
    print (request.POST)
    lid = request.POST['lid']
    medicine=request.POST['medicine']
    sdate=request.POST['startdate']
    edate = request.POST['enddate']
    # num = request.POST['num']
    # d2 = request.POST['dose2']
    # d3 = request.POST['dose3']
    rob=reminder()
    rob.medicine=medicine
    rob.startdate = sdate
    rob.enddate=edate
    rob.num = "0"
    # rob.dose2 = d2
    # rob.dose3 = d3
    rob.lid=login.objects.get(id=lid)
    rob.save()
    data = {"task":"success","mid":rob.id}
    r = json.dumps(data)
    return HttpResponse(r)
  except Exception as e:
      data = {"task": "incorrect format"}
      r = json.dumps(data)
      return HttpResponse(r)


from datetime import datetime
def convert24(time):
	# Parse the time string into a datetime object
	t = datetime.strptime(time, '%I:%M %p')
	# Format the datetime object into a 24-hour time string
	return t.strftime('%H:%M:%S')

# print(convert24('11:21:30 PM')) # Output: '23:21:30'
# print(convert24('12:12:20 AM')) # Output: '00:12:20'



def adddose(request):
  # try:
    print(request.POST)
    mid = request.POST['mid']
    # time1 = request.POST['time']
    m2=""
    currenttime = request.POST['time']
    print(currenttime,"================")
    currenttime=convert24(currenttime)

    # ct=currenttime.split(' ')
    # print(ct[0],"==========")
    # ctt=strftime(ct[0])
    # if ctt >= "10:00" and ctt <= "13:00":
    #     if m2 >= "10:00" and m2 >= "12:00":
    #         m2 = ("""%s%s""" % (m2, " AM"))
    #         print("888888888888")
    #     else:
    #         m2 = ("""%s%s""" % (m2, " PM"))
    #         print("555555555555")
    # else:
    #     m2 = ("""%s%s""" % (m2, " PM"))
    # from datetime import datetime
    # m2 = datetime.strptime(m2, '%I:%M %p')
    # m2 = m2.strftime("%H:%M %p")
    # m2 = m2[:-3]
    # print(m2,"resultttttttttttttttttttt")
    # print(mid,currenttime)
    rob = doseinfo()
    rob.time = currenttime
    rob.mid = reminder.objects.get(id=mid)
    rob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)
  # except Exception as e:
  #     data = {"task": "incorrect format"}
  #     r = json.dumps(data)
  #     return HttpResponse(r)


def convert12(time):
	# Parse the time string into a datetime object
	t = datetime.strptime(time,'%H:%M:%S')
	# Format the datetime object into a 24-hour time string
	return t.strftime( '%I:%M %p')


def viewdose(request):
    mid = request.POST['mid']
    print(mid,"+++++++++++++++")
    res = doseinfo.objects.filter(mid__id=mid)
    data = []
    for i in res:
        # print(convert12(str(i.time)),str(i.time))
        row = {"dose": convert12(str(i.time)),"did":i.id}
        data.append(row)
    r = json.dumps(data)
    print(r,"+=========================")
    return HttpResponse(r)


#update no of dose
def ndose(request):
    mid = request.POST['mid']
    print(mid,"+++++++++++++++")
    ob=doseinfo.objects.filter(mid__id=mid)
    print(ob.count())
    ob1=reminder.objects.get(id=mid)
    ob1.num=str(ob.count())
    ob1.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)



def editdose(request):
    did = request.POST['did']
    dose1=request.POST['dose']
    ob=doseinfo.objects.get(id=did)
    ob.time=convert24(dose1)
    ob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)



#all reminders
def viewreminder(request):
    id=request.POST['lid']
    print(id)
    res=reminder.objects.filter(lid=id)
    data=[]
    for i in res:
        row={"medicine":str(i.medicine),"startdate":str(i.startdate),"enddate":str(i.enddate),"num":i.num,"mid":i.id}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)


#single reminder
def viewrem(request):
    id=request.POST['lid']
    mid=request.POST['mid']
    print(id)
    i=reminder.objects.get(lid__id=id,id=mid)
    data=[]
    row={"medicine":i.medicine,"startdate":str(i.startdate),"enddate":str(i.enddate),"num":i.num,"mid":i.id}
    data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)



def updaterem(request):
    id = request.POST['mid']
    medicine1=request.POST['medicine']
    startdate1=request.POST['startdate']
    enddate1 = request.POST['enddate']
    i = reminder.objects.get(id=id)
    i.medicine=medicine1
    i.startdate=startdate1
    i.enddate=enddate1
    i.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)




def delreminder(request):
    id=request.POST['mid']
    print(id)
    i = reminder.objects.get(id=id)
    i.delete()
    data = {"task":"success"}
    r = json.dumps(data)
    return HttpResponse(r)


def medcond(request):
    id = request.POST['lid']
    print(id)
    from django.db.models import Max
    obb=medicalcondition.objects.aggregate(Max('id'))
    i = medicalcondition.objects.get(id=obb['id__max'])
    data = []
    row = {"diabetes": i.diabetes, "cholestrol": i.cholestrol, "pressure": i.pressure,"id": i.lid.id}
    data.append(row)
    r = json.dumps(data)
    print(r,"==================================")
    return HttpResponse(r)


def updatemedcond(request):
    id = request.POST['lid']
    diabetes = request.POST['diabetes']
    cholestrol = request.POST['cholestrol']
    pressure = request.POST['pressure']
    i = medicalcondition()
    i.diabetes = diabetes
    i.cholestrol = cholestrol
    i.pressure = pressure
    i.date=datetime.today()
    i.lid=login.objects.get(id=id)
    i.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)


def viewmedcond(request):
    id=request.POST['lid']
    print(id)
    res=medicalcondition.objects.filter(lid=id).order_by('-id')
    data=[]
    for i in res:
        row={"date":str(i.date),"diabetes":i.diabetes,"cholestrol":i.cholestrol,"pressure":i.pressure,"mid":i.id}
        data.append(row)
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)


def pics(request):
    res=healthblog.objects.all()
    data=[]
    for i in res:
        row={"image":str(i.image),"caption":i.caption,"date":str(i.date),"blog":i.blog}
        data.append(row)
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)


# def hblog(request):
#     res=healthblog.objects.all()
#     data=[]
#     row={"image":str(i.image),"caption":i.caption,"date":i.date,"blog":i.blog}
#     data.append(row)
#     r=json.dumps(data)
#     print(r,"==============================")
#     return HttpResponse(r)


def addfeedback(request):
    try:
        print(request.POST)
        lid = request.POST['lid']
        feedbacks = request.POST['feedback']

        fob=feedback()
        fob.feedback = feedbacks
        fob.date = datetime.today()
        fob.reply='pending'

        fob.uid = user.objects.get(lid__id=lid)
        fob.save()
        data = {"task": "success"}
        r = json.dumps(data)
        return HttpResponse(r)
    except Exception as e:
        data = {"task": "incorrect format"}
        r = json.dumps(data)
        return HttpResponse(r)


def nutritionistdata(request):
    res=nutritionist.objects.all()
    data=[]
    for i in res:
        row={"name":i.name,"image":str(i.image),"email":i.email,"mobile":i.mobile,"gender":i.gender,"qualification":i.qualification,"experience":i.experience,"license":i.license,"nid":i.id}
        data.append(row)
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)


def nutritionistsearch(request):
    name1 = request.POST['name1']
    res=nutritionist.objects.filter(name__icontains=name1)
    data=[]
    for i in res:
        row={"name":i.name,"image":str(i.image),"email":i.email,"mobile":i.mobile,"gender":i.gender,"qualification":i.qualification,"experience":i.experience,"license":i.license}
        data.append(row)
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)



def foodcal(request):
    res=foodcalories.objects.all()
    data=[]
    for i in res:
        row={"food":i.food,"image":str(i.image),"quantity":i.quantity,"calories":i.calories,"proteins":i.proteins,"carbs":i.carbs,"fats":i.fats,"fiber":i.fiber}
        data.append(row)
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)


def foodsearch(request):
    name1 = request.POST['name1']
    res=foodcalories.objects.filter(food__icontains=name1)
    data=[]
    for i in res:
        row={"food":i.food,"image":str(i.image),"quantity":i.quantity,"calories":i.calories}
        data.append(row)
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)



def notification1(request):
    lid=request.POST['lid']
    res1 = notification.objects.all()
    res=''
    for i in res1:
        t=str(i.time).split(':')
        t=str(t[0])+":"+str(t[1])
        res = res + i.notification+ "#" + str(t) + "@"

    date = datetime.today()
    res1 = doseinfo.objects.filter(mid__lid__id=lid, mid__startdate__gte=date, mid__startdate__lte=date)

    for i in res1:
        t = str(i.time).split(':')
        t = str(t[0]) + ":" + str(t[1])
        res = res +"Medicine Notification "+ i.mid.medicine + "#" + str(t) + "@"

    data = {"task": res}
    r = json.dumps(data)
    print(r,"+=============================")
    return HttpResponse(r)



def reminder1(request):
    uid=request.POST['lid']
    date=datetime.today()
    res1 = doseinfo.objects.filter(mid__lid__id=uid,mid__startdate__gte=date,mid__startdate__lte=date)
    res=''
    print(len(res1),"++++++++++++++++++++")
    today = str(datetime.datetime.now()).split(" ")[1]

    # start time
    start_time = today
    end_time = "11:46:38"

    # convert time string to datetime
    t1 = datetime.strptime(start_time, "%H:%M:%S")
    print('Start time:', t1.time())

    for i in res1:
        end_time=str(i.time)
        t2 = datetime.strptime(end_time, "%H:%M:%S")
        print('End time:', t2.time())

        # get difference
        delta = t2 - t1

        # time difference in seconds
        print(f"Time difference is {delta.total_seconds()} seconds")

        # time difference in milliseconds
        ms = delta.total_seconds() * 1000
        print(f"Time difference is {ms} milliseconds")

        res = res + i.mid.medicine+ "#" + str(i.time) + "@"
    data = {"task": res}
    r = json.dumps(data)
    print(r,"+=============================")
    return HttpResponse(r)



def rating(request):
    lid=request.POST['lid']
    nid = request.POST['nid']
    review = request.POST['review']
    rating = request.POST['rating']
    ob=reviewrating()
    ob.rating=rating
    ob.review=review
    ob.date=datetime.today()
    ob.uid = user.objects.get(lid__id=lid)
    ob.nid = nutritionist.objects.get(id=nid)
    ob.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)






def nutrreview(request):
    from django.db import connection
    cursor = connection.cursor()
    nid = request.POST['nid']
    cursor.execute("SELECT AVG(`health_reviewrating`.`rating`) FROM `health_nutritionist` LEFT JOIN `health_reviewrating` ON `health_nutritionist`.id = `health_reviewrating`.nid_id WHERE `health_nutritionist`.`id`='"+nid+"'")
    row = cursor.fetchone()
    print(row[0])
    data = {'rating': row[0]}
    r=json.dumps(data)
    print(r,"==============================")
    return HttpResponse(r)


def predict1(request):
    gender = request.POST['gender']
    age = request.POST['age']
    height = request.POST['height']
    cweight = request.POST['cweight']
    fweight = request.POST['fweight']
    if gender == "Female":
        gender=0
    else:
        gender=1
    rr=[gender,age,float(height),float(cweight),fweight]
    print(rr,":*******************")
    res=predict(rr)
    print(res,"===========================")
    if res == 0:
        p="a.png"
    elif res == 1:
        p="b.png"
    else:
        p="c.png"
    data = {'task': 'success','res':p}
    r = json.dumps(data)
    return HttpResponse(r)

