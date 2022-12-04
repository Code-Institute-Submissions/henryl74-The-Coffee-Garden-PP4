# Project Portfolio 4 Full Stack Frameworks - The Coffee Garden

The Coffee Garden project portfolio has been created for educational purposes only as the 4th project in the Code Institute’s full stack development program.

Using the principles of UX design and the agile development methodology, this project was developed using HTML, CSS, JavaScript, Python and the Django framework.

## Live Site

You can view the live deployed game here: <a href="https://the-coffee-garden.herokuapp.com/" target="_blank"> The Coffee Garden </a>

![The Coffee Garden](./docs/readme-testing-images/live_site.jpeg)

# Contents

* [Objective](<#objective>)
* [User Experience](<#user-experience-ux>)
* [Agile Methodology](#agile-methodology)
* [User Stories](#user-stories)
* [Design](#design)
* [Database Schema](#database-schema)
* [The Coffe Garden Flow Chart](<#the-coffee-garden-flow-chart>)
* [Features](#features)
* [Future Features](<#future-features>)
* [Technologies Used](#technologies-used)
* [Testing](<#testing>)
  * [Bugs Fixed](#bugs-fixed)
* [Deployment](#deployment)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# Objective

The Coffee Garden is a small restaurant that lacks an online presence and would like to increase the engagement with its customers and potential customers through an online platform. As such they have identified the following areas of opportunity:

   * Create an online presence
   * Interact with current/potential customers
   * Create an online reservation system
   * Display key information
   * Create marketing opportunities through the social media links displayed in the site

[Back to top](<#contents>)

# User Experience (UX)

-   ### Site Aims  
  The overall goal of this project is to create a restaurant webpage that is visually nice and easy to navigate to the user. Visitors should be able to find general information about the restaurant in the home page, as well as finding the menu offerings. In addition, visitors should be able to make a reservation for a table directly on the webpage. It will also provide a booking management admin panel for the restaurant owner.

## Agile Methodology

The principles of agile methodology were utilized during the project. By assigning user stories to issues and taking advantage of the GitHub Kanban board functionality, the necessary goals and priorities throughout the project could be well defined. In addition, labels were used to further define the priority of eacn user story in the Kanban board.

[Back to top](<#contents>)

## User Stories

  -   #### First Time Visitor Goals
        - As a first time visitor, the user can read and learn about the restaurant, it's location, social media involment and get a feel for this place.
        - As a first time visitor, the user can find out what kind of food they serve from their menu.
        - As a first time visitor, the user can find information about how to make a reservation at the restaurant.
        
  -   #### Returning Visitor Goals
        -  As a returning visitor, the user can create an account so I can make an online reservation.
        -  As a returning visitor, the user can login and find my current bookings.
        -  As a returning visitor, the user can update or cancel a booking once they login to the site.
        -  As a returning visitor, the user can check the menu to see if has changed.

-    #### Admin Stories
        - As a site admin I could add, update, cancel existing boookings made in my website.
        - As a site admin I could add, update, delete users registered on my website.
        - As a site admin I could check all the accounts registered on my website.

[Back to top](<#contents>)

## Design

The theme for the project were chosen in accordance with the intended target market in mind for the restaurant. It primarely focus on attracting families, young crows, local residents, and visitors to this region.
    
- Colors  
The main colors are overall cream-pastel, it blends well with the main product that this restaurant has to offer; the best coffe in town.
- Font  
The fonts in the theme are clear and modern and contribute perfectly to the overall look of the site.  
- Images  
The images in the theme provide great content to the site; as the user navegates through the pages; reasures him/her the type of products are being served here.

[Back to top](<#contents>)

# Database Schema
- The database design schema can be viewed below. It consists of a Booking model with a foreignKey of User that relates to the Django standard User model class.  

![dbschema]()

[Back to top](<#contents>)

# The Coffe Garden Flow Chart

![The Coffe Garden Flow Chart](./docs/readme-testing-images/the_coffee_garden_flowchart.jpeg)

[Back to top](<#contents>)

# Features

My project consists of nine webpages:

- Home or landing page.
- Menu page.
- Reservation page.
- Register page.
- Login page.
- Book a Table (Reservation Page).
- Booking confirmation page.
- My Bookings page.
- Logout page.

### The Navigation Bar

- The navigation bar shows all the sections that the user can enter and provides a quick and easy means of navigating the site.
- The navigation bar bar is very responsive and user friendly, it has an additional hover effect to help the user with his/her selection.
- The restaurant logo located on the the left hand corner of the navigation bar, helps the user to go back to the home page by clicking on it.

![Navbar](./docs/readme-testing-images/navigation_bar.jpeg)

### Home or landing page

- The home section makes the first impression of the site to the visitor. The main background image gives a primary idea to the user of what products are sold here, and how they are prepared; it also displays the main contact details of the restaurant located at the bottom of the page as footer.

![Navbar](./docs/readme-testing-images/home_page.jpeg)

### Menu page

- The menu section comes with images and descriptions of a few different options available at this restaurant, it also displays the main contact details of the restaurant located at the bottom of the page as footer.

![Menu](./docs/readme-testing-images/menu_page.jpeg)

### Reservation Page

- On the booking page the customer it's prompted to login to continue with the online booking.

![Reservations](./docs/readme-testing-images/reservation_page.jpeg)

#### Register page

- In this section, the user can create an account to make a registration as well as click on the log-in link to be able to access the site as a new or existing user.  

![Register](./docs/readme-testing-images/register_page.jpeg)

### Login page

- The user can access the site as a registered user to proceed with his/her online booking.  

![Login](./docs/readme-testing-images/login_page.jpeg)

#### Book a Table (Reservation Page)

- In this section, the user can proceed with his/her to book a table, provide his/her name, contact details, number of people, time, and date for the reservation.

![Book a Table](./docs/readme-testing-images/book_a_table_page.jpeg)

### Booking confirmation page

- This section displays a thank you booking confirmation message, it gives the user the option to either perform updates to the booking that just has been made or view the menu again through the links provided within the message.

![Booking Confirmation](./docs/readme-testing-images/booking_confirmation_page.jpeg)

### My Bookings page

- The current bookings for a customer are shown on the mybooking page, that way the customer can get an overview of all bookings and check the date and time, etc for each booking. On this page, the customer can also click on the "Update" button and make necessary changes to the booking that will be saved and shown on the mybooking page. The customer can also delete a booking by clicking on the "Cancel" button. It will then disappear from the list of reservations.

![My Bookings](./docs/readme-testing-images/my_bookings_page.jpeg)

### Logout page

- Here the user can end his online session, this section also displays a message asking the customer if he wants to proceed with this action.

![Logout](./docs/readme-testing-images/logout_page.jpeg)

[Back to top](<#contents>)

## Future Features

Due to time constraints, the following features will be considered for future implementation on a separate project:

- Blog
- Gallery
- Recipe videos 
- Newsletter Sign up

[Back to top](<#contents>)

* # Technologies Used

    * ## Languages Used
        * [HTML](https://www.w3schools.com/html/)
        * [CSS](https://www.w3schools.com/css/)
        * [Javascript](https://en.wikipedia.org/wiki/JavaScript)
        * [Python](https://www.python.org/)

    * ## Libraries/Framework Used
        * [Django](https://www.djangoproject.com/)
        * [Bootstrap](https://getbootstrap.com/)
        * [jQuery](https://jquery.com/)

    * ### Libraries/Module Installed
        * asgiref==3.5.2
        * cloudinary==1.30.0
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2.16
        * django-allauth==0.51.0
        * gunicorn==20.1.0
        * oauthlib==3.2.2
        * psycopg2==2.9.5
        * PyJWT==2.6.0
        * python3-openid==3.2.0
        * pytz==2022.6
        * requests-oauthlib==1.3.1
        * sqlparse==0.4.3

    * ## Other Technologies
        * [Postgres Database](https://www.postgresql.org/)
        * [W3School](https://www.w3schools.com/)
        * [Stackoverflow](https://stackoverflow.com/)
        * [Git](https://git-scm.com/)
        * [Github](https://github.com/)
        * [Gitpod workspace](https://gitpod.io/workspaces)
        * [Heroku](https://dashboard.heroku.com/apps)
        * [Flowchart](https://lucid.app/documents#/documents?folder_id=home)
        * [jshint](https://jshint.com/)
        * [HTML code validator](https://validator.w3.org/)
        * [CSS code validator](https://jigsaw.w3.org/css-validator/)
        * [Font Awsome](https://fontawesome.com/)
        * [Google Fonts](https://fonts.google.com/)
        * [Slack](https://slack.com/intl/en-gb/)

[Back to top](<#contents>)

# Testing

I have included testing details in a separate document called [Testing.md](./docs/testing.md)

[Back to top](<#contents>)

## Bugs Fixed

- Register page for laptops had a css issue with the container, I fixed it by removing the width, margin-left, and added margin: 0 7% within the css file.

![Register Page Bug](./docs/readme-testing-images/register_bug.jpeg)

- Menu, the images were not displaying, I fixed it by changing the path to absolute on each image in the html file.

![Menu Page Bug](./docs/readme-testing-images/menu_images_bug.jpeg)

- Home Page rendiring error, I fixed it by udating the path under urls.py

![Home Page Bug](./docs/readme-testing-images/home_error_template.jpeg)

- Update Booking rendiring error, I fixed it by udating the path under urls.py

![Update Booking Bug](./docs/readme-testing-images/edit_booking.jpeg)

- Nav bar brightness issue, this was down to a bootstrap issue, I fixed it by substituting the span for a fontawesome icon instead.

![Nav bar brightness](./docs/readme-testing-images/nav_bar_brightness.jpeg)

![Nav bar brightness](./docs/readme-testing-images/font_awesome_fix.jpeg)

[Back to top](<#contents>)

## Deployment

Git and GitHub are used for version control. Python is the backend language, and can't be displayed with GitHub alone, To live preview my project, I used Heroku.

## Deployment to Heroku

### 1. Creating the Django Project
* If development if being done locally: Activate your virtual environment
* To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
* Install Django and gunicorn: `pip install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`

### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres' / Now replaced by 'ElephantSQL'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py

* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku  add cloudinary url to 'config vars'
* In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: ```ALLOWED_HOSTS =
['rhi-book-nook.herokuapp.com', 'localhost']```
*Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Make an initial (if this has not been done previously) commit and push the code to the GitHub Repository.
    ```git add .```
    ```git commit -m "Initial deployment"```
    ```git push```

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku
* In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
* In the 'search' box enter the Github repository name for the project
* Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

### 6. Final Deployment
In the IDE: 
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

[Back to top](<#contents>)

## Credits

- [Code Institute walkthrough](https://codeinstitute.net/) as inspiration and code examples, the code institute walkthroughs "Hello Django" and "I Think Therefore I Blog" was used.

- [Django Documenation](https://www.djangoproject.com/) was used to provide examples of code solutions and Django functionality.

- [Bootstrap Documenation](https://getbootstrap.com/) was used to provide examples of Bootstrap functionality and building blocks.

- [Django YouTube Tutorial on how to create a Blog](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)

- [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4)

- [Python Django 7 Hour Course](https://www.youtube.com/watch?v=PtQiiknWUcI)

- [Stackoverflow](https://stackoverflow.com/)

- [Slack](https://slack.com/intl/en-gb/) community support.

- Code Institute - Tutor Assistance, big thank you for all your support, suggestions and help!


[Back to top](<#contents>)

## Acknowledgements

- Again, the online tutors for all their help.
- The Code Institute slack community.
- All my classmates for constantly sharing new ideas in our dedicated slack channel.
- Stack Overflow question and answer website.
- My mentor Chris Quinn, big thank you for all your all your amazing guidance given, I learned a lot throughout our sessions.
- My family, THANK YOU for being part of the team.
- Last but not least Code Institute student support team, for being there for us.

[Back to top](<#contents>)


