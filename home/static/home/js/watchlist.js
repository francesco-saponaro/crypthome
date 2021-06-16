//Get all table's favourite buttons
let favourites = document.querySelectorAll('.favourites');

//Change Icon class and input value on click
favourites.forEach(favourite => {
    favourite.addEventListener('click', e => {
        if (e.target.classList.contains('far')) {
            e.target.classList.remove('far');
            e.target.classList.add('fas', 'text-warning');
        } else {
            e.target.classList.remove('fas', 'text-warning');
            e.target.classList.add('far');
        }
    });
});