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

## Automated Python testing
* I had great trouble testing for views that require authentication. I am afraid I haven't been able to research or practice the TestCase class, however I kept all tests that passed and the rest will be tested manually nonetheless.
![Automated Pythone tests](/testing-screenshots/automated-python-tests.png) 

## Client stories testing
The website flow is designed so that every page available to the user is accessible through the Navbar or slider menu, which interchange depending on screen size. The "Register" and "Log in" links interchange with the "Profile" and "Log out" links depending on if the user is logged in or not.  
Defensive programming was implemented to:
* Make sure logged in or logged out users are not able to access other user`s accounts and pages by pasting their URL. On trying to do so they will be redirected to the Home page.
* Make sure users dont log in without authentication by pasting the right URL. On trying to do so they will be redirected to the Home page.
* In the case of a 404 or 500 error the user will be redirected to a page informing him of the error and with a link to go back to the Home page.
### As a user i want:
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
* I had great trouble deploying Celery, hence the many repeated commit messages towards the end of the projcts. However after plenty of research I managed to deploy it successfully.
* Upon changing a model field of the Position model in home.models and running the "makemigrations" command, I have been unable to either migrate or access the model in Admin, and kept getting an OperationalError. Somehow the field changed but there was a model instance in the database with the old field, therefore giving an error.   
After many attempts to fix it I had to delete both my Sqlite3 and PostgreSQL databases, reinstall them, rerun migrations and load the data again. This fixed the issue.
* On the coins_desc variable of the home.views, unfortunately I couldn't use a single regex to remove all anchor tags of the text coming from the API. For each tag I had to copy exaxt matched string to replace.  
I have taken this regex from stack overflow '("<(?:a\b[^>]*>|/a>)", "")' but was not working. Even the tutors were not able to find the issue as the regex are valid and were tested with a regex validator.
* Upon testing the "fail authentication" payment scenario with stripe, I get the "Devtools failed to load source map" warning, however it doesn't affect the code.