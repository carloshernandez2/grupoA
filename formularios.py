from wtforms import Form,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, IntegerField




class RecordarContra(Form):
    correo = EmailField("Usuario", validators=[DataRequired(message="Correo es requerido")])
    clave = PasswordField("Clave Master", validators=[DataRequired(message="Clave Master es requerida")])
    nueva = PasswordField("Clave nueva", validators=[DataRequired(message="Clave nueva es requerida")])
    submit = SubmitField("Submit")
class Index(Form):
    correo = StringField("Nombre de Usuario", validators=[DataRequired(message="Correo es requerido")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="Clave es requerida")])
    ingresar = SubmitField("Ingresar")
class RegistroProducto(Form):
    producto = StringField("Nombre del producto", validators=[DataRequired(message="Nombre es requerido")])
    cantidad = IntegerField("Cantidad base", validators=[DataRequired(message="Cantidad es requerida")])
    categoria = StringField("Categoria", validators=[DataRequired(message="Categoría es requerida")])
    precio = IntegerField("Precio", validators=[DataRequired(message="Precio es requerido")])
    registrar = SubmitField("Registrar")
class ModificarProducto(Form):
    producto = StringField("Nombre del producto", validators=[DataRequired(message="Nombre es requerido")])
    categoria = StringField("Categoria", validators=[DataRequired(message="Categoría es requerida")])
    precio = IntegerField("Precio", validators=[DataRequired(message="Precio es requerido")])
    actualizar = SubmitField("Actualizar")
    borrar = SubmitField("Borrar")
class RegistroEmpleado(Form):
    nombre = StringField("Nombre del empleado", validators=[DataRequired(message="Nombre es requerido")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="Clave es requerida")])
    cedula = IntegerField("Cédula", validators=[DataRequired(message="Cédula es requerida")])
    correo = StringField("Correo", validators=[DataRequired(message="Correo es requerido")])
    registrar = SubmitField("Registrar")
class ModificarEmpleado(Form):
    nombre = StringField("Nombre del empleado", validators=[DataRequired(message="Nombre es requerido")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="Clave es requerida")])
    cedula = IntegerField("Cédula", validators=[DataRequired(message="Cédula es requerida")])
    correo = StringField("Correo", validators=[DataRequired(message="Correo es requerido")])
    actualizar = SubmitField("Actualizar")
    borrar = SubmitField("Borrar")
class ModificarCantidades(Form):
    nombre = StringField("Nombre del producto", validators=[DataRequired(message="Nombre es requerido")])
    cantidad = IntegerField("Cantidad base", validators=[DataRequired(message="Cantidad es requerida")])
    actualizar = SubmitField("Actualizar")
