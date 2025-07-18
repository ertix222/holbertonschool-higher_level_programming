const toggle = document.getElementById('toggle_header');
const header = document.querySelector('header');

toggle.addEventListener('click', function () {
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
