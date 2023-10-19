from multiprocessing import AuthenticationError,UserCreationForm

from james.bond.models import CustomUser


class CustomAuthenticationForm(AuthenticationError):
    class Meta:
        model=CustomUser
        fields=('username','password')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('email','first_name','last_name','password1','password2')