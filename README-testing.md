# Crypthome Testing 
This is a page dedicated to the project's testing process.  
## Validation
* HTML
    * Fixed all relevant errors. Only errors showing on the [HTML validator](https://validator.w3.org/) are related to Django template syntax and missing elements on "includes" file.
* CSS
    * No errors found on any of the two CSS files on the [Jigsaw](https://jigsaw.w3.org/css-validator/) validator.
* Javascript
    * Only errors are shown on the Portfolio page script as Jinja template syntax is used in the Javascript code to pass data into the AmCharts function.
    * No errors on [JSHint](https://jshint.com/) otherwise, only warninga about template literal syntax and arrow functions belonging to ES6.
* Python
    * Fixed most errors showing with Pylint.
    * I could't fix the exceptions below for various reasons:
        * Most objects give errors like the following: "Class 'Position' has no 'objects' member". I don't understand what is causing this error, as all instances have the member and the code works fine.
        * The CheckoutConfig class in the checkout's apps.py shows an "imported but never used" error on the "checkout.signals" import, however it is being used by other files.
        * Some models give errors like the following: "Instance of 'ForeignKey' has no 'price' member". I don't understand what is causing this error, as all foreign keys have the member and the code works fine.
        * I cannot divide the lines in the AUTH_PASSWORD_VALIDATORS list as i did on all other lines too long. Somehow if I do, no matter where I place the trailing slash, the code stops working.
        * Same issue as above occurs with some of the replace methods in home.views, there are a few in which if I place a trailing slash the code stops working.
        * In the asgi.py file I get a "module not imported at top of file error", however I had to import them below the get_asgi_application() method in order for the code to work.

## Automated Python testing
* I had great trouble testing for views that require authentication. I am afraid I haven't been able to research or practice the TestCase class, however I kept all tests that passed and the rest will be tested manually nonetheless.
![Automated Pythone tests](/testing-screenshots/automated-python-tests.png) 

## Client stories testing
The website is divided in two major sections: Crypthome and Crypthomerch.   
The flow is designed so that every page available to the user is accessible through the Navbar, which changes layout depending on screen size.  
The nav link in fact move at the top of the page on screens smaller than 1000px and the portfolio link disappears on screens smaller than 500px. The portfolio link however, can also be found in the "My Account" dropdown. 
The Crypthome and Crypthomerch links and logos interchange with each other depending on which of the two section is the user.
The "Register" and "Log in" links interchange with the "Portfolio", "Profile" and "Log out" links depending on if the user is logged in or not.  
### As a user i want:
* I want to learn about cryptocurrencies history and purpose, to find out what is behind the latest mass interest.
* I want to learn to trade cryptocurrencies, to one day profit from it.
* I want to learn how to interpret cryptocurrencies data and charts, to learn how to trade them.
* I want to check cryptocurrencies latest data and charts, to plan my next trading move.
    * Home page![Home Page](/testing-screenshots/home-page.png)
    * Home page table price update![Home Page price update](/testing-screenshots/home-page-price-update.png)
    * Token page![Token Page](/testing-screenshots/token-page.png) 
    * Token page price update![Token Page price update](/testing-screenshots/token-page-price-update.png)
    * Token page "buy token" button![Token page buy token button](/testing-screenshots/token-page-buy-bitcoin-link.png) 
    * Token page website link![Token page website link](/testing-screenshots/token-page-website-link.png) 
    * Token website page![Token page website link2](/testing-screenshots/token-page-website-link2.png) 
    * Token page Reddit link![Token page Reddit link](/testing-screenshots/token-page-reddit-link.png) 
    * Token Reddit page![Token page Reddit link2](/testing-screenshots/token-page-reddit-page.png) 
    * Token page Github link![Token page Github link](/testing-screenshots/token-page-github-link.png) 
    * Token Github page![Token page Github link2](/testing-screenshots/token-page-github-link2.png) 
    * Token page Chart link![Token page Chart link](/testing-screenshots/token-page-github-link.png) 
    * Token Coingecko Chart page![Token page Chart link2](/testing-screenshots/token-page-chart-link2.png)  
* I want to register and/or login to practice trading cryptocurrencies, to one day open a real account.
* I want to register and/or login to buy a token, to learn how to trade.
* I want to register and/or login to sell a token, to take profit on my position.
* I want to register and/or login to check and manage my portfolio, to make sure my strategy is working and/or come out with a new plan.
    * Buy token page![Buy token page](/testing-screenshots/buy-token-page.png)
    * Buy token page price update![Buy token page price update](/testing-screenshots/buy-token-page-price-update.png)
    * Buy token page "Add10k" to allowance button![Buy token page "Add10k" to allowance button](/testing-screenshots/buy-token-page-add10ktoallowance-button.png)
    * Buy token page "Buy token" button![Buy token page "Buy token" button](/testing-screenshots/buy-token-page-buy-button.png)
    * Successful token purchase message and Portfolio page redirect![Buy token page](/testing-screenshots/token-bought-and-redirect-to-portfolio-and-cashandvaluevalueschnaged.png)
    * Successful "available equity" value deduction upon purchase![Available equity](/testing-screenshots/amount-over-allowance-and-availableequityamountchanged.png)
    * Token purchase failure message when attempting to buy more than allowance value![Amount over allowance](/testing-screenshots/amount-over-allowance-message.png)
    * Portfolio page, with graph chart of portfolio allocation, cash available to spend and total portfolio value![Portfolio page](/testing-screenshots/chart-value-cash-display-and-values.png)
    * Portfolio page open positions table![bought-positions-table](/testing-screenshots/bought-positions-table.png)
    * Open positions table sell button![bought-positions-table-sell-button](/testing-screenshots/bought-positions-table-sell-button.png)
    * Successful position selling message and change of cash available value![position-sold-message-and-cash-value-change](/testing-screenshots/position-sold-message-and-cash-value-change.png)
    * Crypto search bar![search-bar](/testing-screenshots/search-bar.png)
    * Crypto search result![search-result](/testing-screenshots/search-results.png)
    * Crypto search result price update![Crypto search result price update](/testing-screenshots/search-result-price-update.png)
* I want to buy merchandise, to express my interest in cryptocurrencies or to gift to my friends.
* I want to register and/or login to check my profile page to change my delivery details.
* I want to register and/or login to check details of my past merchandise purchases.
    * Crypthomerch home page![Crypthomerch home page](/testing-screenshots/crypthomerch-home-page.png)
    * Crypthomerch accordion![Crypthomerch accordion](/testing-screenshots/crypthomerch-home-page-accordion.png)
    * Crypthomerch accordion selection![Buy token page](/testing-screenshots/crypthomerch-home-page-accordion-selection.png)
    * Crypthomerch accordion selection result![Buy token page](/testing-screenshots/crypthomerch-home-page-selection-result.png)
    * All products page![All products page](/testing-screenshots/all-products-page.png)
    * All clothing result![All clothing result](/testing-screenshots/all-clothing-result.png)
    * Tag selection![Tag selection](/testing-screenshots/tag-selection.png)
    * Tag selection result![Tag selection result](/testing-screenshots/tag-selection-result.png)
    * Filter selection![Filter selection](/testing-screenshots/merch-filter-selection.png)
    * Filter selection result![Filter selection result](/testing-screenshots/merch-filter-result.png)
    * Product detail page (with image)![Product detail page (with image)](/testing-screenshots/product-with-image-page.png)
    * Product detail page (no image)![Product detail page (no image)](/testing-screenshots/product-with-no-image-page.png)
    * Product full size image target_blank redirect![Product full size image target_blank redirect](/testing-screenshots/target-blank-full-size-image-link.png)
    * Add to bag success message![Add to bag success message](/testing-screenshots/add-to-bag-message.png)
    * Shopping bag page![Shopping bag page](/testing-screenshots/shopping-bag-page.png)
    * Successfully updated shopping bag message![Successfully updated shopping bag message](/testing-screenshots/update-shopping-bag-message.png)
    * Successfully removed from shopping bag message![Successfully removed from shopping bag message](/testing-screenshots/remove-from-shopping-bag-message.png)
    * Shopping bag totals![Shopping bag totals](/testing-screenshots/shopping-bag-totals.png)
    * Checkout page![Checkout page](/testing-screenshots/checkout-page.png)
    * Checkout page validation![Checkout page validation](/testing-screenshots/checkout-page-validation.png)
    * Checkout authentication step![Checkout authentication step](/testing-screenshots/checkout-authentication-step.png)
    * Checkout failed authentication![Checkout failed authentication](/testing-screenshots/failed-authentication.png)
    * Successful checkout attempt![Successful checkout attempt](/testing-screenshots/successful-checkout-attempt.png)
    * Checkout loading spinner![Checkout loading spinner](/testing-screenshots/checkout-loading-spinner.png)
    * Successful checkout page and message![Successful checkout page and message](/testing-screenshots/successful-checkout-page-and-message.png)
    * Profile page![Profile page](/testing-screenshots/profile-page.png)
    * Profile page update![Profile page update](/testing-screenshots/profile-page-update.png)
    * Merch search bar![Merch search bar](/testing-screenshots/merch-search-bar.png)
    * Merch search result![Merch search result](/testing-screenshots/merch-search-result.png)
    * Empty shopping bag![Empty shopping bag](/testing-screenshots/empty-shopping-bag.png)

    * Add product with no image![Add product with no image](/testing-screenshots/add-product-with-no-image.png)
    * Add product with image![Add product with image](/testing-screenshots/add-product-with-image.png)
    * Edit product page![Edit product page](/testing-screenshots/product-editing-page.png)
    * Successfully remove product image![Successfully remove product image](/testing-screenshots/successfully-remove-image.png)
    * If image file absent then if image URL is present it will show instead![If image file absent then if image URL is present it will show instead](/testing-screenshots/if-not-image-file-url-will-takeover.png)
    * If both image file and image URL are present, image will show![If both image file and image URL are present, image will show](/testing-screenshots/if-image-and-image-url-image-will-takeover.png)
    * Add/edit product pages image widget![Add/edit product pages image widget](/testing-screenshots/add-image-widget.png)
    * Add/edit forms required fields validation![Add/edit forms required fields validation](/testing-screenshots/add-edit-product-form-required-validation.png)
    * Add/edit forms Image url field validation![Add/edit forms Image url field validation](/testing-screenshots/add-edit-product-form-imageurl-validation.png)
    * Successfully remove product![Successfully remove product](/testing-screenshots/remove-product.png)
    * Sign out page![Sign out page](/testing-screenshots/sign-out-page.png)
    * Sign out message![Sign out message](/testing-screenshots/sign-out-message.png)
    * Sign in with wrong credentials![Sign in with wrong credentials](/testing-screenshots/sign-in-wrong-credentials.png)
    * Successful sign in message![Successful sign in message](/testing-screenshots/sign-in-message.png)
    * Password reset![Password reset](/testing-screenshots/reset-password.png)
    * Sign up page![Sign up page](/testing-screenshots/sign-up-page.png)
    * Sign up verify address step![Sign up verify address step](/testing-screenshots/register-verify-email-address.png)
    * Address verified message![Address verified message](/testing-screenshots/address-verified-message.png)

## Defensive programming tests
* Attempt to access Portfolio page while logged out![Attempt to access Portfolio page while logged out](/testing-screenshots/defensive-portfolio2.png)
* Attempt to access Profile page while logged out![Attempt to access Profile page while logged out](/testing-screenshots/defensive-profile.png)
* Attempt to access Add product functionality while logged out![Attempt to access Add product functionality while logged out](/testing-screenshots/defensive-add-product2.png)
* Attempt to access Edit product functionality while logged out![Attempt to access Edit product functionality while logged out](/testing-screenshots/defensive-edit.png)
* Attempt to access Remove product functionality while logged out![Attempt to access Remove product functionality while logged out](/testing-screenshots/defensive-delete.png)
* Attempt to access Add/Edit/Delete functionalities while not a superuser![Attempt to access Add/Edit/Delete functionalities while not a superuser](/testing-screenshots/defensive-add-edit-delete-not-superuser.png)
* Attempt to edit non existing product![Attempto edit non existing product](/testing-screenshots/404-when-editing-nonexistent.png)
* Attempt to remove non existing product![Attempto remove non existing product](/testing-screenshots/404-when-removing-nonexistent.png)
* Attempt to access order history while logged out![Attempt to access order history while logged out](/testing-screenshots/logged-out-history.png)
* Attempt to access another user order history![Attempt to access another user order history](/testing-screenshots/defensive-order-history.png)

* 404 page![404 page](/testing-screenshots/404-page.png)

## Lighthouse
* Passed all audits.
* Scores:
    * Performance - 78
    * Accessibility - 81
    * Best Practices - 87
    * SEO - 80

## Browsers
* Mozilla, Chrome, Edge and Safari all display same projected layout and have no issues at any screen sizes.

## Screen sizes
* The website is fully responsive through the Boostrap grid system and media queries, starting from a screen size as small as 378px upwards.
* All features are available and visible on every screen size. 
* The nav links move to the top of the screen from 1000px downwards.

## Bugs discovered
* I had great trouble deploying Celery, hence the many repeated commit messages towards the end of the projcts. However after plenty of research online I managed to deploy it successfully. There were three main issues:
    * In the Procfile had to remove Gunicorn and install Daphne instead (as it is an asynchronous application) and pass it my "application" variable from asgi.py. 
    * In the asgi file I also had to import the "get_asgi_application" method at the very top before all other imports.
    * In the Procfile I had to pass the celery worker and beat, but I had to do it in one line as Heroku can only run two dynos at the time apparently. So by adding -B to the worker command, I managed to add the beat to it, therefore having the worker and beat in one command.
* Upon changing a model field of the Position model in home.models and running the "makemigrations" command, I have been unable to either migrate or access the model in Admin, and kept getting an OperationalError. Somehow the field changed but there was a model instance in the database with the old field, therefore giving an error.   
After many attempts to fix it I had to delete both my Sqlite3 and PostgreSQL databases, reinstall them, rerun migrations and load the data again. This fixed the issue.
* On the coins_desc variable of the home.views, unfortunately I couldn't use a single regex to remove all anchor tags of the text coming from the API. For each tag I had to copy exaxt matched string to replace.  
I have taken this regex from stack overflow '("<(?:a\b[^>]*>|/a>)", "")' but was not working. Even the tutors were not able to find the issue as the regex are valid and were tested with a regex validator.
* Upon testing the "fail authentication" payment scenario with stripe, I get the "Devtools failed to load source map" warning, however it doesn't affect the code.
* Once the app starts idling after 30 minutes, the app changes from up to down, and exits with status 0 and therefore the price stops being updated automatically.  
After researching on Stack Overflow, I have discovered that, If on the Heroku free tier, then this is expected behavior. It should restart on the next web request to it, so it is definitely not an issue and unnoticeable unless the user stays on the same page for 30 minutes. But the latest terms for the free tier don't let you keep it on 24/7 even if that many requests come in.