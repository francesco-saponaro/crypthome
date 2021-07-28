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

// Disable submit button modal trigger by default.
document.getElementById('submit-button').classList.add('disabled');

// Enable submit button modal trigger if all form fields have been filled correctly
// and the stripe card element is complete.
var form = document.getElementById('payment-form');
form.addEventListener('change', () => {
    if ($('#id_full_name').val() === "no") {
        card.addEventListener('change', (event) => {
            if (event.complete) {
                document.getElementById('submit-button').classList.remove('disabled');
            } else {
                document.getElementById('submit-button').classList.add('disabled');
            }
        })
    }
})

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
    };

    // Enable submit button modal trigger if the stripe element is complete and
    // all form fields have been filled correctly.
    if (event.complete) {
        form.addEventListener('change', () => {
            if ($('#id_full_name').val() === "no") {
                document.getElementById('submit-button').classList.remove('disabled');
            } else {
                document.getElementById('submit-button').classList.add('disabled');
            }
        })
    }
})

// Handle form submit. From Stripe.
form.addEventListener('submit', function(ev) {
    // When the user clicks the submit button this eevnt prevents the form from 
    // submitting, the default action, which in this case is POST.
    // Instead we'll execute code below
    ev.preventDefault();
    // Instead disables the card element and submit button to prevent multiple
    // submissions, fades out the form and triggers the loading overlay.
    card.update({'disabled': true});
    document.getElementById('submit-button').setAttribute('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Then we create a few variables to capture the form data we can't put in the 
    // the payment intent here. Like checking the if the user checked the save info box.
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    // And instead post the above data to the cache_checkout_data view.
    // The view in views.py updates the payment intent and returns a 200 response.
    // At which point, when it's "done", we call confirmCardPayment from stripe
    // and if everything is ok, submit the form
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function () {
        // If the client secret was rendered server-side as a data-secret attribute
        // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                  name: form.full_name.value.trim(),
                  phone: form.phone_number.value.trim(),
                  email: form.email.value.trim(),
                  address:{
                      line1: form.street_address1.value.trim(),
                      line2: form.street_address2.value.trim(),
                      city: form.town_or_city.value.trim(),
                      country: form.country.value.trim(),
                      state: form.county.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address:{
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim(),
                }
            }
        }).then(function(result) {
            // If there is an error in the form, the loading overlay will be hidden,
            // the card element re enabled and the error displayed for the user.
            if (result.error) {
                // Show error to the user (e.g., insufficient funds).
                let errorDiv = document.getElementById('card-errors');
                errorDiv.innerHTML = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                // Fade in the form and out the trigger loading overlay.
                $('#payment-form').fadeToggle(100)
                $('#loading-overlay').fadeToggle(100)
                // Re enable both the card element and the submit button to allow the user to fix it.
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
    }).fail(function () { 
          // If anything goes wrong posting the data to the view we reload the page
          // without ever charging the user.
          location.reload();
    })
});
