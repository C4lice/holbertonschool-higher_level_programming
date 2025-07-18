const doc = document.querySelector('header');

function toggleClass () {
  doc.classList.toggle('red');
  doc.classList.toggle('green');
}
document.getElementById('toggle_header').addEventListener('click', toggleClass);
