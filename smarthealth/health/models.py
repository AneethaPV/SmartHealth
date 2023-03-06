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
    height=models.FloatField()
    cweight=models.FloatField()
    gweight=models.FloatField()
    medcond=models.CharField(max_length=200)
    bmi=models.FloatField()


class nutritionist(models.Model):
    name=models.CharField(max_length=30)
    image=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mobile=models.IntegerField()
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20)
    experience=models.IntegerField()
    license=models.CharField(max_length=30)


class reminder(models.Model):
    lid=models.ForeignKey(login, on_delete=models.CASCADE)
    medicine=models.CharField(max_length=30)
    startdate=models.DateField()
    enddate=models.DateField()
    dose=models.TimeField()


class notification(models.Model):
    notification=models.CharField(max_length=50)
    time=models.TimeField()


class feedback(models.Model):
    uid=models.ForeignKey(user, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=30)
    date=models.DateField()
    reply=models.CharField(max_length=30)


class foodcalories(models.Model):
    food=models.CharField(max_length=30)
    image=models.CharField(max_length=100)
    calories=models.IntegerField()


class calories(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    date=models.DateField()
    breakfast=models.IntegerField()
    lunch = models.IntegerField()
    dinner=models.IntegerField()


class healthblog(models.Model):
    blog=models.CharField(max_length=50)
    image=models.CharField(max_length=100)
    date=models.DateField()