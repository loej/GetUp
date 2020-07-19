from flask import Flask
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

# Main function.
if __name__ == "__main__":
    app.run()