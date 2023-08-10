from flaskr import app


@app.route('/')
def homepage():
    return "Home Page"

@app.route('/products')
def products():
    return "products"

@app.route('/products/<products_id>')
def products_id():
    return "speciifc product"
