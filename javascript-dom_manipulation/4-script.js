// Récupère la liste <ul> avec la classe "my_list"
const docs = document.querySelector('ul.my_list');

// Fonction pour ajouter un <li> avec le texte "Item"
function addElement () {
  const node = document.createElement('li'); // Crée un <li>
  const textnode = document.createTextNode('Item'); // Crée le texte
  node.appendChild(textnode); // Ajoute le texte au <li>
  docs.appendChild(node); // Ajoute le <li> à la liste
}

// Ajoute un clic sur le bouton avec id "add_item"
document.getElementById('add_item').addEventListener('click', addElement);
