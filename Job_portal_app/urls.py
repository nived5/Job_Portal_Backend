from django.urls import path, include
from rest_framework import routers

from Job_portal_app import views
from Job_portal_app.views import delete_job_post

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
    path('user_apply_for_jobs',views.user_apply_for_jobs.as_view()),
    path('applied_jobs_view',views.applied_jobs_view.as_view()),
    # path('AppliedJobsView',views.AppliedJobsView.as_view()),
    # path('employer_jobs_view',views.employer_jobs_view.as_view())
    path('AddQualification',views.AddQualification.as_view()),
    # path('AppliedJobsView',views.AppliedJobsView.as_view()),
    path('jobseeker_view_jobs/<int:id>/',views.jobseeker_view_jobs.as_view()),
    path('CompanyDetails',views.CompanyDetails.as_view()),
    path('CountView',views.CountView.as_view()),
    path('UsersCountView',views.UsersCountView.as_view()),
    path('TotalNoofJobPost',views.TotalNoofJobPost.as_view()),
    path('ManagerCountView',views.ManagerCountView.as_view()),
    path('ManagerView',views.ManagerView.as_view()),
    # path('AppliedJobAdminView',views.AppliedJobAdminView.as_view())

    path('JobSeekerList',views.JobSeekerList.as_view()),
    path('AppliedJobsAdminView',views.AppliedJobsAdminView.as_view()),
    path('JobPostListAdminView',views.JobPostListAdminView.as_view()),
    path('delete_job_post/<int:id>/',delete_job_post,name= 'delete_job_post'),
    path('BlockUserView/<int:id>/',views.BlockUserView.as_view()),
    # path('managerID',views.managerID.as_view())
    path('BlockedUserLogin/<int:id>/',views.BlockedUserLogin.as_view())

]