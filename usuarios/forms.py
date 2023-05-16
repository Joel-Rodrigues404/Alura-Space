""" Models para Criaçao de formularios """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django import forms

#Classes que definem modelos de formularios que herdam de forms.Form

class LoguinForms(forms.Form):
    """ Formulario de Login """

    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João Silva",
            }
        ),
    )
    senha = forms.CharField(
        label='senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha",
            }
        ),
    )

class CadastroForms(forms.Form):
    """ Formulario de Cadastro """

    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João Silva",
            }
        ),
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget = forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva@xpto"
            }
        ),
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha",
            }
        ),
    )
    senha_2 = forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha novamente",
            }
        ),
    )

    #Validaçoes dos Campos deve Começar com [clean_]
    def clean_nome_cadastro(self):
        #Pega o nome_cadastro
        nome = self.cleaned_data("nome_cadastro")
        #verifica se ele contem espaços entre os nomes se tiver retorna um erro
        if nome:
            nome = nome.strip()
            if " " in nome:
                #Erro
                raise forms.ValidationError("Espaços não são permitidos nesse campo!")
            else:
                #retorna o nome 
                return nome
    
    def clean_senha_2(self):
        #Pega os campos senha_1 senha_2
        senha_1 = self.cleaned_data("senha_1")
        senha_2 = self.cleaned_data("senha_2")
        #verifica se eles são diferentes se forem retorna um erro
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                #Erro
                raise forms.ValidationError("Senhas não são iguais!")
            else:
                 #retorna senha_2
                 return senha_2
