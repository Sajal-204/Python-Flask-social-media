
# prequest : Basic Flask , Routes, Rendering templates and static file , block content uses , url_for 
## Level : Up_basic to MEDIUM( intermidiate)




# FLASK

## what to follow while doing backend for social media app

### step are:
### step 1 : install flask_wtf
### step 2 : Import required things
        ``` bash  
        class Login_form(Flaskform):
            from flask_wtf import FlaskForm 
            from wtfforms import stringfield , booleanfield , submitfield
            from wtfforms.validators import Datarequired , Length , Email , Equal-to 
        ```
### step 3 : make form using wtforms 
    ``` bash
    email = StringFiled("Email", validators=[Email()])
    password = StringFiled("Password", validators=[DataRequired(),Lenght(min=8,max=20)])
    confirm_password = StringField(" Confirm Password" ,
                                         validators=[ DataRequired(),Equal-to(" Password ")])
    submit = SubmitField("Submit")
    ```
### step 4 : setup secret key 
    ``` bash
    app.config["SECRET_KEY"] = " your key here " 
    ```

### step 5 : add CRSF prevention in html file in jinja template
    ``` bash
    {{ form.hidden_tag() }}
    ```
### step 6 : make sure your validations works 
    ``` bash
    form.validate_on_submit() 
    ```
    #### It checks two things at once:

    Was the request a POST? (meaning the form was submitted)

    Did the form pass all validators? (including CSRF token validation, required fields, etc.)