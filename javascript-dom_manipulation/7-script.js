// Prend l'élément avec id 'list_movies'
const docs = document.getElementById('list_movies');

// Prépare la requête pour récupérer les films Star Wars
const request = new Request('https://swapi-api.hbtn.io/api/films/?format=json');

// Envoie la requête
fetch(request)
  .then((response) => {
    return response.json(); // Transforme la réponse en JSON
  })
  .then((data) => {
    // Parcourt chaque film dans la réponse
    data.results.forEach(element => {
      const node = document.createElement('li'); // Crée un <li>
      const textnode = document.createTextNode(element.title); // Prend le titre du film
      node.appendChild(textnode); // Ajoute le titre dans le <li>
      docs.appendChild(node); // Ajoute le <li> dans la liste
    });
  });
