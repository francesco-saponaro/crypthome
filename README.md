# Crypthome
# UX
## Project Goals
The purpose of this website is to allow users to learn about cryptocurrencies and learn how to trade them by being able to explore data and history on a selected token details page, demo buy and sell tokens, and manage positions via the portfolio page.  
The user will also be able to purchase crypto merchandise via the e-commerce Crypthomerch section, therefore also bringing monetary incentive to the website owner. 
### Note for the assessor
Although a profile is not needed to explore the website and buy merchandise from Crypthomerch, most of Crypthome features like demo buying and selling tokens, and access to the portfolio page are available once registered and logged in.  
If you would like to test run the website and have fun with the features without having to create an account, you can use this account which has plenty of positions and history on its name:  
**USERNAME: fran, PASSWORD: codeinstitute**.  
Enjoy :)

## User Stories
### First time users
* I want to learn about cryptocurrencies history and purpose, to find out what is behind the latest mass interest.
* I want to learn to trade cryptocurrencies, to one day profit from it.
* I want to learn how to interpret cryptocurrencies data and charts, to learn how to trade them.
* I want to register and/or login to practice trading cryptocurrencies, to one day open a real account.
* I want to register and/or login to buy a token, to learn how to trade.
* I want to register and/or login to sell a token, to take profit on my position.
* I want to register and/or login to check and manage my portfolio, to make sure my strategy is working and/or come out with a new plan.
* I want to buy merchandise, to express my interest in cryptocurrencies or to gift to my friends.
* I want to register and/or login to check my profile page to change my delivery details.
* I want to register and/or login to check details of my past merchandise purchases.
### Returning users
* I want to learn to trade cryptocurrencies, to one day profit from it.
* I want to check cryptocurrencies latest data and charts, to plan my next trading move.
* I want to login to practice trading cryptocurrencies, to one day open a real account.
* I want to login to buy a token, to learn how to trade.
* I want to login to sell a token, to take profit on my position.
* I want to login to check and manage my portfolio, to make sure my strategy is working and/or come out with a new plan.
* I want to buy merchandise, to express my interest in cryptocurrencies or to gift to my friends.
* I want to login to check my profile page to change my delivery details.
* I want to login to check details of my past merchandise purchases.

## Design Choices
The website is fully responsive.  
Due to the technologic nature of cryptocurrencies a retro design, logo font and colors were adopted. This contributes to give the website an overall early '00s feel.   
Bootstrap framework was chosen due to its consistent design, responsiveness features and wide browser compatibility.
### Fonts
* The 'Press Start 2P' font was used for the logo, due to its retro feel.
* The 'Lato font' was used for its simplicity and versatility.
### Icons
* All Icons were taken from Font awesome and were chosen based on their clearness and message conveying ability.
* Crypto logos come directly from the Coingecko API.
### Colours
* The logo color is a aqua and green gradient, the combination was chosen due to its retro effect.
* The majority of the website uses sharp shades of colors for the same reason mentioned above.
* The body color is a dark blue to balance the rest of the website sharp colors.
### Images
* The recipe images were chosen based on their definition and ability to portray the item. However, superusers are able to chose whichever image suit their taste. If an image is not uploaded, a placeholder image is loaded instead, informing users that no image is available.

## Wireframes
[Link to Wireframes](/wireframes/crypthome-wireframes.pdf)

## Database schema
The PostgreSQL database contains 8 models:
* Order - Stores users merchandise orders. Has a foreign key with the UserProfile, in order to access a user's orders.
* OrderLineItem - Stores order items. Has a foreign key to the Order and product models to access all their fields.
* Position - Stores tokens data coming from the API and sends it to the websocket through channels.
* BuyToken - Stores users token orders. Has a foreign key with the UserProfile in order to access a user's orders.
* Allowance - Stores users trading allowance. Has a foreign key with the UserProfile in order to access a user's allowance.
* Category - Stores clothing available categories.
* Merch - Store a product details. Has a foreign key with the Category model to assign the product to desired category.
* UserProfile - Stores users delivery details. Has a OneToOne relation to the Django User model.

## Features
### Existing features
* Register and log in 
    * Allows users to create an account and log in to take advantage of all features. 
* Log out
    * Allows users to log out to protect their profile.
* Every minute cryptocurrencies data tables
    * Allows users to have quick access to a token's basic data and buy button, it updates every minute with new actual data.
    * The price turns either green, red or white depending on if it's direction since previous minute. 
    * It has a date object updating every minute, telling the user exactly when the price was last updated.
* Token details page
    * Allows users to see detailed token data, it's history and purpose, trading chart link, other important links and a "Buy" button. The "Price" in this page also updates every minute.   
* Buy token page
    * Allows logged in users to demo buy a token. The "Price" in this page also updates every minute. 
    * It contains an "available equity" value telling the user how much "GBP" they have still available to spend, based on the allowance they have and amount already invested.
    * It contains an "add 10k" button which add £10000 gbp to a user allowance. So the user has complete freedom of how big they want their allowance to be from £10000 upwards.
* Portfolio page
    * Allows users to manage their portfolio, positions, allowance and profit/loss.
    * It contains a "cash" value telling the user how much "GBP" they have still available to spend, based on the total portfolio value minus the amount already invested.
    * It contains a "value" value telling the user the total amount of their portfolio, based on their available cash plus the amount invested.
    * It contains a graph chart representation of the user investments.
    * It contains the user's investments data represented as a table row, along with a "sell" button to sell their investment.
* Merchandise slideshow
    * A slideshow in the Crypthomerch home page.
* Merch accordion menu
    * Accordion containing products categories and filter options.
* Products page
    * Allows users to browse for products.
    * Contains product cards with image, name, price, category and rating info.
    * Contains a "sort by" filtering select box.
    * Contains a number value of amount of products displayed.
    * Contains a "back to top" button.
* Product details page
    * Allows users to access a larger product image and add the product to the shopping bag.
    * Contains same product details as products page along with size and quantity selectors.
    * Contains a "keep shopping" button redirecting you to the all products page and an "add to bag" button.
* Shopping bag page
    * Contains all items added by the user and allows users to update the amounts for each item or delete them from the shopping bag.
    * Contains the bag total, delivery cost and grand total amounts, along with a warning message telling the user how much is left to spend to get free delivery.
    * Contains a "secure checkout" button to redirect you to the checkout page. 
* Checkout page
    * Allows users to fill out their delivery and credit card details, and to complete their order.
    * Contains all info of shopping bag page along with delivery details and credit card form
* Checkout success page
    * Contains a summary of the succesfull order.
* Profile page
    * Allows users to change their default delivery information and merchandise order history.
    * Contains a default delivery information form.
    * Contains a responsive table of the user's merchandise order history. Each order is clickable and redirected to a page of order's detailed summary.
* Product management features
    * Allows superusers to add, edit or delete a product.
* Search bars
    * Allows users to search for either cryptocurrencies or products, depending on which section of the website the user is.
* Django messages
    * The website uses pop us message cards to advise the user on important events.
* Back to previous page buttons
    * Most website pages contain a go back to previous url button, to improve user experience and facilitate navigation. 
### Potential features
* Crypto orders history.
* Incorporated trading chart, at the moment there is a link redirecting to the tokens Coingecko chart page.
* Watchlist page containing a user's favourite tokens.

## Technologies used
* HTML 
    * The project uses HTML5 as it is the latest and upgraded version of HTML.
* CSS
    * The project uses CSS3 as it is an easy, consistent, lightweight and fast language to style the HTML.
* JavaScript
    * The project uses Javascript to interact with the DOM.
* [JQuery](https://jquery.com/)
    * JQuery is used to interact with the DOM.
* Python
    * The project uses Python for back end implementation.
* [Django](https://www.djangoproject.com/)
    * The project uses Django macro framework for the back end and for interaction with front end.
* [FontAwesome](https://fontawesome.com/)
    * The project uses FontAwesome to take advantage of  the extensive icons libraries.
* [Bootstrap5](https://getbootstrap.com/)
    * The project uses Bootstrap5 due to its consistent design, responsiveness features and wide browser compatibility.
* [Stripe](https://stripe.com/en-gb-fr)
    * The project uses Stripe as a payment service.
* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
    * The Project uses Celery to process task queues.
* [Redis](https://redis.io/)
    * The project uses Redis as the message broker, to send and receive messages.
* [Channels](https://channels.readthedocs.io/en/stable/)
    * The project uses Channels to handle the websocket connection.
* [AmCharts](https://www.amcharts.com/)
    * The project uses AmCharts library to render the portfolio investments chart.
* [PostgreSQL](https://www.postgresql.org/)
    * PostgreSQL was used as the relational database.

## Testing
### Validation
* HTML
    * Only errors showing on [HTML validator](https://validator.w3.org/) are related to jinja syntax.
* CSS
    * No errors shown on [Jigsaw](https://jigsaw.w3.org/css-validator/) validator.
* Javascript
    * Only errors are shown on the dashboard HTML page script as Jinja template syntax is used in the Javascript code to pass data into the AmCharts function.
    * No errors on [JSHint](https://jshint.com/) otherwise.
* Python
    * No errors shown on [PEP8 online](http://pep8online.com/)
    * Only warnings, regarding trailing whitespaces
### Client stories testing
The website flow is designed so that every page available to the user is accessible through the Navbar or slider menu, which interchange depending on screen size. The "Register" and "Log in" links interchange with the "Profile" and "Log out" links depending on if the user is logged in or not.  
Defensive programming was implemented to:
* Make sure logged in or logged out users are not able to access other user`s accounts and pages by pasting their URL. On trying to do so they will be redirected to the Home page.
* Make sure users dont log in without authentication by pasting the right URL. On trying to do so they will be redirected to the Home page.
* In the case of a 404 or 500 error the user will be redirected to a page informing him of the error and with a link to go back to the Home page.
#### As a user i want:
* I want to browse through all recipes, to find inspiration for a meal.
    * As soon as the user land in the home page he will see all available recipes displayed in panels and paginated.
    * By clicking on the desired recipe he will be redirected to the recipe page.  
* I want to browse recipes by:
    * Recipe name
    * Ingredient
    * Meal type
    * Difficulty
    * Prep time
    * Calories
    * Country
    * Dietary requirements
    * Allergens
    * High protein
        * By clicking the "search" button on the top left of the page, selecting your parameters and clickin the "apply" button.
        * The "search" button is available on every page but the "profile" and "dashboard" pages.
* I want to log in to do a quick search for a recipe, to find inspiration for a meal when I am short of time.
    * The "Quick search" dropdown menu page is located in the Navbar or Side menu depending on screen sizes.
* I want to see the available stats, to see what users are most interested in or who is most active.
    * The "Dashboard" page link is located in the Navbar or Side menu depending on screen sizes.
* I want to register to add, edit and delete my own recipes.
    * The "Register" page link is available whenever logged out and located in the Navbar or Side menu depending on screen sizes.
* I want to log in to add, edit or delete a recipe.
    * The "Log in" page link is available whenever logged out and located in the Navbar or Side menu depending on screen sizes.
* I want to log in to add a recipe.
    * The "Add recipe" page button is located on the right side of the screen and available on all pages but the "Dashboard" page, whenever logged in.
    * By clicking on the button, filling the form and clicking the "Add recipe" button.
* I want to log in to edit my own recipes.
    * The "Edit recipe" page button is located on each of the user's recipe panel whenever logged in.
    * By clicking on the button, editing the form and clicking the "Edit recipe" button.
* I want to log in to delete my own recipes.
    * The "Delete recipe" button is located on each of the user's recipe panel whenever logged in.
    * By clicking on the button, and clicking the Modal's "Confirm" button.
* I want to log in to like and unlike another user's recipe, to connect with the community and to add the recipe on my favourites bookmarked recipes section in my profile page.
    * The "Like" button is located, in the form of a "Heart" icon, on each recipe panel whenever logged in.
    * By clicking on the icon the user can like and unlike the recipe, on each click it will be redirected to the current page.
* I want to log in to access my profile, to see if my recipes have more likes or comments or to go through my favourite recipes for inspiration.
    * The "Profile" page link is available whenever logged in and located in the Navbar or Side menu depending on screen sizes.
    * By clicking on the link, and clicking on either the "Your recipes" panel or the "Your favourite recipes" panel.
* I want to log in to comment on other users recipes, to connect with the community.
    * The "Comment" link is located on each recipe panel and at the top of each recipe page, whenever logged in.
    * By clicking on the icon the user is redirected to that recipe page comments section, where it'll be able leave a comment 
    * The comments section is also accessible by manually going to a recipe page and scrolling to the bottom.
* I want to log in to see a specific recipe comments
    * The "Comment" link is located on each recipe panel and at the top of each recipe page, whenever logged in.
    * By clicking on the icon the user is redirected to that recipe page comments section, where it'll be able to see all comments.
    * The comments section is also accessible by manually going to a recipe page and scrolling to the bottom.
* I want to log in to remove a comment I posted.
    * The "Delete comment" icon is located on the right side of each of the user's comment panel.
* I want to log in to see which recipes are most liked or commented.
    * The "Like" and "Comment" counts are located beside their respective icons.
* I want to log in to see if any users liked my recipes or if any users commented on my recipes and who they were.
    * The "Profile" page link is available whenever logged in and located in the Navbar or Side menu depending on screen sizes.
    * By clicking on the link, and clicking on either the "Your recipes" panel or the "Your favourite recipes" panel.
### Lighthouse
* Passed all tests
* Scores:
    * Performance - 95
    * Accessibility - 71
    * Best Practices - 100
    * SEO - 80
### Browsers
* Mozilla, Chrome, Edge and Safari all display same projected layout and have no issues at any screen sizes.
### Screen sizes
* The website is fully responsive through the Materialize grid system and media queries, starting from a screen size as small as 280px to as large as 1680px.
* All features are available and visible on every screen size. The Navbar becomes a toggled side menu on small screen sizes.
### Bugs discovered
* Upon deploying and testing the application on Iphone, I found that none of the single or multiple options Materialize select elements were responding correctly. When trying to select an element the wrong elements would be selected, this happened every single time. Therefore I decided to replace all single option select elements with the respective "browser default" version, and all multiple option select elements with the Select2 version.  
All elements now work as desired.
* I tried to sort recipes by User likes descending, however, I found that after liking a recipe, pagination would render the wrong recipes, removing some from the page and duplicating others. I tried to find out why with the assistance of a tutor but unfortunately we couldn't fix it. Therefore I decided to display recipes in no particular order which fixed the issue.
* When displaying filtered results, the "recipe name" filter info will display with a colon punctuation ":" prior to the name. I have managed to remove all other unnecessary syntax from the results with the "replace" method, however, I don't seem to be able to target this particular colon.
* When adding a comment, the comment does not immediately show in the comments section below. It will only show once leaving the page and reloading it.
* Fixed Firefox Unordered list aligning issue by adding -moz-fit-content to the width property and -moz-center to the text-align property.
* A few days prior to submitting this projects, upon trying to open the deployed version of the website, the page would throw a "Type Error - None object is not subscriptable". This would only happen if I tried to log in from my laptop, while it worked fine on my phone. I fixed this error by clearing the data on the application storage on the dev tools. Unfortunately, even with the help of a tutor, I wasn't able to find out why this happened.

## Deployment DEPLOYMENT SECTION AS TO INSTRUCT A THIRD PARTY
This project was developed using Gitpod, a [Github repository](https://github.com/francesc-droid/recipe-cookbook) was created and regular commits were pushed to the repository through Git commands.

The project was deployed to [Heroku](https://www.heroku.com/) using the following steps:
* Set environment variables and made sure they were in the gitignore file and not being tracked.
* Created requirements.txt for dependencies and Procfile to tell which file is required to run the app: pip3 freeze --local requirements.txt echo web: python app.py > Procfile. I made sure you remove the blank line from the Procfile as it might cause problems when running the app on Heroku.
* Created new Heroku app from the Heroku website by clicking "Create new app".
* Connected my app from my Github repository by clicking on the Github icon in my app's "Deploy" section, then clicked "Search" and once it found my repo I clicked "connect".
* Before I clicked "Enable automatic deployment" I needed to tell Heroku which hidden environment variables were required (the ones hidden in the env.py file), so I clicked on the "Settings" tab and then on "Reveal config vars" and added all required hidden variables.
* Went back to "Deploy" tab, clicked on "Enable automatic deployment" and then directly below it clicked on "Deploy branch"
Heroku will now receive the code from Github and start building the app using the required packages.
* After a minute or so the message "Your app was successfully deployed" appeared, I then clicked on the "View" button below that message to launch my app.
* The deployed site was now available and automatically updated whenever I pushed changes to the Github repository.
* My deployed website can be found [here](https://recipe-cookbook-fran.herokuapp.com/).

# Credits
## Code
### HTML
* The pattern "regex" on both the mailing list and modals email input was taken from [Geek for geeks](https://www.geeksforgeeks.org/html-dom-input-email-pattern-property/)
### JavaScript
* The Maps JavaScript code was researched through The Google Maps and Places API pages and various Youtube instructional videos
* The "selectItem" function in the script.js file was taken from [Traversy Media](https://www.traversymedia.com/)
* The "clearValue" function was taken from [Traversy Media](https://www.traversymedia.com/)
* The "sendMail" function was taken from [EmailJS](https://www.emailjs.com/docs/) through [Code Institute](https://codeinstitute.net/)


## Content
### Text 
* The Main Page Hero section text and the Tab content items text was sourced at [Tokyo Ramen Tours](https://www.tokyoramentours.com/post/ramen-types-big-4)
* The Regional Ramen pages text wa sourced at [Gurunavi](https://gurunavi.com/en/japanfoodie/2018/02/regional-ramen.html)
### Quiz
* The Quiz questions were partly sourced at [All the tests](https://www.allthetests.com/knowledge-trivia-tests/food-drinks/other-food-drinks/quiz23/1182521396/do-you-know-ramen-noodles)

## Media 
### Video
* The video was sourced at [Pexels](https://www.pexels.com/video/person-using-chopsticks-getting-food-4224218/) - Video by alleksana from Pexels  
### Icons
* The favicon was sourced at <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> 
* The Main and Regional page menu Icon was sourced at <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> 
*  The Map Markers Icon was sourced at <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a>
* The Quiz Home page Icon was sourced at <a href="https://www.freepik.com/vectors/icons">rawpixel.com - www.freepik.com</a>
### Images
* The Images of the Form submission Modals and Quiz results Modals were sourced at <a href='https://www.freepik.com/vectors/food'>Food vector created by catalyststuff - www.freepik.com</a>
* The Main Page Tab content Images were sourced at [Tokyo Ramen Tours](https://www.tokyoramentours.com/post/ramen-types-big-4)
* The Regional Ramen dish images were sourced at [Gurunavi](https://gurunavi.com/en/japanfoodie/2018/02/regional-ramen.html)
