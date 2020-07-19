from flask import Flask, redirect, url_for
# redirect and url_for allow the user to immediatley get redirected from a different url

# Imports Flask instance 
app = Flask(__name__)

# Defines how to access specific page 
# This is the route: the default domain.
@app.route('/')
def mainPage():
    return '<h1>Get Up</h1>'

# This is a new page that accepts any input inside the brackets
# Out puts what the function recieves from the parameter in the URL. 
@app.route('/<name>')
def userInterface(name):
    return f'Hello {name}'

# GetUp route where the user selects the time. 
@app.route('/getup')
def getUpPage():
    return f'<h1> Welcome to Get Up! </h1>'
    
# Redirecting user to new page:
# Is a user tries to access the /admin page it will redirect them to 
# /getup
def admin():
    # A redirect simply redirects the user to a new screen. 
    return redirect(url_for('getUpPage'))


# Main function.
if __name__ == "__main__":
    app.run()