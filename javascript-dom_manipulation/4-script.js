const button = document.getElementById('add_item');
const list = document.querySelector('.my_list');

button.addEventListener('click', function () {
  const newItem = document.createElement('li'); // Crée un nouvel élément <li>
  newItem.textContent = 'Item';                 // Ajoute le texte "Item" dedans
  list.appendChild(newItem);                    // L'ajoute à la liste <ul>
});
