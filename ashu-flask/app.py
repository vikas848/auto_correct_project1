from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Route for Login Page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Example: Hardcoded credentials
        if username == 'Vikas Singh' and email=='6391782926vs@gmail.com' and password == '9569':
            return redirect(url_for('home'))
        else:
            error = "Invalid username or password"
            return render_template('index.html', error=error)

    return render_template('index.html')  # Render login page for GET request


# Route for the Home Page
@app.route('/home', methods=['GET', 'POST'])
def home():
    #user_input = None
    output = None
    if request.method == 'POST':  # Handle form submission
        user_input = request.form.get('user_input')  # Get the text from the textarea
        data="https://randomuser.me/"+user_input
        x1=requests.get(data)
        output=x1.json()
    return render_template('home.html', user_input=output)


if __name__ == '__main__':
    app.run(debug=True,port=5009)
