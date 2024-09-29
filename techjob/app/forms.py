from django import forms
from .models import Usuario, Freelancer, Empresa

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['usuario', 'tipo_usuario', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")

class FreelancerForms(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ['nome', 'cpf', 'email', 'github']

class EmpresaForms(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_empresa', 'cnpj', 'email']
