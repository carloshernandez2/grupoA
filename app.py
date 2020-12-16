from flask import Flask,render_template,request,session
from formularios import RecordarContra,Index,RegistroProducto,ModificarProducto,RegistroEmpleado,ModificarEmpleado,ModificarCantidades
import os
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

app.secret_key = os.urandom(24)


lista_empleados = [{"cargo":"admin","nombre":"admin","correo":"admin@cafe.com","cedula": 7777,"id":1, "password":"1234"}, 
                    {"cargo":"empleado","nombre":"empleado1","correo":"empleado1@cafe.com","cedula": 1,"id":2,"password":"12345"},
                    {"cargo":"empleado","nombre":"empleado2","correo":"empleado2@cafe.com","cedula": 2,"id":3,"password":"123456"},
                    {"cargo":"empleado","nombre":"empleado3","correo":"empleado3@cafe.com","cedula": 3,"id":4,"password":"1234567"},
                    {"cargo":"empleado","nombre":"empleado4","correo":"empleado4@cafe.com","cedula": 4,"id":5,"password":"12345678"}]


lista_productos = [{"id":1,"nombre":"producto1","precio":100,"existencias":20},
                    {"id":2,"nombre":"producto2","precio":200,"existencias":40},
                    {"id":3,"nombre":"producto3","precio":300,"existencias":60},
                    {"id":4,"nombre":"producto4","precio":400,"existencias":80},
                    {"id":5,"nombre":"producto5","precio":500,"existencias":100}]





@app.route("/", methods=["POST","GET"])
def login():
    form = Index(request.form)
    return render_template("index.html",form=form)


@app.route("/recuperar_contra",methods=["POST","GET"])
def recuperar_contra():
    form = RecordarContra()
    return render_template("recordarContra.html",form = form)


@app.route("/inicio",methods=["POST","GET"])
def inicio():
    user = request.form['correo']
    password = request.form['clave']
    cargo = ''
    form = Index()
    for u in lista_empleados:
        if u["correo"] == user:
            if u['password'] == password:
                cargo = u["cargo"]
            else:
                return render_template("index.html", form = form, mensaje = "Contraseña no valida")
    if cargo == "admin":
        session['usuario'] = cargo
        return render_template("inicioAdministrador.html")
    elif cargo == "empleado":
        session['usuario'] = cargo
        return render_template("inicioEmpleado.html", productos = lista_productos)
    else:
        return render_template("index.html", form = form, mensaje = "Usuario no reconocido")


@app.route("/logout")
def logout():
    session.pop("usuario")
    form = Index()
    return render_template("index.html", form = form)

@app.route("/inicio/admin_autorizado", methods=["POST","GET"])
def inicio_admin():
    if "usuario" in session and session['usuario'] == "admin":
        return render_template("inicioAdministrador.html")
    else:
        return "Usuario no autorizado."

@app.route("/registrar_producto", methods=["POST","GET"])
def registrar_producto():
    if "usuario" in session and session['usuario'] == "admin":
        form = RegistroProducto()
        return render_template("registroProducto.html",form = form, productos = lista_productos)
    else:
        return "Usuario no autorizado."

@app.route("/producto_registrado", methods=["POST","GET"])
def producto_registrado():
    if "usuario" in session and session['usuario'] == "admin":
        return "<center>Producto Registrado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
    else:
        return "Usuario no autorizado."

@app.route("/modificar_producto", methods=["POST","GET"])
def modificar_producto():
    if "usuario" in session  and session['usuario'] == "admin":
        form = ModificarProducto()
        return render_template("modificarProducto.html",form = form)
    else:
        return "Usuario no validado"

@app.route("/producto_modificado", methods=["POST","GET"])
def producto_modificado():
    if "usuario" in session  and session['usuario'] == "admin":
        return "<center>Producto Modificado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
    else:
        return "Usuario no validado"

@app.route("/registrar_empleado", methods = ["POST","GET"])
def registrar_empleado():
    if "usuario" in session  and session['usuario'] == "admin":
        form = RegistroEmpleado()
        return render_template("registroEmpleado.html",form = form, empleados = lista_empleados)
    else:
        return "Usuario no validado"

@app.route("/empleado_registrado", methods=["POST","GET"])
def empleado_registrado():
    if "usuario" in session  and session['usuario'] == "admin":
        return "<center>Empleado Registrado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
    else:
        return "Usuario no validado"

@app.route("/modificar_empleado", methods=["POST","GET"])
def modificar_empleado():
    if "usuario" in session  and session['usuario'] == "admin":
        form = ModificarEmpleado()
        return render_template("modificarEmpleado.html",form = form)
    else:
        return "Usuario no validado"

@app.route("/empleado_modificado", methods=["POST","GET"])
def empleado_modificado():
    if "usuario" in session  and session['usuario'] == "admin":
        return "<center>Empleado Modificado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
    else:
        return "Usuario no validado"

@app.route("/inicio/empleado_autorizado", methods=["POST","GET"])
def inicio_empleado():
    if "usuario" in session and session['usuario'] == "empleado":
        return render_template("inicioEmpleado.html", productos = lista_productos)
    else:
        return "Usuario no validado"

@app.route("/modificar_cantidades",methods=["POST","GET"])
def modificar_cantidades():
    if "usuario" in session and session['usuario'] == "empleado":
        form = ModificarCantidades()
        return render_template("modificarCantidades.html", form = form)
    else:
        return "Usuario no validado"

@app.route("/cantidad_modificada", methods=["POST","GET"])
def cantidad_modificada():
    if "usuario" in session and session['usuario'] == "empleado":
        return "<center>Cantidad Modificada <br> <a href='/inicio/empleado_autorizado'>Volver</a></center>"
    else:
        return "Usuario no validado"


if __name__ == "__main__":
    app.run(debug=True)