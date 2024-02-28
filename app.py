from flask import Flask, redirect, url_for, render_template, make_response, request, flash,session,jsonify
from constant import LOGINPAGE



app = Flask(__name__)


@app.route('/login')
def login():
    # Your login logic here
    return "This is the login page"



@app.route('/')
def index():
    html_content = render_template(LOGINPAGE)
    response = make_response(html_content)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, no-store'
    return response

if __name__ == "__main__":    
    app.run(debug=True, port=5008)