from chalice import Chalice
import pyrebase

config = {
    "apiKey": "AIzaSyDpTe7Ijr0iHmW6n26c71kQaGkYBY6ZiRk",
    "authDomain": "imanager-ai.firebaseapp.com",
    "databaseURL": "https://imanager-ai.firebaseio.com",
    "projectId": "imanager-ai",
    "storageBucket": "imanager-ai.appspot.com",
    "messagingSenderId": "255523144424"
}

firebase = pyrebase.initialize_app(config)

app = Chalice(app_name='calculator')


@app.route('/webhook', methods=['POST', 'PUT'])
def index():
    req = app.current_request
    print("req: ", req)
    num1 = int(req.json_body.get("result").get("parameters").get("number"))
    num2 = int(req.json_body.get("result").get("parameters").get("number1"))
    op = req.json_body.get("result").get("parameters").get("operation")
    result = calculation(num1, num2, op)
    print("result: ", result)
    db = firebase.database()
    data = {"name": "Mortimer 'Morty' Smith"}
    db.child("users").push(data)
    return {
        'speech': result
    }


def calculation(num1, num2, op):
    if(op == "sub"):
        return num1 - num2
    elif(op == "add"):
        return num1 + num2
    elif(op == "multiply"):
        return num1 * num2
    elif(op == "divide"):
        return num1 / num2

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
