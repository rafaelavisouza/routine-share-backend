from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class RegisterForm(forms.ModelForm):
    # Eu criei esses dois campos de senha no form (o User não tem password1/password2)
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput)

    # Campos extras do Profile
    phone = forms.CharField(label="Telefone", required=False)
    address = forms.CharField(label="Endereço", required=False)

    # Foto do usuário (arquivo do computador)
    photo = forms.ImageField(label="Foto", required=False)

    class Meta:
        model = User
        fields = ["first_name", "email", "username"]

    def clean(self):
        # Aqui eu valido se as duas senhas são iguais
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "As senhas não conferem.")
        return cleaned

    def save(self, commit=True):
        # Aqui eu crio o usuário e salvo senha criptografada
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

            # Aqui eu preencho os dados do perfil
            profile = user.profile
            profile.phone = self.cleaned_data.get("phone", "")
            profile.address = self.cleaned_data.get("address", "")

            # Se a pessoa escolheu uma foto, eu salvo também
            photo = self.cleaned_data.get("photo")
            if photo:
                profile.photo = photo

            profile.save()

        return user


class LoginForm(AuthenticationForm):
    # Eu uso o form pronto do Django pra autenticação
    # Dá pra customizar labels/placeholders no template
    pass