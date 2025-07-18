const doc = document.querySelector('header');

function addClass () {
  doc.classList.add('red');
}
document.getElementById('red_header').addEventListener('click', addClass);
