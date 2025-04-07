'''
This is file contains all the website's auth routes.


'''

# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template

# Create the blueprint views
auth = Blueprint('auth',__name__)


# Create signup route
@auth.route('/signup')
def signup():
  '''
  Create a route for the signup page

  GET method:
    display sign up page

  POST method:
    send necessary fields needed to sign up (name, username, email, password)

  Return:
    valid = 0 if user not in database
      sign up new user
      redirects to home page
    valid = 1 if user is in database but incorrect password
      flash incorrect password
    valid = 2 if correct user an correct password
      login user
      redirects to home page
  '''
  return render_template("auth/signup.html")

# Create login route
@auth.route('/login')
def login():
  '''
  Create a route for the login page

  GET method:
    display login page

  POST method:
    send necessary fields needed to login (username & password)

  Return:
    valid = 0 if user not in database
      flash incorrect user
    valid = 1 if user is in database but incorrect password
      flash incorrect password
    valid = 2 if correct user an correct password
      login user
      redirects to home page
  '''
  return render_template("auth/login.html")

# Create logout route
@auth.route('/logout')
def logout():
  '''
  Create a route for logging out

  Return:
    flash logout message
    redirect to login page
  '''
  return render_template("standard/home.html")