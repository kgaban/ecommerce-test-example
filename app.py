from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Product 1', 'price': 100},
    {'id': 2, 'name': 'Product 2', 'price': 150},
    {'id': 3, 'name': 'Product 3', 'price': 200},
]

cart_items = []


@app.route('/')
def index():
    return render_template('index.html', products=products)


@app.route('/cart')
def cart():
    return render_template('cart.html', cart_items=cart_items)


@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart_items.append(product)
    return redirect(url_for('cart'))


@app.route('/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    global cart_items
    cart_items = [item for item in cart_items if item['id'] != product_id]
    return redirect(url_for('cart'))


if __name__ == '__main__':
    app.run(debug=True)
