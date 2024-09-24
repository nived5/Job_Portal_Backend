from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, request, generics, viewsets, permissions
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from Job_portal_app.forms import Userregister, EmployerRegistration
from Job_portal_app.models import Add_job, Add_resume, add_profile_photo, Save_jobs, job_application2, \
    add_qualification, employer_applied_job_view, companyDetails, Login

from Job_portal_app.serializers import signup_serializer_user, signup_serializer_employer, job_post_serializer, \
    Add_resume_serializer, save_job_serializer, profile_photo_serializer, apply_jobs_serializer, \
    addQualificationSerializer, employerJobViewSerializer, companyDetailsSerializer, appliedJobsSerilazer


# Create your views here.

# class UserRegistration(APIView):
#     def post(self,request):
#             serializer = signup_serializer_user(data = request.data)
#             if serializer.is_valid():
#                 serializer.validated_data['is_Job_seeker'] =True
#                 serializer.save()
#                 return Response(serializer.data,status = status.HTTP_201_CREATED)
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
#
# class Employer_Registration(APIView):
#     def post(self,request):
#             serializer = signup_serializer_employer(data = request.data)
#             if serializer.is_valid():
#                 serializer.validated_data['is_Employer'] =True
#                 serializer.save()
#                 return Response(serializer.data,status = status.HTTP_201_CREATED)
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

# class Login(APIView):
#     def post(self,request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username,password=password)
#         print(user)
#         if user is not None:
#             if user.is_Employer:
#                 user_type = 'Employer'
#             elif user.is_jobseeker:
#                 user_type= 'Job seeker'
#             else:
#                 user_type = 'Unknown'
#             return Response({'message':'user logged in successfully as {Emloyer}'},status=status.HTTP_200_OK)
#         else:
#             return Response({'message':'Ivalid username or password'},status=status.HTTP_401_UNAUTHORIZED)




# from django.contrib.auth import authenticate
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class User_Login(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         print(username)
#         password = request.data.get('password')
#         print(password)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             if user.is_Employer:
#                 user_type = 'Employer'
#             elif user.is_Job_seeker:
#                 user_type = 'Job Seeker'
#             else:
#                 user_type = 'Unknown'  # If neither employer nor job seeker, you might want to handle this case
#             return Response({'message': f'User logged in successfully as {'Employer'}','user': {'id': user.id, 'username': user.username}}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def user_registration(request):
    result_data=None
    if request.method=='POST':
        form=Userregister(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.is_active=True
            form.is_Job_seeker=True
            form.save()
            result_data=True
    try:
        if result_data:
            data={'result':True}
        else:
            print(list(form.errors))
            error_data=form.errors
            error_dict={}
            for i in list(form.errors):
                error_dict[i]=error_data[i][0]
                data={
                    'result':False,
                    'errors':error_dict
                }
    except:
        data={
            'result':False
        }
    return JsonResponse(data,safe=False)

@csrf_exempt
def Employer_registration(request):
    result_data=None
    if request.method=='POST':
        form=EmployerRegistration(request.POST)

        if form.is_valid():
            form=form.save(commit=False)
            form.is_active=True
            form.is_Employer=True
            form.save()
            result_data=True
    try:
        if result_data:
            data={'result':True}
        else:
            print(list(form.errors))
            error_data=form.errors
            error_dict={}
            for i in list(form.errors):
                error_dict[i]=error_data[i][0]
                data={
                    'result':False,
                    'errors':error_dict
                }
    except:
        data={
            'result':False
        }
    return JsonResponse(data,safe=False)

@csrf_exempt
def UserLogin( request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password1')
    print(password)
    user = authenticate(request, username=username,password=password)
    print(user)
    if user is not None:
        if user.is_blocked:
            return Response({"message:User is blocked"},status=status.HTTP_403_FORBIDDEN)
        login(request, user)
        if user.is_Employer:
            user_type = 'Employer'
        elif user.is_Job_seeker:
            user_type = 'Job seeker'
        elif user.is_blocked:
            user_type = 'blocked user'
        else:
            user_type = 'admin'
        data = {
            'status': True,
            'result': {
                'id': user.id,
                'name': user.Name,
                'username':user.username,
                'phoneno':user.phoneno,
                'type': user_type
            }
        }
    else:
        data = {
            'status': False,
            'result': 'Invalid username or password'
        }
    return JsonResponse(data, safe=False)




    #New functions
# class BaseRegistrationView(APIView):
#         serializer_class =None
#         user_type_field = None
#
#         def post(self,request):
#             serializer = self.serializer_class(data=request.data)
#             if serializer.is_valid():
#                 serializer.validated_data[self.user_type_field]=True
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class UserRegistration2(BaseRegistrationView):
#     serializer_class = signup_serializer_user
#     user_type_field = 'is_Job_seeker'
#
#
# class EmployerRegistration(BaseRegistrationView):
#     serializer_class = signup_serializer_employer
#     user_type_field = 'is_Employer'
#
#
# class LoginView(APIView):
#     def post(self, request):
#         print("hhhikkkkkkkkkkkkk")
#         username = request.data.get('username')
#         print(username)
#         password = request.data.get('password')
#         print(password)
#
#         user = authenticate(request,username=username, password=password)
#         print(username)
#         print(user)
#         if user is not None:
#             print(user)
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class job_post_add(generics.ListCreateAPIView):
    queryset = Add_job.objects.all()
    serializer_class = job_post_serializer


class PostDetailed_view(APIView):
    def get(self,request,id):
        post = get_object_or_404(Add_job,id=id)
        serializer = job_post_serializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)

# class post_detailed_view(viewsets.ModelViewSet,id):
#     queryset = Add_job.objects.all(id=id)
#     serializer_class = job_post_serializer


class Add_jobseeker_resume(generics.ListCreateAPIView):
    queryset = Add_resume.objects.all()
    serializer_class = Add_resume_serializer


class jobseeker_saved_jobs(APIView):
    def post(self,request):
        serializer = save_job_serializer(data=request.data)
        request.POST.get("jobs")
        print(serializer)
        if serializer.is_valid():
            # print("hello")
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class saved_jobs_view(generics.ListCreateAPIView):
    queryset = Save_jobs.objects.all()
    print(queryset)
    serializer_class = save_job_serializer
class profile_photo_add(generics.ListCreateAPIView):
    queryset = add_profile_photo.objects.all()
    serializer_class = profile_photo_serializer

class user_apply_for_jobs(APIView):
    def post(self,request):
        serializer = apply_jobs_serializer(data= request.data)
        print(request.POST.get('new_resume'))
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class applied_jobs_view(generics.ListCreateAPIView):
    # print(request.user)
    queryset = job_application2.objects.all()
    serializer_class = apply_jobs_serializer


# class AppliedJobsView(generics.ListCreateAPIView):
#     serializer_class = apply_jobs_serializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return job_application2.objects.filter(user=self.request.user)


# class employer_jobs_view(generics.ListCreateAPIView):
#     queryset = employer_applied_job_view.objects.all()
#     serializer_class = jobs_view_serializer

class AddQualification(generics.ListCreateAPIView):
    queryset = add_qualification.objects.all()
    print(queryset)
    serializer_class = addQualificationSerializer


# class AppliedJobsView(generics.ListAPIView):
#     serializer_class = employerJobViewSerializer
#     def get_queryset(self):
#         return employer_applied_job_view.objects.filter(details = self.request.user)

class jobseeker_view_jobs(APIView):
    def get(self,request,id):
        print(id)
        data = job_application2.objects.filter(job_details = id)
        for i in data:
            print(i.user.phoneno)

        serializer = apply_jobs_serializer(data,many=True)
        print(serializer)
        return Response(serializer.data)

class CompanyDetails(generics.ListCreateAPIView):
    queryset = companyDetails.objects.all()
    serializer_class = companyDetailsSerializer



class CountView(APIView):
    def get(self,request):
        count = job_application2.objects.count()
        return Response({"count":count})


class UsersCountView(APIView):
    def get(self,request):
        count1 = Login.objects.count()
        return Response({"count1":count1})

class TotalNoofJobPost(APIView):
    def get(self,request):
        postCount = Add_job.objects.count()
        return Response({"postCount":postCount})


# class MangerCountView(APIView):
#     def get(self,request):
#         managerCount = Login.objects.filter(is_manager=True).count()
#         return Response({"managerCount":managerCount})

class ManagerCountView(APIView):



    def get(self, request):

        manager_count = Login.objects.filter(is_Employer=True).count()
        return Response({"manager_count": manager_count})
class ManagerView(APIView):
    def get(self,request):
        print(id)
        data = Login.objects.filter(is_Employer = True)
        print(data)

        serializer = signup_serializer_employer(data,many=True)
        print(serializer)
        return Response(serializer.data)

class JobSeekerList(APIView):
    def get(self,request):
        data = Login.objects.filter(is_Job_seeker = True)
        serializer = signup_serializer_user(data,many=True)
        return Response(serializer.data)

class appliedJobAdminView(APIView):
    def get(self,request):
        print(id)
        data = job_application2.objects.all()

        serializer = job_post_serializer(data,many=True)
        print(serializer)
        return Response(serializer.data)
# class AppliedJobAdminView(APIView):
#     """
#     API view to retrieve job applications filtered by job title.
#     """
#
#     def get(self, request):
#         job_title = job_application2.job_details.query_params.get('job_title')  # Assuming job_title is passed as a query parameter
#         print(job_title)
#         if not job_title:
#             return Response({"error": "job_title parameter is required"}, status=400)
#
#         applications = job_application2.objects.filter(
#             job_details__job_title=job_title)  # Assuming job_details is a ForeignKey
#         serializer = job_post_serializer(applications, many=True)
#
#         return Response(serializer.data)

class AppliedJobsAdminView(generics.ListCreateAPIView):
    queryset = job_application2.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return apply_jobs_serializer
        return appliedJobsSerilazer

class JobPostListAdminView(APIView):
    def get(self,request):
        data = Add_job.objects.all()
        serializer = job_post_serializer(data,many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_job_post(request,id):
    try:
        jobPost = Add_job.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    jobPost.delete()
    return  Response(status = status.HTTP_204_NO_CONTENT)


class BlockUserView(APIView):
    def patch(self, request, id):
        print(f"received ID:{id}")
        user = get_object_or_404(Login, id=id)
        print(user)

        # Toggle the block status
        user.is_blocked = not user.is_blocked
        user.save()

        status_message = "blocked" if user.is_blocked else "unblocked"
        return Response({"message": f"User {status_message} successfully"}, status=status.HTTP_200_OK)



# class BlockedUserLogin(APIView):
#     def get(self,request):
#         user = Login.objects.filter(is_blocked =True)
#         if user.is_blocked:
#             return Response("user is blocked")


# class BlockedUserLogin(APIView):
#     def get(self, request,id):
#         # user = request.user
#         user = get_object_or_404(Login, id=id)
#         if user.is_blocked:
#             return Response({"message": "User is blocked"}, status=status.HTTP_403_FORBIDDEN)
#         else:
#             return Response({"message": "User is not blocked"}, status=status.HTTP_200_OK)



# class BlockedUserLogin(APIView):
#     def get(self,request):
#         user = Login.objects.filter(is_blocked = True)
#         serializer = signup_serializer_user(user,many=True)
#         if user.is_blocked:
#             return Response({"message": "User is blocked"}, status=status.HTTP_403_FORBIDDEN)
#         else:
#             return Response({"message": "User is not blocked"}, status=status.HTTP_200_OK)
#         return Response(serializer.data)
class BlockedUserLogin(APIView):
    def get(self, request, id):

        user = get_object_or_404(Login, id=id)
        if user.is_blocked:
            return Response({"message": "User is blocked"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"message": "User is not blocked"}, status=status.HTTP_200_OK)