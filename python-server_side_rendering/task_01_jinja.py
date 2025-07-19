# Importe Flask et la fonction render_template pour afficher des pages HTML
from flask import Flask, render_template

# Crée une instance de l'application Flask
app = Flask(__name__)


# Route pour la page d'accueil "/"
@app.route('/')
def home():
    return render_template('index.html')  # Affiche le fichier index.html


# Route pour la page "À propos" "/about"
@app.route('/about')
def about():
    return render_template('about.html')  # Affiche le fichier about.html


# Route pour la page "Contact" "/contact"
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Affiche le fichier contact.html


# Démarre l'application en mode debug sur le port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
