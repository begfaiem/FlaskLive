from flask import Flask, request,render_template

"""
Explanation:
from flask import Flask, request: Import the Flask class and the request object from the Flask library. 
Flask is used to create the web application, and request is used to handle HTTP requests.
render_template is used to render HTML templates.
"""

app = Flask(__name__)
"""
app = Flask(__name__): Create an instance of the Flask class named app. 
The __name__ argument is a special variable in Python that represents the name of the current module.
"""
# Route

@app.route("/", methods=['GET', 'POST'])

#Decorate the home_page function with the route decorator. 
#This function will be called when the client accesses the root ("/") endpoint 
#using either the GET or POST methods

def home_page():
    return render_template("index.html")

#Define the home_page function. When the root endpoint is accessed, it returns the string "Hello World".
#The function returns the rendered template "index.html".

@app.route('/aboutus')

#Decorate the aboutus function with the route decorator. 
#This function will be called when the client accesses the "/aboutus" endpoint using the default GET method.

def aboutus():
    return "we are ineuron"

@app.route('/demo', methods=['POST'])

#his line uses the @app.route decorator to define a route for the "/demo" URL endpoint. 
#The methods=['POST'] argument specifies that this route should only respond to HTTP POST requests.

def operation():

    #This line defines a function named operation. 
    #This function will be executed when a client accesses the "/demo" endpoint using the POST method.

    if request.method == 'POST': #Check if the request method is POST
        operation = request.form['operation'] #
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if operation == "add":
            result = num1 + num2

        elif operation == "multiply":
            result = num1 * num2

        elif operation == "division":
            result = num1 / num2

        else:
            result = num1 - num2

        return render_template("result.html",result=result)
        
        #render_template: rendering HTML templates
        #"result.html": This is the name of the HTML template file that Flask will look for in the templates folder. 
        #In this case, it's "result.html". Flask typically expects templates to be in a folder named "templates" in the same directory as your main script.
        #result=result: This is a keyword argument passed to the template. It associates the variable result (calculated in the previous part of the code) with the name result in the template. 
        #This means that within the HTML template, you can refer to the result using the result variable.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
