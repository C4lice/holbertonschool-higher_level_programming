// Prend l'élément avec id 'character'
const docs = document.getElementById('character');

// Demande les infos de la personne avce l'API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Lis la réponse
  .then(data => {
    const name = document.createTextNode(data.name); // Prend son nom
    docs.appendChild(name); // L’ajoute dans la page
  });
