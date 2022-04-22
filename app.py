from flask import Flask, render_template, abort, json
app = Flask(__name__)	

f = open('Libreria/books.json')

datos = json.load(f)

app.run('0.0.0.0',5000,debug=True)