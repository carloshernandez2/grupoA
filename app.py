from flask import Flask,render_template,request,session, jsonify
from formularios import RecordarContra,Index,RegistroProducto,ModificarProducto,RegistroEmpleado,ModificarEmpleado,ModificarCantidades
import os
from flask_session import Session
import sqlite3
from werkzeug.utils import secure_filename
import logging
import db
from markupsafe import escape
import hashlib

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

FOLDER_IMAGENES = "static/imagenes/"
EXT_VALIDAS = ["png", "jpg"]

app.secret_key = os.urandom(24)


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
    user = escape(request.form['correo'])
    pas = escape(request.form['clave'])
    h = hashlib.sha256(pas.encode())
    password = h.hexdigest()
    cargo = ''
    form = Index()
    with sqlite3.connect("cafeteria1.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select correo,clave,cargo from usuarios")
            row = cur.fetchall()

    #for u in lista_empleados:
    for u in row:
        if u["correo"] == user:
            if u['clave'] == password:
                cargo = u["cargo"]
            else:
                return render_template("index.html", form = form, mensaje = "Contraseña no valida")
    if cargo == "admin":
        session.pop("cargo",None)
        session["cargo"] = cargo
        return render_template("inicioAdministrador.html")
    elif cargo == "empleado":
        session.pop("cargo",None)
        session["cargo"] = cargo
        with sqlite3.connect("cafeteria1.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select id_producto, nombre, cantidad, categoria, precio from productos")
            productos = cur.fetchall()   
        return render_template("inicioEmpleado.html", productos = productos)
    else:
        return render_template("index.html", form = form, mensaje = "Usuario no reconocido")


@app.route("/logout")
def logout():
    session.pop("cargo",None)
    form = Index()
    return render_template("index.html", form = form)

@app.route("/escribir", methods=["POST","GET"])
def escribir():
    nombre = escape(request.form["username"])
    con = db.get_db()
    cur = con.cursor()
    cur.execute("SELECT filename FROM productos WHERE nombre = ?;",[nombre])
    diccionario = {"filename":"Archivo no encontrado"}
    a = cur.fetchone()
    b = jsonify(a)
    if b:
        db.close_db(con)
        return b
    else:
        db.close_db(con)
        return diccionario

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
        with sqlite3.connect("cafeteria1.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select id_producto, nombre, cantidad, categoria, precio, filename from productos")
            row = cur.fetchall()   
            return render_template("registroProducto.html",form = form, productos = row)
    else:
        return "Usuario no autorizado."

@app.route("/producto_registrado", methods=["POST","GET"])
def producto_registrado():
    if "usuario" in session and session['usuario'] == "admin":
        nombre = escape(request.form["producto"])
        cantidad = escape(request.form["cantidad"])
        categoria = escape(request.form["categoria"])
        precio = escape(request.form["precio"])
        arch = request.files["arch"]
    # mi imagen.jpg => ['mi imagen','jpg']
        ext = arch.filename.rsplit(".", 1)[1]
        if ext in EXT_VALIDAS:
                ruta = FOLDER_IMAGENES + secure_filename(arch.filename)
                arch.save(ruta)
                filename = arch.filename
        #try:
                with sqlite3.connect("cafeteria1.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO productos (nombre,cantidad,categoria,precio,filename) VALUES (?,?,?,?,?);", 
                    [nombre,cantidad,categoria,precio,filename])
                    con.commit()
                    return "<center> Guardado con éxito <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
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
        # Aqui para UPDATE
        form = ModificarProducto()
        nombre = escape(form.producto.data)
        categoria = escape(form.categoria.data)
        precio = escape(form.precio.data)
        with sqlite3.connect("cafeteria1.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE productos SET  categoria = ?, precio = ? WHERE nombre = ?", [
                    categoria, precio, nombre  ])
            con.commit()
            return "<center>Producto Modificado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
    else:
        return "Usuario no validado"


#esta lo va a mostrar en la tabla
@app.route("/registrar_empleado", methods = ["POST","GET"])
def registrar_empleado():
    if "usuario" in session  and session['usuario'] == "admin":
        form = RegistroEmpleado()
        with sqlite3.connect("cafeteria1.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select id_usuario, nombre, cedula,correo from usuarios")
            row = cur.fetchall()
        return render_template("registroEmpleado.html",form = form, empleados = row)
    else:
        return "Usuario no validado"

# lo va a meter a la base de datos
@app.route("/empleado_registrado", methods=["POST","GET"])
def empleado_registrado():
    if "usuario" in session  and session['usuario'] == "admin":
        form = RegistroEmpleado()
        nombre = escape(form.nombre.data)
        cla = escape(form.clave.data)
        h = hashlib.sha256(cla.encode())
        clave = h.hexdigest()
        cedula = escape(form.cedula.data) 
        correo = escape(form.correo.data)
        cargo = 'empleado'
        with sqlite3.connect("cafeteria1.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO usuarios (nombre,clave,cedula,correo,cargo) VALUES (?,?,?,?,?);",  
            [nombre,clave,cedula,correo,cargo])
            con.commit()
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
        #UPDATE
        form = ModificarEmpleado()
        nombre = escape(form.nombre.data)
        cla = escape(form.clave.data)
        h = hashlib.sha256(cla.encode())
        clave = h.hexdigest()
        cedula = escape(form.cedula.data)
        correo = escape(form.correo.data)
        cargo = 'empleado'
        with sqlite3.connect("cafeteria1.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE usuarios SET cedula = ?, correo = ?, cargo = ?, clave = ? WHERE nombre = ?",
            [cedula, correo, cargo, clave, nombre ])
            con.commit()
            return "<center>Empleado Modificado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>" 
    else:
        return "Usuario no validado"

@app.route("/inicio/empleado_autorizado", methods=["POST","GET"])
def inicio_empleado():
    if "usuario" in session and session['usuario'] == "empleado":
        with sqlite3.connect("cafeteria1.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select id_producto, nombre, cantidad, categoria, precio from productos")
            productos = cur.fetchall()   
            return render_template("inicioEmpleado.html", productos = productos)
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
        # update solo con cantidades
        form = ModificarCantidades()
        nombre = escape(form.nombre.data)
        cantidad = escape(form.cantidad.data)
        with sqlite3.connect("cafeteria1.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE productos SET cantidad = ? WHERE nombre = ?",
            [cantidad, nombre ])
            con.commit()
            return "<center>Cantidad Modificada <br> <a href='/inicio/empleado_autorizado'>Volver</a></center>"
    else:
        return "Usuario no validado"

# ruta para borrar producto 
@app.route("/eliminar_producto/<nombre>", methods =["POST","GET"])
def eliminar_producto(nombre):
    if "usuario" in session  and session['usuario'] == "admin":
        with sqlite3.connect("cafeteria1.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM productos WHERE nombre = ?",[nombre])
            con.commit()
            return "<center>Producto Eliminado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>"
    else:
        return "Usuario no validado"

# ruta para borrar empleado
@app.route("/eliminar_empleado/<nombre>", methods =["POST","GET"])
def eliminar_empleado(nombre):
    if "usuario" in session  and session['usuario'] == "admin":
        with sqlite3.connect("cafeteria1.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM usuarios WHERE nombre = ?",[nombre])
            con.commit()
            return "<center>Usuario Eliminado <br> <a href='/inicio/admin_autorizado'>Volver</a></center>"
    else:
        return "Usuario no validado"

if __name__ == "__main__":
    app.run(debug=True)