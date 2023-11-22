from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    The index file url
    """
    return (render_template('index.html'))

@app.route('/product', strict_slashes=False)
def product():
    """
    The function to the product page
    """
    return (render_template('product.html'))

@app.route('/contacts', strict_slashes=False)
def contact():
    """
    The route to the contacts page
    """
    return (render_template('contact.html'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=888, debug=True)
