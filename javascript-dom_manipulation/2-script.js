const button = document.getElementById('red_header');
const header = document.querySelector('header');

button.addEventListener('click', function() {
  header.classList.add('red');
});
