/* Create new instance of Websocket class and pass it the URL defined in routing.py */
let socket = new WebSocket(`wss://${window.location.host}/ws/home/`);

/* Add data coming from the consumer to a variable */
socket.onmessage = function(event) {
    let tokens = JSON.parse(event.data);
    console.log(tokens);

    /* Create a variable to populate the small table, that loops through each token and creates a row with token data for each */
    let newDataTokenPg = 
    );
    
    /* Add respective variables to the small-table and large-table divs */
    document.querySelector(".token-pg-container").innerHTML = newDataTokenPg;

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
}