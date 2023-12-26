document.querySelector('#toggle').addEventListener('click', function () {
    var icone = document.querySelector('#ion');

    icone.setAttribute('name', this.checked ? 'close-outline' : 'menu-outline')
});