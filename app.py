from flask import Flask, jsonify, render_template, request, make_response
from letters import generate_letters

app = Flask(__name__)

@app.route("/")
def index():
    output = generate_letters()
    # return render_template("letter_generator.html")
    return render_template("parent.html", output=output)

# @app.route("/places")
# def places():
#     return render_template("places.html")

if __name__ == "__main__":
    app.run(debug=True)