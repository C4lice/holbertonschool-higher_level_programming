// Quand la page est chargée
document.addEventListener('DOMContentLoaded', function () {

  // Prend l'élément avec id 'hello'
  const docs = document.getElementById('hello');

  // Appelle l'API pour dire bonjour en français
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(res => res.json()) // Lis la réponse
    .then(data => {
      docs.textContent = data.hello; // Affiche le bonjour
    });
});
