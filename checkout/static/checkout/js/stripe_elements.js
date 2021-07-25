// These first two variables are accessible thanks to the json script filter which allows external javascript files to access Django variables.
let stripePublicKey = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
let clientSecret = document.getElementById('id_client_secret').innerText.slice(1, -1);
// Create an instance of stripe using our public key.
let stripe = Stripe(stripePublicKey);
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

// Handle form submit. From Stripe.
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  // Prevent default action, which in this case is POST.
  // Instead we'll execute code beloe
  ev.preventDefault();
  // Before we call out stripe we want to disable both the card element and the
  // submit button, to prevent multiple submissions.
  card.update({'disabled': true});
  document.getElementById('submit-button').setAttribute('disabled', true)
  // If the client secret was rendered server-side as a data-secret attribute
  // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
        // Show error to your customer (e.g., insufficient funds)
        errorDiv.innerHTML = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
        // If there is an error we also want to re enable both the card element
        // and the submit button to allow the user to fix it.
        card.update({'disabled': false});
        document.getElementById('submit-button').setAttribute('disabled', false)
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
        form.submit();
      }
    }
  });
});