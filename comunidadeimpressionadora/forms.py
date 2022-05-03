from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='O campo nome de usuário é obrigatório')])
    email = StringField('E-mail', validators=[DataRequired(message='O campo de e-mail é obrigatório'), Email(message='Digite um endereço de e-mail válido')])
    senha = PasswordField('Senha', validators=[DataRequired(message='O campo senha é obrigatório'), Length(6, 20, message='Sua senha deve ter entre 6 e 20 caracteres')])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(message='O campo confirmação de senha é obrigatório'), EqualTo('senha', message='As senhas digitadas são diferentes')])
    botao_submit_criarconta = SubmitField('Criar conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Esse e-mail já está sendo usado')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(message='O campo de e-mail é obrigatório'), Email(message='Digite um endereço de e-mail válido')])
    senha = PasswordField('Senha', validators=[DataRequired(message='O campo senha é obrigatório'), Length(6, 20, message='Sua senha deve ter entre 6 e 20 caracteres')])
    lembrar_dados = BooleanField('Lembrar Login')
    botao_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='O campo nome de usuário é obrigatório')])
    email = StringField('E-mail', validators=[DataRequired(message='O campo de e-mail é obrigatório'), Email(message='Digite um endereço de e-mail válido')])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('Power BI Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Apresentações Impressionadoras')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Esse e-mail já está sendo usado por outro usuário.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(message='O campo título do post é obrigatório'), Length(2, 140, message='O título deve ter entre 2 e 140 caracteres')])
    corpo = TextAreaField('Escreva seu Post aqui', validators=[DataRequired(message='Você deve escrever algo no seu Post')])
    botao_submit = SubmitField('Enviar Post')