
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    nombre = None
    total_sin_descuento = None
    descuento_monto = None
    total_con_descuento = None
    descuento_porcentaje = None

    if request.method == 'POST':

        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        total_sin_descuento = cantidad * 9000

        if 18 <= edad <= 30:
            descuento_porcentaje = 15

        elif edad > 30:
            descuento_porcentaje = 25

        else:
            descuento_porcentaje = 0

        descuento_monto = total_sin_descuento * (descuento_porcentaje / 100)

        total_con_descuento = total_sin_descuento - descuento_monto

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        descuento_monto=descuento_monto,
        total_con_descuento=total_con_descuento,
        descuento_porcentaje=descuento_porcentaje
    )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    mensaje = None

    if request.method == 'POST':

        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido Administrador juan"

        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido Usuario pepe"

        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

@app.route('/repositorio')
def repositorio():
    return render_template('repositorio.html')


if __name__ == '__main__':
    app.run(debug=True)
()
