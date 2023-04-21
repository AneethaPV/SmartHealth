from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)


class user(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    gender=models.CharField(max_length=10)


class healthdetails(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    dob=models.DateField()
    height=models.IntegerField()
    cweight=models.IntegerField()
    bmi=models.IntegerField()



class medicalcondition(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    date=models.DateField()
    diabetes=models.CharField(max_length=10, default='0')
    cholestrol=models.CharField(max_length=10, default='0')
    pressure=models.CharField(max_length=10, default='0')



class nutritionist(models.Model):
    name=models.CharField(max_length=30)
    image=models.FileField()
    email=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20)
    experience=models.IntegerField()
    license=models.CharField(max_length=30)


class reminder(models.Model):
    lid=models.ForeignKey(login, on_delete=models.CASCADE)
    medicine=models.CharField(max_length=30)
    startdate=models.DateField()
    enddate=models.DateField()
    num=models.IntegerField()



class doseinfo(models.Model):
    mid=models.ForeignKey(reminder, on_delete=models.CASCADE)
    time=models.CharField(max_length=200)


class notification(models.Model):
    notification=models.CharField(max_length=50)
    time=models.CharField(max_length=200)


class feedback(models.Model):
    uid=models.ForeignKey(user, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=30)
    date=models.DateField()
    reply=models.CharField(max_length=30)


class foodcalories(models.Model):
    food=models.CharField(max_length=30)
    image=models.FileField()
    quantity = models.CharField(max_length=30)
    calories=models.IntegerField()
    proteins = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()
    fiber = models.FloatField()



class calories(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    date=models.DateField()
    breakfast=models.IntegerField()
    lunch = models.IntegerField()
    dinner=models.IntegerField()


class healthblog(models.Model):
    caption=models.CharField(max_length=50)
    blog=models.CharField(max_length=500)
    image=models.FileField()
    date=models.DateField()


class reviewrating(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    nid = models.ForeignKey(nutritionist, on_delete=models.CASCADE)
    review=models.CharField(max_length=60)
    rating=models.FloatField()
    date = models.DateField()
