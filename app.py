# Step 1 - To import FLASK
from flask import Flask, request, render_template

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)


###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality


@app.route('/', methods=['GET', 'POST'])
def search_fun():
    if request.method == 'POST':
        return "Welcome to the search page using POST Req"
    else:
        return render_template('search.html', results = [])


@app.route('/add', methods=['POST', 'GET'])

def regex_fun():
    import re
    regular_expression_string = request.form.get('var_1')
    test_string = request.form.get('var_2')
    result = re.findall(regular_expression_string,test_string)
    return render_template('search.html',results = result)

###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)