import string, random
from flask import jsonify


def generate_letters(lines, case):

    lines = int(lines)
    case = case.lower()

    print("From letters.py, lines = ", lines)
    print("From letters.py, case = ", case)

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
    
    print(output_list)

    return jsonify(random_letters) # Return a JSON that can be pulled into JS.