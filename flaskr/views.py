from flaskr import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/products')
def products():
    return "products"

@app.route('/products/<products_id>')
def products_id():
    return "speciifc products"
