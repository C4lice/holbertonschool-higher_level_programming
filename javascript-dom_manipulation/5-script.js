// Prend le header
const docs = document.querySelector('header');

// Change le texte du header
function addElement() {
  docs.textContent = 'New Header!!!';
}

// Quand on clique sur #update_header, on lance la fonction
document.getElementById('update_header').addEventListener('click', addElement);
