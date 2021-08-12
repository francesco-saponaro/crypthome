# Crypthome
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
* Cryptocurrencies data tables updated every minute
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

## Credits
### Code
#### HTML
* The pattern "regex" on both the mailing list and modals email input was taken from [Geek for geeks](https://www.geeksforgeeks.org/html-dom-input-email-pattern-property/)
#### JavaScript
* The Maps JavaScript code was researched through The Google Maps and Places API pages and various Youtube instructional videos
* The "selectItem" function in the script.js file was taken from [Traversy Media](https://www.traversymedia.com/)
* The "clearValue" function was taken from [Traversy Media](https://www.traversymedia.com/)
* The "sendMail" function was taken from [EmailJS](https://www.emailjs.com/docs/) through [Code Institute](https://codeinstitute.net/)


### Content
#### Text 
* The Main Page Hero section text and the Tab content items text was sourced at [Tokyo Ramen Tours](https://www.tokyoramentours.com/post/ramen-types-big-4)
* The Regional Ramen pages text wa sourced at [Gurunavi](https://gurunavi.com/en/japanfoodie/2018/02/regional-ramen.html)
#### Quiz
* The Quiz questions were partly sourced at [All the tests](https://www.allthetests.com/knowledge-trivia-tests/food-drinks/other-food-drinks/quiz23/1182521396/do-you-know-ramen-noodles)

### Media 
#### Video
* The video was sourced at [Pexels](https://www.pexels.com/video/person-using-chopsticks-getting-food-4224218/) - Video by alleksana from Pexels  
#### Icons
* The favicon was sourced at <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> 
* The Main and Regional page menu Icon was sourced at <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> 
*  The Map Markers Icon was sourced at <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a>
* The Quiz Home page Icon was sourced at <a href="https://www.freepik.com/vectors/icons">rawpixel.com - www.freepik.com</a>
#### Images
* The Images of the Form submission Modals and Quiz results Modals were sourced at <a href='https://www.freepik.com/vectors/food'>Food vector created by catalyststuff - www.freepik.com</a>
* The Main Page Tab content Images were sourced at [Tokyo Ramen Tours](https://www.tokyoramentours.com/post/ramen-types-big-4)
* The Regional Ramen dish images were sourced at [Gurunavi](https://gurunavi.com/en/japanfoodie/2018/02/regional-ramen.html)
