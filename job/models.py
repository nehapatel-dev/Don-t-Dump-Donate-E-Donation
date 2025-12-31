from django.db import models
from django.contrib.auth.models import User

class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=20,null=True)
    def _str_(self):
        return self.user.username

class Recuiter(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    company=models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    def _str_(self):
        return self.user.username

class Job(models.Model):
    recuiter = models.ForeignKey(Recuiter,on_delete=models.CASCADE)
    start_date = models.CharField(max_length=40,null=True)
    end_date = models.CharField(max_length=40,null=True)
    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=20)
    image = models.FileField()
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def _str_(self):
        return self.title

class Applyjob(models.Model):
    fname = models.CharField(max_length=20,null=True)
    lname = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    experience = models.CharField(max_length=20,null=True)
    qualification = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    num = models.CharField(max_length=40,null=True)


