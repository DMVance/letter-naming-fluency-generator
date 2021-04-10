from flask import Flask, jsonify, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    # fig = russ_map()
    return render_template("letter_generator.html")

# @app.route("/places")
# def places():
#     return render_template("places.html")

if __name__ == "__main__":
    app.run(debug=True)