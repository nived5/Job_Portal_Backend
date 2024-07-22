from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, request, generics, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from Job_portal_app.forms import Userregister, EmployerRegistration
from Job_portal_app.models import Add_job, Add_resume, add_profile_photo, Save_jobs
from Job_portal_app.serializers import signup_serializer_user, signup_serializer_employer, job_post_serializer, \
    Add_resume_serializer, save_job_serializer, profile_photo_serializer, apply_jobs_serializer \
 \
 \
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
        login(request, user)
        if user.is_Employer:
            user_type = 'Employer'
        elif user.is_Job_seeker:
            user_type = 'Job seeker'
        else:
            user_type = 'unknown'
        data = {
            'status': True,
            'result': {
                'id': user.id,
                'name': user.Name,
                'username':user.username,
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
            print("hello")
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class saved_jobs_view(generics.ListCreateAPIView):
    queryset = Save_jobs.objects.all()
    serializer_class = save_job_serializer
class profile_photo_add(generics.ListCreateAPIView):
    queryset = add_profile_photo.objects.all()
    serializer_class = profile_photo_serializer

class user_apply_for_jobs(APIView):
    def post(self,request):
        serializer = apply_jobs_serializer(data= request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
