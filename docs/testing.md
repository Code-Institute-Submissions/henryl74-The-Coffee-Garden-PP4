# Testing  

## Methodology  
Testing was done throughout the process while developing the project by the use of Django debug pages. In addition all code has been validated with different online tools as presented below.

* ## Html Code Validator
    * All the HTML pages code ran through [html code validator](https://validator.w3.org/#validate_by_uri) and there were no issues found.

### Home Page   
![html code validator](./readme-testing-images/html_home_w3c_result.png)

### Menu Page
![html code validator](./readme-testing-images/html_menu_w3c_result.png)

### Reservation Page
![html code validator](./readme-testing-images/html_reservation_w3c_result.png)

### Register Page
![html code validator](./readme-testing-images/html_register_w3c_result.png)

### Login Page
![html code validator](./readme-testing-images/html_login_w3c_result.png)

### Book a Table Page
![html code validator](./readme-testing-images/html_book_a_table_w3c_result.png)

### Booking Confirmation Page
![html code validator](./readme-testing-images/html_booking_confirmation_w3c_result.png)

### My Bookings Page
![html code validator](./readme-testing-images/html_my_bookings__w3c_result.png)

### Log Out Page
![html code validator](./readme-testing-images/html_logout_w3c_result.png)

* ## CSS Code Validator
    * All the CSS code ran through using [css code validator](https://validator.w3.org/#validate_by_input) and there were no issues found.

![css code validator](./readme-testing-images/css_w3c_result.png)

There was however an error, and some warnings issues regarding the use of css variables that it could not validate, this only happened when I validated the code by URI.

![css code validator](./readme-testing-images/font_awesome_error.png)

![css code validator](./readme-testing-images/bootstrap_warnings.png)

![css code validator](./readme-testing-images/font_awesome_warnings.jpeg)

The following warnings messages were fixed for HTML and CSS while validating my code:

* #### HTML

![html code validator](./readme-testing-images/html_warning_fixed.png)

* #### CSS

![css code validator](./readme-testing-images/font_family_warning_fixed.png)


* ## Javascript Code Validator
    * Using [jshint](https://jshint.com/), I ran my jquery/javascript code and found no errors.


* ## Python Validation

    * All Python code was validated using CI Python Linter [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/) and the following indentation errors were found and fixed accordingly.

manage.py

![CI Python Linter](./readme-testing-images/manage_py_fixed.png)

models.py

![CI Python Linter](./readme-testing-images/phone_models_py_fixed.png)

views.py

![CI Python Linter](./readme-testing-images/views_py_fixed.png)

* ## Lighthouse Testing
    * All pages were checked on lighthouse with average results of 88% and 97% for each page on desktop, and an average of 72% and 100% for each page on mobile devices.
    Performance was impacted on a few pages, especially on mobile devices. Similar to the warnings with CSS validation above, the performance issues are related to the third-party library used in my project; I could have compressed further the background images to improve performance, but due to time constraints I couldn't tackle this; I will defefitenely bear this in mind for my next project.

### Home Page

#### **Desktop**

![Home Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_%20home_desktop.png)

#### **Mobile**

![Home Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_%20home_mobile.png)

### Menu Page

#### **Desktop**

![Menu Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_menu_desktop.png)

#### **Mobile**

![Menu Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_menu_mobile.png)

### Reservation Page

#### **Desktop**

![Reservation Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_reservation_desktop.png)

#### **Mobile**

![Reservation Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_reservation_mobile.png)

### Register Page

#### **Desktop**

![Register Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_register_desktop.png)

#### **Mobile**

![Register Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_register_mobile.png)

### Login Page

#### **Desktop**

![Login Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_login_desktop.png)

#### **Mobile**

![Login Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_login_mobile.png)

### Book a Table Page

#### **Desktop**

![Book a Table Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_bookatable_desktop.png)

#### **Mobile**

![Book a Table Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_bookatable_mobile.png)

### Booking Confirmation Page

#### **Desktop**

![Booking Confirmation Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_booking_confirmation_desktop.png)

#### **Mobile**

![Booking Confirmation Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_booking_confirmation_mobile.png)

### My Bookings Page

#### **Desktop**

![My Bookings Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_my_bookings_desktop.png)

#### **Mobile**

![My Bookings Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_my_bookings_mobile.png)

### Log Out Page

#### **Desktop**

![Log Out Page Desktop Lighthoue Validation](./readme-testing-images/lighthouse_log_out_desktop.png)

#### **Mobile**

![Log Out Page Mobile Lighthoue Validation](./readme-testing-images/lighthouse_log_out_mobile.png)

* ## Manual Testing

    * In addition to the other tests, I have conducted a manual check list for myself to carry out to make sure that everything is working as intended.

| Status | **Navigation Bar Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Menu, Reservation, Register, Login
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Menu tab on the navbar loads the menu page
| &check; | Clicking the Reservation tab on the navbar loads the reservation page
| &check; | Clicking the Login tab on the navbar loads the login page

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | That the navbar shows the username of the logged in user
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Menu, Reservation, My Bookings, Logout if the user is logged in
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Reservation tab on the navbar loads the Book a Table page
| &check; | Clicking the My Bookings tab on the navbar loads the user's bookings made page
| &check; | Clicking the Logout tab on the navbar loads the logout page
| &check; | That the Logout button once clicked displays a logout message


| Status | **Navigation Bar - Admin (superuser) User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar Django adminitration logo loads the home page
| &check; | That the navbar displays a welcome message, tabs to View Site, Change Password, Log Out
| &check; | That the navbar shows the username of the logged in user
| &check; | Clicking the Accounts tab on the admin panel loads the Email addresses
| &check; | Clicking the Email Addresses tab, it will load the user emails registered
| &check; | Clicking the Restaurant tab on the admin panel loads the bookings tab
| &check; | Clicking the Booking tab, it will list all the existing reservations that have been made
| &check; | Clicking the Add Booking, allows the admin user to add a booking to an specific user
| &check; | Clicking on an existing Booking, allows the admin user to delete or update that reservation

| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | That the Footer displays the Opening Hours, Contact Details, and Social Media icons
| &check; | Clicking the Facebook icon loads the instagram home page in a new tab
| &check; | Clicking the Instagram icon loads the facebook home page in a new tab
| &check; | Clicking the TikTok icon loads the twitter home page in a new tab