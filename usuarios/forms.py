from django.forms import ModelForm, PasswordInput, CharField
from .models import Usuario


class UsuarioForm(ModelForm):
    password = CharField(widget=PasswordInput(
        attrs={'placeholder':'Escribe contraseña','class':'form-control'}), 
        label="Contraseña"
    )
    password_re = CharField(widget=PasswordInput(
        attrs={'placeholder':'Repite contraseña','class':'form-control'}), 
        label="Repita contraseña"
    )
    
    class Meta:
        model = Usuario
        fields = ('first_name','last_name','email','username','password','password_re')