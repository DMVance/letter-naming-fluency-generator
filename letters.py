import string, random
from flask import jsonify


def generate_letters(lines, case):

    lines = int(lines)
    case = case.lower()

    print("letters.py, lines = ", lines)
    print("letters.py, case = ", case)

    if case == "l":
        alphabet = list(string.ascii_lowercase)     # Can this section be collapsed?
    elif case == "u":
        alphabet = list(string.ascii_uppercase)
    elif case == "m":
        alphabet = list(string.ascii_letters)
    
    p = 10
    output_list = []
    for i in range(lines):
        random_letters = random.sample(alphabet, p)
        output_list.append(random_letters)
    
    print("letters.py: ", type(output_list))
    print("letters.py: ", *output_list, sep="\n")

    ##############################################
    # Set up the data for a Plotly table or other plot here. Send this back as JSON, rather than the raw data.
    # var values = [
    #   ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
    #   [1200000, 20000, 80000, 2000, 12120000],
    #   [1300000, 20000, 70000, 2000, 130902000],
    #   [1300000, 20000, 120000, 2000, 131222000],
    #   [1400000, 20000, 90000, 2000, 14102000]]

    output_data = [{
        "type": 'table',
        "header": {
            "values": ["<b>Lines</b>"],   #[ , ["<b>Q1</b>"], ["<b>Q2</b>"], ["<b>Q3</b>"], ["<b>Q4</b>"]],
            "align": "center",
            "line": {"width": 1, "color": "black"},
            "fill": {"color": "grey"},
            "font": {"family": "Arial", "size": 12, "color": "white"}
        },
        "cells": {
            "values": output_list,
            "align": "center",
            "line": {"color": "black", "width": 1},
            "font": {"family": "Arial", "size": 11, "color": ["black"]}
        }
    }]

    # print("letters.py: output_data = ", output_data)

    ##############################################

    # return jsonify(random_letters) # Return a JSON that can be pulled into JS. --> Update: used jsonify() in app.py
    return output_data     #output_list