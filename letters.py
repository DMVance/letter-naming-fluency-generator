import string, random
# import pandas as pd
# import plotly
# import plotly.express as px
# import plotly.graph_objects as go
# import os, csv, requests, json, datetime
# import numpy as np
# from datetime import date
from flask import Flask, jsonify, render_template, request, make_response
# import re
# from config import mapbox_token
# from flask_sqlalchemy import SQLAlchemy
# from sklearn.feature_extraction.text import CountVectorizer
# import nltk
# from nltk.corpus import stopwords

# app = Flask(__name__)

# @app.route("/places")
def letters():

    lowercase_alphabet = list(string.ascii_lowercase)
    uppercase_alphabet = list(string.ascii_uppercase)
    upper_lower_mix_alphabet = list(string.ascii_letters)

    n = 26
    m = 52

    random_lowercase = random.sample(lowercase_alphabet, n)
    random_uppercase = random.sample(uppercase_alphabet, n)
    random_mix = random.sample(upper_lower_mix_alphabet, m)

    test = random_lowercase[:5]

    print(', '.join(random_lowercase[:5]))
    # print(', '.join(random_lowercase[5:10]))
    # print(', '.join(random_lowercase[10:15]))
    # print(', '.join(random_lowercase[15:20]))
    # print(', '.join(random_lowercase[20:26]))
    # print("\n")
    # print(', '.join(random_uppercase[:5]))
    # print(', '.join(random_uppercase[5:10]))
    # print(', '.join(random_uppercase[10:15]))
    # print(', '.join(random_uppercase[15:20]))
    # print(', '.join(random_uppercase[20:26]))
    # print("\n")
    # print(', '.join(random_mix[:5]))
    # print(', '.join(random_mix[5:10]))
    # print(', '.join(random_mix[10:15]))
    # print(', '.join(random_mix[15:20]))
    # print(', '.join(random_mix[20:25]))
    # print(', '.join(random_mix[25:30]))
    # print(', '.join(random_mix[30:35]))
    # print(', '.join(random_mix[35:40]))
    # print(', '.join(random_mix[40:45]))
    # print(', '.join(random_mix[45:52]))

    return test


#######################################################################################

# letters()

#######################################################################################

# @app.route("/")
# def home():
#     output = letters()
#     return render_template("letter_generator.html", output=output)

# if __name__ == "__main__":
#     app.run(debug=True)