# --- Flask Hello World --- #

# import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# Use decorators to link the function to an URL
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello World!!"
# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query
"""
# treated as an integer
@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"
# treated as a floating point
@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"
# treated as a path
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"
"""
@app.route("/name/<name>")
# returns name if it is Matilde, if not it is a status code 404, and it will return Not Found
def index(name):
    if name.lower() == "matilde":
        return "Hello {}".format(name)
    else:
        return "Not Found", 404


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
