from chalice import Chalice, Response

app = Chalice(app_name='hello world')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/webhook', methods=['POST', 'PUT'])
def index():
    request = app.current_request
    num1 = int(request.json_body.get("result").get("parameters").get("number"))
    num2 = int(request.json_body.get("result").get("parameters").get("number1"))
    op = request.json_body.get("result").get("parameters").get("operation")
    result = calculation(num1, num2, op)
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
