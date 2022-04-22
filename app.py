from flask import Flask, render_template, abort, json
app = Flask(__name__)	

f = open('Libreria/books.json')

datos = json.load(f)

@app.route('/')
def inicio():
	return render_template("inicio.html",lista_libros=datos)

@app.route('/libro/<isbn>')
def libros(isbn):
    for libro in datos:
        if libro.get("isbn")==isbn:
            return render_template("libro.html",contenido=libro)
    abort(404)
app.run('0.0.0.0',5000,debug=True)