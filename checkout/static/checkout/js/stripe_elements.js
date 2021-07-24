// These first two variables are accessible thanks to the json script filter which allows external javascript files to access Django variables.
let stripe_public_key = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
let client_secret = document.getElementById('id_client_secret').innerText.slice(1, -1);
// Create an instance of stripe using our public key.
let stripe = Stripe(stripe_public_key);
// Create an instance of stripe elements.
let elements = stripe.elements();

let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
  };

// Create a card element and mount it to designated div.
let card = elements.create('card', { style: style });
card.mount(document.getElementById('card-element'));


// Handle realtime validation errors on the card element.
// Listen for Stripe errors everytime there is a change in the card element, and display them if any.
card.addEventListener('change', (event) => {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        errorDiv.innerHTML = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`
    } else {
        errorDiv.textContent = '';
    }
})