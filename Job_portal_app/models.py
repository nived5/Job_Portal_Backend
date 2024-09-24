from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Login(AbstractUser):
    is_Employer=models.BooleanField(default = False)
    is_Job_seeker = models.BooleanField(default=False)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    companyName = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=12)
    place = models.CharField(max_length=100)
    is_blocked = models.BooleanField(default=False)

class Add_job(models.Model):
    job_title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.TextField()
    Qualification = models.TextField()
    salary = models.IntegerField()

class Add_resume(models.Model):
    Resume = models.FileField(upload_to='document/')

class Save_jobs(models.Model):
    jobs = models.ForeignKey(Add_job,on_delete=models.CASCADE)
    user = models.ForeignKey(Login,on_delete=models.CASCADE)

class add_profile_photo(models.Model):
    photo = models.FileField(upload_to='document/')



class job_application2(models.Model):
    job_details = models.ForeignKey(Add_job,on_delete=models.CASCADE)
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    resume = models.ForeignKey(Add_resume,on_delete=models.CASCADE)
    experience = models.CharField(max_length=200)
    noofyears = models.CharField(max_length=20)
    new_resume = models.FileField(upload_to='document/')
    phoneno= models.CharField(max_length=12)
    user_details =models.CharField(max_length=255)



# class employer_applied_job_view(models.Model):
#     details = models.ForeignKey(job_application2,on_delete=models.CASCADE)
class add_qualification(models.Model):
    higher_secondary = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)


class employer_applied_job_view(models.Model):
    details = models.ForeignKey(job_application2,on_delete=models.CASCADE)

class companyDetails(models.Model):
    company_name = models.CharField(max_length=200)
    logo = models.TextField()
    company_details = models.CharField(max_length=255)











