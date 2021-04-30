from flask import Flask, jsonify, render_template, request, make_response

from letters import generate_letters

app = Flask(__name__)

@app.route("/")
def index():
    # letters_output = generate_letters()
    return render_template("index.html") #, output=letters_output)

# Try this to transfer data to and from python and JS
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    print("Running test in app.py")

    # GET request
    if request.method == 'GET':  
        message = {'greeting':'Hello from app.py Flask!'}
        return jsonify(message)  # serialize and use JSON headers

    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss at app.py', 200

    user_data = request.get_json()
    print(user_data)

    lines, case = user_data

    output = generate_letters(lines, case)

    response = json.dumps(output)
    return response

# @app.route('/test', methods=['GET', 'POST'])
# def testfn():
#     print("Running test in app.py")
#     user_lines = request.get_json()
#     print(user_lines)

#     response = json.dumps(user_lines)
#     return response


if __name__ == "__main__":
    app.run(debug=True)