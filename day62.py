#Create a simple web server using Flask 
from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return 'Hello, World! Welcome to my Flask server.'

# Another example route
@app.route('/about')
def about():
    return 'This is a simple Flask web server.'

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
