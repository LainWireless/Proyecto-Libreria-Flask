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
    
@app.route('/categoria/<tipo>')
def categoria(tipo):
    listacategorias=[]
    for cate in datos:
        for lista in cate.get("categories"):
            if lista==tipo:
                listacategorias.append(cate)
    return render_template("categoria.html",categoria=tipo,lista_categorias=listacategorias,lista_libros=datos)

app.run('0.0.0.0',5000,debug=True)