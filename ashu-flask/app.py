from flask import Flask, render_template, request, redirect, url_for, session
import requests
from openai import OpenAI 

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session security

# calling apikey as credentials
myapi_key = "(use api key)"  # <------------------------------------------------------------
gptclient = OpenAI(api_key=myapi_key)
# Route for Login Page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Example: Hardcoded credentials
        if username == 'Vikas Singh' and email == '6391782926vs@gmail.com' and password == '9569':
            session['user'] = username  # Store username in session
            return redirect(url_for('home'))
        else:
            error = "Invalid username or password"
            return render_template('index.html', error=error)

    return render_template('index.html')  # Render login page for GET request

# Route for the Home Page
@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:  # Check if user is logged in
        return redirect(url_for('index'))  # Redirect to login page if not logged in

    my_output = None
    if request.method == 'POST':  # Handle form submission
        user_input = request.form.get('user_input')  # Get the text from the textarea
        if user_input :
            try:
                completion = gptclient.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant. you need to correct the gramitcal and spelling mistakes given by user"},
                            {"role": "system", "content": "You strictly say to to any other thing apart from correcting the statement."},
                            {"role": "user", "content": "tell me about java and python language"},
                            {"role": "assistant", "content": "sorry i can't provide any info apart form setence correction"},
                            {"role": "user", "content": "what is water supply?"},
                            {"role": "assistant", "content": "sorry i can't provide any info apart form setence correction"},
                            {
                                "role": "user",
                                "content": user_input
                            }
                        ]
                    )
                my_output=completion.choices[0].message.content
                
            except Exception as e:
                my_output = f"An error occurred: {str(e)}"

            return render_template('home.html', user_input=my_output)

        elif user_input == "":
            my_output = "Please submit input."
            return render_template('home.html', user_input=my_output)

        else:
            my_output = "Only 'api' can be entered in the input."
            return render_template('home.html', user_input=my_output)

    # Render the page for GET requests or if no valid response is returned.
    return render_template('home.html', user_input=my_output)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user from session
    return redirect(url_for('index'))

if __name__ == '__main__': 
    app.run(debug=True, port=5016)
