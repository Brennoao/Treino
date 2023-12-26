const test = [
    { nome: 'item 1', icon: 'add-circle-outline', link: './html/page2.html' },
    { nome: 'item 2', icon: 'arrow-back-outline', link: './html/page3.html' },
    { nome: 'item 3', icon: 'bluetooth-outline', link: '#' },
    { nome: 'item 3', icon: 'bookmarks-outline', link: '#' },
];
// Selecione o elemento ul
const ul = document.querySelector('.List');

// Use a função map para criar um novo elemento li para cada item
const listItems = test.map((item, index) =>
    `<li key="${index}" class="insideList"><a href='${item.link}' class='menuAncor'><ion-icon name="${item.icon}"></ion-icon> ${item.nome}</a></li>`
).join('');

ul.innerHTML = listItems;