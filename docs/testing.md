# Testing  

## Methodology  
Testing was done throughout the process while developing the project by the use of Django debug pages. In addition all code has been validated with different online tools as presented below.

* ## Html Code Validator
    * All the HTML pages code ran through [html code validator](https://validator.w3.org/#validate_by_uri) and there were no issues found.
        
![html code validator](./readme-testing-images/html_w3c_result.png)

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