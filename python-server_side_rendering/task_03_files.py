from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Page à propos
@app.route('/about')
def about():
    return render_template('about.html')

# Page contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Affiche les items depuis items.json
@app.route('/items')
def items():
    with open('items.json') as f:
        items = json.load(f)
    return render_template('items.html', items=items.get("items"))

# Affiche les produits depuis JSON ou CSV
@app.route('/products')
def products():
    error = 0
    source = request.args.get('source')  # "json" ou "csv"
    id = request.args.get('id')          # id du produits

    # Vérifie si source est valide
    if source != "json" and source != "csv":
        value = "Wrong source"
        error = 1
    else:
        # Lit les données selon la source
        if source == "json":
            value = read_json()
        else:
            value = read_csv()

        # Si un id est donné, cherche le produit
        if id:
            success = 0
            for element in value:
                if id == str(element['id']):
                    success = 1
                    value = [element]  # Affiche uniquement ce produit
            if success == 0:
                value = "Product not found"
                error = 1

    return render_template('product_display.html', value=value, error=error)

# Lit les données depuis products.csv
def read_csv():
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = list(reader)
        print(result)  # Affiche les données dans la console (pour debug)
    return result

# Lit les données depuis products.json
def read_json():
    with open('products.json') as f:
        value = json.load(f)
    return value

# Lance l'app Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
