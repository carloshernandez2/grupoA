from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, IntegerField




class RecordarContra(FlaskForm):
    correo = EmailField("Usuario", validators=[DataRequired(message="Correo es requerido")])
    clave = PasswordField("Clave Master", validators=[DataRequired(message="Clave Master es requerida")])
    nueva = PasswordField("Clave nueva", validators=[DataRequired(message="Clave nueva es requerida")])
    submit = SubmitField("Submit")
class Index(FlaskForm):
    correo = StringField("Nombre de Usuario", validators=[DataRequired(message="Correo es requerido")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="Clave es requerida")])
    ingresar = SubmitField("Ingresar")
class RegistroProducto(FlaskForm):
    producto = StringField("Nombre del producto", validators=[DataRequired(message="Nombre es requerido")])
    cantidad = IntegerField("Cantidad base", validators=[DataRequired(message="Cantidad es requerida")])
    categoria = StringField("Categoria", validators=[DataRequired(message="Categoría es requerida")])
    precio = IntegerField("Precio", validators=[DataRequired(message="Precio es requerido")])
    arch = FileField("Archivo", validators=[DataRequired(message="Archivo es requerido")])
    registrar = SubmitField("Registrar")
class ModificarProducto(FlaskForm):
    producto = StringField("Nombre del producto", validators=[DataRequired(message="Nombre es requerido")])
    categoria = StringField("Categoria", validators=[DataRequired(message="Categoría es requerida")])
    precio = IntegerField("Precio", validators=[DataRequired(message="Precio es requerido")])
    actualizar = SubmitField("Actualizar")
    borrar = SubmitField("Borrar")
    eliminar = SubmitField("Eliminar")
class RegistroEmpleado(FlaskForm):
    nombre = StringField("Nombre del empleado", validators=[DataRequired(message="Nombre es requerido")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="Clave es requerida")])
    cedula = IntegerField("Cédula", validators=[DataRequired(message="Cédula es requerida")])
    correo = StringField("Correo", validators=[DataRequired(message="Correo es requerido")])
    registrar = SubmitField("Registrar")
class ModificarEmpleado(FlaskForm):
    nombre = StringField("Nombre del empleado", validators=[DataRequired(message="Nombre es requerido")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="Clave es requerida")])
    cedula = IntegerField("Cédula", validators=[DataRequired(message="Cédula es requerida")])
    correo = StringField("Correo", validators=[DataRequired(message="Correo es requerido")])
    actualizar = SubmitField("Actualizar")
    borrar = SubmitField("Borrar")
    eliminar = SubmitField("Eliminar")
class ModificarCantidades(FlaskForm):
    nombre = StringField("Nombre del producto", validators=[DataRequired(message="Nombre es requerido")])
    cantidad = IntegerField("Cantidad base", validators=[DataRequired(message="Cantidad es requerida")])
    actualizar = SubmitField("Actualizar")

