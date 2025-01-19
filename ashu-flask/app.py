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
    my_output = None
    if request.method == 'POST':  # Handle form submission
        user_input = request.form.get('user_input')  # Get the text from the textarea
        if user_input == "api":
            try:
                data = "https://randomuser.me/api/"  # Fixing the API URL
                x1 = requests.get(data)
                output = x1.json()
                b = output["results"]

                c = b[0]
                gender = c["gender"]
                title = c["name"]["title"]
                first = c["name"]["first"]
                last = c["name"]["last"]
                date = c["dob"]["date"]
                age = c["dob"]["age"]

                fullname = f"{gender} {title} {first} {last} {date} {age}"

                country = c["location"]["country"]
                state = c["location"]["state"]
                city = c["location"]["city"]
                postcode = c["location"]["postcode"]

                post = f"{country} {state} {city} {postcode}"

                username = c["login"]["username"]
                password = c["login"]["password"]
                email = c["email"]

                user_id = f"{username} {password} {email}"

                my_output = f"{fullname}\n{post}\n{user_id}"
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


if __name__ == '__main__': 
    app.run(debug=True,port=5015)
