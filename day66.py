from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch data from an external API (example: JSONPlaceholder)
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()

    # Render data using a simple HTML template
    html_template = """
    <!doctype html>
    <html>
        <head><title>API Data Display</title></head>
        <body>
            <h1>Post from JSONPlaceholder</h1>
            <h2>{{ data['title'] }}</h2>
            <p>{{ data['body'] }}</p>
        </body>
    </html>
    """

    return render_template_string(html_template, data=data)

if __name__ == '__main__':
    app.run(debug=True)
