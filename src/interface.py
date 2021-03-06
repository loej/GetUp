import time
from flask import Flask, redirect, url_for, render_template, request
# redirect and url_for allow the user to immediatley get redirected from a different url
# render_template allows to render an html file

# Imports Flask instance
app = Flask(__name__)

# Defines how to access scpecific page
# This is the route: the default domain.


@app.route('/')
def mainPage():
    return redirect(url_for('getUpPage'))

# GetUp route where the user selects the time.


@app.route('/GetUp')
def getUpPage():
    # Renders file inside template/index.html
    return render_template('basic.html')

# This is a new page that accepts any input inside the brackets
# Out puts what the function recieves from the parameter in the URL.


@app.route('/<name>')
def userInterface(name):
    return f'This page is for {name}s only.'

# Redirecting user to new page:
# Is a user tries to access the /admin page it will redirect them to
# /getup

@app.route('/admin')
def admin():
    # A redirect simply redirects the user to a new screen.
    # name=' ' allows to pass the admin NAME to print the function userInterface()
    return redirect(url_for('userInterface', name='admin'))

# Main function.
if __name__ == "__main__":
    app.run(debug=True)
