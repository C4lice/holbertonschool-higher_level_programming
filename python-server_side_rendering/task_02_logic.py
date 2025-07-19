from flask import Flask, render_template
import json

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

# Page items (affiche des données JSON)
@app.route('/items')
def items():
    with open('items.json') as f:         # Ouvre le fichier JSON
        items = json.load(f)              # Charge les données
    return render_template('items.html', items=items.get("items"))  # Affiche items

# Démarre le serveur
if __name__ == '__main__':
    app.run(debug=True, port=5000)
