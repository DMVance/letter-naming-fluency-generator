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
    print("app.py: Running test in app.py")

    user_data = request.get_json()
    #user_data = request.form  #.get_json() # Was working, then got None type. The data was not making it from JS to "/test".
    print("app.py: ", user_data)
    print("app.py: ", type(user_data))

    lines, case = user_data
    print("app.py, Unpacked lines: ", lines)
    print("app.py, Unpacked case: ", case)

    output_raw = generate_letters(lines, case)
    print("app.py Output_raw type: ", type(output_raw))
    print("app.py, Output_raw = ", output_raw)

    output = jsonify(output_raw)
    print("app.py Output type: ", type(output))
    print("app.py, Output = ", output)
    # response = json.dumps(output)  # This was part of the problem!! Response is not json-serializable! Must have messed with this and broken the process that was working before.
    
    return output

if __name__ == "__main__":
    app.run(debug=True)