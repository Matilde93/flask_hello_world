# --- Flask Hello World --- #

# import the Flask class from the flask package
from flask import Flask

# Create the application objekt
app = Flask(__name__)


# Use decorators to link the function to an URL
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello World!"


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
