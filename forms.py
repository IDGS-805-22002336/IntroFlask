
from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
from wtforms import validators
from wtforms import EmailField


class UserForm(Form):
    matricula=IntegerField("matricula", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese el valor valido")
    ])
    nombre=StringField("nombre", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    apaterno=StringField("Apaterno", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    amaterno=StringField("Amaterno", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    correo = EmailField("correo", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Email(message="Ingrese un correo válido"),
    validators.Length(min=10, max=100, message="Longitud inválida")
    ])
