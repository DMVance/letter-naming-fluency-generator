from flask import Flask, jsonify, render_template, request, make_response

# from letters import generate_letters

app = Flask(__name__)

@app.route("/")
def index():
    # output = generate_letters()
    return render_template("parent.html") # , output=output)

# Try this to transfer data to and from python and JS
@app.route('/test', methods=['GET', 'POST'])
def testfn():

    # GET request
    if request.method == 'GET':  
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

if __name__ == "__main__":
    app.run(debug=True)