from django.urls import path, include
from rest_framework import routers

from Job_portal_app import views



urlpatterns = [

    path('user_registration',views.user_registration,name='user_registration'),
    path('UserLogin',views.UserLogin,name='UserLogin'),
    path('Employer_registration',views.Employer_registration,name='Employer_registration'),
    path('job_post_add',views.job_post_add.as_view()),
    # path('post_detailed_view/<int:id>/',views.post_detailed_view.as_view()),
    path('PostDetailed_view/<int:id>/',views.PostDetailed_view.as_view()),
    path('Add_jobseeker_resume',views.Add_jobseeker_resume.as_view()),
    path('jobseeker_saved_jobs',views.jobseeker_saved_jobs.as_view()),
    path('profile_photo_add',views.profile_photo_add.as_view(),),
    path('saved_jobs_view',views.saved_jobs_view.as_view()),
    path('user_apply_for_jobs',views.user_apply_for_jobs.as_view())
]