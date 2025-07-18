const doc = document.querySelector('header');

function changeColor () {
  doc.style.color = '#FF0000';
}
document.getElementById('red_header').addEventListener('click', changeColor);
