const test = [
    { nome: 'item 1', icon: 'bluetooth-outline' },
    { nome: 'item 2', icon: 'bluetooth-outline' },
    { nome: 'item 3', icon: 'bluetooth-outline' },
    { nome: 'item 3', icon: 'bluetooth-outline' },
];
// Selecione o elemento ul
const ul = document.querySelector('.List');

// Use a função map para criar um novo elemento li para cada item
const listItems = test.map((item, index) =>
`<li key="${index}" class="insideList"><a href='#' class='menuAncor'><ion-icon name="${item.icon}"></ion-icon> ${item.nome}</a></li>`
).join('');

ul.innerHTML = listItems;

console.table(test)