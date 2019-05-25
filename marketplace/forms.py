from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'email',
                'password1',
                'password2'
            ]
        labels = {
                'username': 'Nombre de Usuario',
                'first_name': 'Nombre',
                'email': 'Correo',

        }