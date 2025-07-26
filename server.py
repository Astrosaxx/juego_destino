from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "clave_secreta"  # Necesaria para usar sesiones

# Ruta principal con el formulario
@app.route("/")
def index():
    return render_template("index.html")

# Ruta POST que recibe los datos del formulario
@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    gusto = request.form.get("gusto")

    session["nombre"] = nombre
    session["edad"] = edad
    session["gusto"] = gusto

    return redirect("/futuro")

# Ruta para mostrar la predicción del destino
@app.route("/futuro")
def futuro():
    mensajes_buenos = [
        "¡Vas a tener un futuro brillante!",
        "¡Encontrarás el éxito en lo que amas!",
        "¡El amor tocará tu puerta pronto!"
    ]
    mensajes_malos = [
        "Hoy no es tu día, pero mañana puede serlo.",
        "Prepárate, vienen cambios difíciles.",
        "Tendrás que tomar decisiones importantes pronto."
    ]

    prediccion = random.choice(mensajes_buenos + mensajes_malos)

    return render_template("futuro.html", 
                           nombre=session.get("nombre"),
                           edad=session.get("edad"),
                           gusto=session.get("gusto"),
                           prediccion=prediccion)

if __name__ == "__main__":
    app.run(debug=True)
