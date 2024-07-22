from django.contrib.auth.forms import UserCreationForm

from Job_portal_app.models import Login


class Userregister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Login
        fields = ('username','password1','password2','Name','email','place','phoneno')

class EmployerRegistration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Login

        fields = ('username', 'password1', 'password2','email','companyName','place', 'phoneno')

