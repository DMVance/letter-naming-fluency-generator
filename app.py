import json, requests
from flask import Flask, jsonify, render_template, request, make_response

from letters import generate_letters

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Transfer data between python and JS
@app.route("/test", methods=["POST", "GET"])
def testfn():
    print("Running test in app.py")

    user_data = request.get_json()
    #user_data = request.form  #.get_json() # was working, now getting None type. The data is not making it from JS to "/test".
    print(user_data)
    print(type(user_data))

    lines, case = user_data
    print(lines)
    print(case)

    output = generate_letters(lines, case)
    print("Output = ", output)

    # response = json.dumps(output)  # This was part of the problem!! response is not json serializable!
    return output

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)