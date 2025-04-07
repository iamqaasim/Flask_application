'''
This is file contains all the website standard routes.
'''

# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template

# Create the blueprint views
views = Blueprint('views',__name__)


# Create Home route
@views.route('/')
def home():
  '''
  Create a route for the Home page

  Functionality:
    home page of the website will be displayed when the user visits the website
    
  Return:
    home.html
  '''
  return render_template("standard/home.html")