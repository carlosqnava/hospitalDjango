from django.forms import ModelForm, PasswordInput, CharField, TextInput
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

        widgets = {
                'first_name':TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nombre...'}),
                'email':TextInput(attrs={'class':'form-control','placeholder':'Escribe tu e-mail...'}),
                'last_name':TextInput(attrs={'class':'form-control','placeholder':'Escribe tus apellidos'}),
                'username':TextInput(attrs={'class':'form-control','placeholder':'Esscribe tu nombre de usuario'}),
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        
        return user