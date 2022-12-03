# Testing  

## Methodology  
Testing was done throughout the process while developing the project by the use of Django debug pages. In addition all code has been validated with different online tools as presented below.

* ### Html Code Validator
    * All the HTML pages code ran through [html code validator](https://validator.w3.org/#validate_by_uri) and there were no issues found.
        
![html code validator](./readme-testing-images/html_w3c_result.png)

* ### CSS Code Validator
    * All the CSS code ran through using [css code validator](https://validator.w3.org/#validate_by_input) and there were no issues found.

![css code validator](./readme-testing-images/css_w3c_result.png)

There was however an error, and some warnings issues regarding the use of css variables that it could not validate, this only happened when I validated the code by URI.

![css code validator](./readme-testing-images/font_awesome_error.png)

![css code validator](./readme-testing-images/bootstrap_warnings.png)

![css code validator](./readme-testing-images/font_awesome_warnings.jpeg)

The following warnings messages were fixed for html and css while validating my code:

* #### HTML

![html code validator](./readme-testing-images/html_warning_fixed.png)

* #### CSS

![css code validator](./readme-testing-images/font_family_warning_fixed.png)


* ### Javascript Code Validator
    * Using [jshint](https://jshint.com/), I ran my jquery/javascript code and found no errors.


* ### Python Validation

    * All Python code was validated using CI Python Linter [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/) and the following indentation errors were found and fixed accordingly.

manage.py

![CI Python Linter](./readme-testing-images/manage_py_fixed.png)

models.py

![CI Python Linter](./readme-testing-images/phone_models_py_fixed.png)

views.py

![CI Python Linter](./readme-testing-images/views_py_fixed.png)

* ### Lighthouse Testing
    * All pages were checked on lighthouse with the results between % and % for each page on mobile and desktop.