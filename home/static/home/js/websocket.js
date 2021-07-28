/* Create new instance of Websocket class and pass it the URL defined in routing.py */
let socket = new WebSocket(`wss://${window.location.host}/ws/home/`);

/* Add data coming from the consumer to a variable */
socket.onmessage = function(event) {
    let ws_tokens = JSON.parse(event.data);

    /* Create a variable to populate the large table, that loops through each token and creates a row with token data for each */
    let newDataLg = ws_tokens.map(ws_token => 
        `<tr>
            <td class="align-middle"><i class="far fa-star favourites"></i></td>
            <td class="align-middle">${ws_token.rank}</td>
            <td class="align-middle text-start">
                <a href="token_page/${ws_token.id}/" class="text-light link">
                    <img src=${ws_token.image} height="30"> 
                    ${ws_token.name}
                    <span class="text-uppercase fw-bold symbol">${ws_token.symbol}</span>
                </a>
            </td>
            <td class="align-middle">
                <!-- Buy button -->
                <a href="buy_token/${ws_token.id}/" class="btn rounded-0 text-uppercase">Buy</a>
            </td>
            <td class="align-middle text-end ${ws_token.direction === "higher" ? "higher" : ws_token.direction === "lower" ? "lower" : "same"}">${ws_token.price}</td>
            <td class="align-middle text-end">${ws_token.price_change.toFixed(2)}</td>
            <td class="align-middle text-end">${ws_token.market_cap}</td>
        </tr>`
    );

    /* Create a variable to populate the small table, that loops through each token and creates a row with token data for each */
    let newDataSm = ws_tokens.map(ws_token => 
        `<tr>
            <td class="align-middle"><img src=${ws_token.image} height="30"></td>
            <td class="text-start">
                <a href="token_page/${ws_token.id}/" class="text-light link">
                    ${ws_token.name}
                    <br><span class="bg-dark btn-sm">${ws_token.rank}</span>
                    <span class="text-uppercase fw-bold x-small">${ws_token.symbol}  ${ws_token.price_change.toFixed(2)}%</span>
                </a>
            </td>
            <td class="align-middle">
                <!-- Buy button -->
                <a href="buy_token/${ws_token.id}/" class="btn rounded-0 text-uppercase">Buy</a>
            </td>
            <td class="align-middle text-end price ${ws_token.direction === "higher" ? "higher" : ws_token.direction === "lower" ? "lower" : "same"}">£${ws_token.price}
                <br><span class="x-small text-light">MCap £${ws_token.market_cap}</span>
            </td>
        </tr>`
    );
    
    /* Add respective variables to the small-table and large-table divs */
    document.querySelector(".large-table").innerHTML = newDataLg;
    document.querySelector(".small-table").innerHTML = newDataSm;

    /* Replace all array items dividing commas with an empty string for correct table display */
    document.querySelector(".small-table").innerHTML = document.querySelector(".small-table").innerHTML.replace(/,/g, "");
    document.querySelector(".large-table").innerHTML = document.querySelector(".large-table").innerHTML.replace(/,/g, "");

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
