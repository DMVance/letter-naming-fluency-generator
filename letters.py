import string, random
from flask import jsonify
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER

def generate_letters(lines, case):
    # The user selections captured by JavaScript code are passed to the Python function here and types are established.
    lines = int(lines)
    case = case.lower()

    # Depending on the user selection for case, the bank of letters is set - either upper, lower, or mixed case.
    # The full set of upper and lower case letters are contained in "string.ascii_letters".
    if case == "l":
        alphabet = list(string.ascii_lowercase)
    elif case == "u":
        alphabet = list(string.ascii_uppercase)
    elif case == "m":
        alphabet = list(string.ascii_letters)
    
    # Set the number of letters on a line to 10 and generate the random set of letters for each line.
    # Number of lines are set by user.
    p = 10
    output_list = []
    for i in range(lines):
        random_letters = random.sample(alphabet, p)
        output_list.append(random_letters)

    ##############################################
    # Generate PDF
    # Not currently getting the desired format, so this is a work in progress.

    pdf_string = '\n'.join([' '.join(map(str,l)) for l in output_list]) # Separate each letter with a space and each set on a separate line.
    canvas = Canvas("hello.pdf", pagesize=LETTER)
    canvas.setFont("Times-Roman", 18)
    [canvas.drawString(1 * inch, 10 * inch, pdf_string] # output_list[l][0]) for l in output_list]
    canvas.save()

    ##############################################

    return output_list