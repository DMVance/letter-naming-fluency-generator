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
    print("letters.py: ", output_list)

    # return jsonify(random_letters) # Return a JSON that can be pulled into JS.
    return output_list