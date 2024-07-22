from rest_framework import serializers

from Job_portal_app.models import Login, Add_job, Add_resume, Save_jobs, add_profile_photo, job_application \

class signup_serializer_user(serializers.ModelSerializer):

     class Meta:
         model = Login
         fields = ('username','password','is_Job_seeker','Name','email','phoneno','place')


class signup_serializer_employer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username','password','email','companyName','place', 'phoneno',)


class job_post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_job
        fields = ('job_title','companyName','place','description','Qualification','salary','id')


class Add_resume_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_resume
        fields = ('Resume',)

class save_job_serializer(serializers.ModelSerializer):
    class Meta:
        model = Save_jobs
        fields = ('jobs','user','id')

class profile_photo_serializer(serializers.ModelSerializer):
    class Meta:
        model = add_profile_photo
        fields = ('photo',)


class apply_jobs_serializer(serializers.ModelSerializer):
    class Meta:
        model =job_application
        fields = ('job_details','user','resume','experience','noOfYears','new_resume')
