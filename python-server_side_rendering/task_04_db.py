from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Sources acceptées : json, csv, sql
source_author = ["json", "csv", "sql"]

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

# Affiche les produits depuis json, csv ou sql
@app.route('/products')
def products():
    error = 0
    source = request.args.get('source')  # Source demandée (json, csv ou sql)
    id = request.args.get('id')          # ID du produit (optionnel)

    # Vérifie si la source est valide
    if source not in source_author:
        value = "Wrong source"
        error = 1
    else:
        # Charge les données selon la source
        if source == "json":
            value = read_json()
        elif source == "csv":
            value = read_csv()
        else:
            value = read_sql()

        # Si un id est donné, filtre le produit
        if id:
            success = 0
            for element in value:
                if id == str(element['id']):
                    success = 1
                    value = [element]
            if success == 0:
                value = "Product not found"
                error = 1

    # Affiche le résultat dans product_display.html
    return render_template('product_display.html', value=value, error=error)

# Lit les produits depuis un fichier CSV
def read_csv():
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = list(reader)
    return result

# Lit les produits depuis un fichier JSON
def read_json():
    with open('products.json') as f:
        value = json.load(f)
    return value

# Lit les produits depuis une base SQLite
def read_sql():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row  # Pour accéder aux colonnes par nom
    cur = conn.cursor()
    cur.execute('SELECT * FROM Products')
    rows = cur.fetchall()
    conn.close()
    return rows

# Lance le serveur Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
