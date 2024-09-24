from rest_framework import serializers

from Job_portal_app.models import Login, Add_job, Add_resume, Save_jobs, add_profile_photo, job_application2, \
    add_qualification, employer_applied_job_view, companyDetails


class signup_serializer_user(serializers.ModelSerializer):

     class Meta:
         model = Login
         fields = ('username','password','is_Job_seeker','Name','email','phoneno','place','id')


class signup_serializer_employer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username','password','email','companyName','place', 'phoneno','id')


class job_post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_job
        fields = ('job_title','companyName','place','description','Qualification','salary','id')


class Add_resume_serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_resume
        fields = ('Resume','id')

class save_job_serializer(serializers.ModelSerializer):
    class Meta:
        model = Save_jobs
        fields = ('jobs','user','id')

class profile_photo_serializer(serializers.ModelSerializer):
    class Meta:
        model = add_profile_photo
        fields = ('photo',)


class apply_jobs_serializer(serializers.ModelSerializer):
    # job_details = job_post_serializer()
    # user = signup_serializer_user()
    class Meta:
        model =job_application2
        fields = ('job_details','user','resume','experience','noofyears','new_resume','phoneno')

class appliedJobsSerilazer(serializers.ModelSerializer):
    job_details = serializers.PrimaryKeyRelatedField(queryset=Add_job.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all())
    class Meta:
        model = job_application2
        fields = ('job_details', 'user', 'resume', 'experience', 'noofyears', 'new_resume', 'phoneno')


# class jobs_view_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = employer_applied_job_view
#         fields = ('details',)

class addQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = add_qualification
        fields = ('higher_secondary','degree','skills')



class employerJobViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = employer_applied_job_view
        fields = ('details',)


class companyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyDetails
        fields = ('company_name','logo','company_details')



