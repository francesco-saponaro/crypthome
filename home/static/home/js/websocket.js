/* Create new instance of Websocket class and pass it the URL defined in routing.py */
let socket = new WebSocket(`wss://${window.location.host}/ws/home/`);

/* Add data coming from the consumer to a variable */
socket.onmessage = function(event) {
    let tokens = JSON.parse(event.data);
    console.log(tokens);

    /* Create a variable to populate the large table, that loops through each token and creates a row with token data for each */
    let newDataLg = tokens.map(token => 
        `<tr>
            <td class="align-middle"><i class="far fa-star favourites"></i></td>
            <td class="align-middle">${token.rank}</td>
            <td class="align-middle text-start">
                <a href="${token.id}" class="text-light link">
                    <img src=${token.image} height="30"> 
                    ${token.name}
                    <span class="text-uppercase fw-bold symbol">${token.symbol}</span>
                </a>
            </td>
            <td class="align-middle">
                <!-- Buy button trigger modal -->
                <button type="button" class="btn rounded-0 text-uppercase" data-bs-toggle="modal" data-bs-target="#staticBackdrop${token.name}">
                    Buy
                </button>

                <!-- Modal -->
                <div class="modal fade" id="staticBackdrop${token.name}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content crypto-modal">
                            <div class="modal-header text-light">
                                <h5 class="modal-title text-uppercase" id="staticBackdropLabel">Buy ${token.name}</h5>
                                <button type="button" class="btn-close bg-secondary" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>

                            <div class="modal-body">
                                <!-- Token data -->
                                <div class="row pb-3 modal-row">
                                    <div class="col-6">
                                        <p class="modal-data-h">Price</p>
                                        <p class="modal-data mb-0">£${token.price}</p>
                                    </div>
                                    <div class="col-6">
                                        <p class="modal-data-h">24h %</p>
                                        <p class="modal-data mb-0">${token.price_change.toFixed(2)}%</p>
                                    </div>
                                </div>

                                <!-- Monetary inputs -->
                                <div class="row pt-3">
                                    <div class="col-12 pb-3 text-start">
                                        <label for="token-amount" class="pb-1 modal-data-h">Amount ${token.name}</label>
                                        <input class="form-control border-0 rounded-0 bg-secondary text-center" type="number" id="token-amount" name="token-amount" placeholder="Amount ${ token.name}">
                                    </div>
                                    <div class="col-12 text-start">
                                        <label for="gbp-amount" class="pb-1 modal-data-h">Total (GBP)</label>
                                        <input class="form-control border-0 rounded-0 bg-secondary text-center" type="number" id="gbp-amount" name="gbp-amount" placeholder="Total (GBP)">
                                    </div>
                                </div>
                            </div>

                            <div class="modal-footer">
                                <!-- Cancel and buy buttons -->
                                <button type="button" class="btn cancel-sell-btn" data-bs-dismiss="modal">
                                    Cancel
                                </button>
                                <button type="button" class="btn">
                                    Buy
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
            <td class="align-middle text-end ${token.direction === "higher" ? "higher" : token.direction === "lower" ? "lower" : "same"}">${token.price}</td>
            <td class="align-middle text-end">${token.price_change.toFixed(2)}</td>
            <td class="align-middle text-end">${token.market_cap}</td>
        </tr>`
    );

    /* Create a variable to populate the small table, that loops through each token and creates a row with token data for each */
    let newDataSm = tokens.map(token => 
        `<tr>
            <td class="align-middle"><img src=${token.image} height="30"></td>
            <td class="text-start">
                <a href="${token.id}" class="text-light link">
                    ${token.name}
                    <br><span class="bg-dark btn-sm">${token.rank}</span>
                    <span class="text-uppercase fw-bold x-small">${token.symbol}  ${token.price_change.toFixed(2)}%</span>
                </a>
            </td>
            <td class="align-middle">
                <!-- Buy button trigger modal -->
                <button type="button" class="btn rounded-0 text-uppercase" data-bs-toggle="modal" data-bs-target="#staticBackdropSmall${token.name}">
                    Buy
                </button>

                <!-- Modal -->
                <div class="modal fade" id="staticBackdropSmall${token.name}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content crypto-modal">
                            <div class="modal-header text-light">
                                <h5 class="modal-title text-uppercase" id="staticBackdropLabel">Buy ${token.name}</h5>
                                <button type="button" class="btn-close bg-secondary" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>

                            <div class="modal-body">
                                <!-- Token data -->
                                <div class="row pb-3 modal-row">
                                    <div class="col-6">
                                        <p class="modal-data-h">Price</p>
                                        <p class="modal-data mb-0">£${token.price}</p>
                                    </div>
                                    <div class="col-6">
                                        <p class="modal-data-h">24h %</p>
                                        <p class="modal-data mb-0">${token.price_change.toFixed(2)}%</p>
                                    </div>
                                </div>

                                <!-- Monetary inputs -->
                                <div class="row pt-3">
                                    <div class="col-12 pb-3 text-start">
                                        <label for="token-amount" class="pb-1 modal-data-h">Amount ${token.name}</label>
                                        <input class="form-control border-0 rounded-0 bg-secondary text-center" type="number" id="token-amount" name="token-amount" placeholder="Amount ${ token.name}">
                                    </div>
                                    <div class="col-12 text-start">
                                        <label for="gbp-amount" class="pb-1 modal-data-h">Total (GBP)</label>
                                        <input class="form-control border-0 rounded-0 bg-secondary text-center" type="number" id="gbp-amount" name="gbp-amount" placeholder="Total (GBP)">
                                    </div>
                                </div>
                            </div>

                            <div class="modal-footer">
                                <!-- Cancel and buy buttons -->
                                <button type="button" class="btn cancel-sell-btn" data-bs-dismiss="modal">
                                    Cancel
                                </button>
                                <button type="button" class="btn">
                                    Buy
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
            <td class="align-middle text-end price ${token.direction === "higher" ? "higher" : token.direction === "lower" ? "lower" : "same"}">£${token.price}
                <br><span class="x-small text-light">MCap £${token.market_cap}</span>
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
