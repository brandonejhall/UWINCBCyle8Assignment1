from flaskr import app
from flask import render_template

lst_of_products = [
    ("../static/xbox.jpg", "xbox series s", "The Xbox Series S is a compact gaming console with powerful performance, supporting a wide range of games.",0,"$250"),
    ("../static/iphone11.jpg", "iphone 11", "The iPhone 11 features a dual-camera system, A13 Bionic chip, and a Liquid Retina display, offering a great smartphone experience.",1,"$350"),
    ("../static/beats.jpg", "beats headphones", "Beats headphones deliver high-quality audio and come in various styles, providing an immersive listening experience.",2,"$100"),
    ("../static/headphones.jpg", "boss headphones", "Boss headphones offer premium sound quality and comfortable design, making them an ideal choice for audio enthusiasts.",3,"$80"),
    ("../static/ashirt.jpg", "tshirt", "This comfortable t-shirt is made from soft cotton and comes in a variety of colors, perfect for casual everyday wear.",4,"$30"),
    ("../static/eldenring.jpg", "game code", "The game code grants access to a digital game or downloadable content, offering entertainment and fun for gamers.",5,"$60"),
]

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/products')
def products():
    return render_template("product.html",prod = lst_of_products)

@app.route('/product/<int:prod_id>')
def products_id(prod_id):
    return render_template("specificproduct.html",prod_id=prod_id,prod = lst_of_products)
