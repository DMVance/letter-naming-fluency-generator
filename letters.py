import string, random
from flask import jsonify
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER

def generate_letters(lines, case):

    lines = int(lines)
    case = case.lower()

    if case == "l":
        alphabet = list(string.ascii_lowercase)
    elif case == "u":
        alphabet = list(string.ascii_uppercase)
    elif case == "m":
        alphabet = list(string.ascii_letters)
    
    p = 10
    output_list = []
    for i in range(lines):
        random_letters = random.sample(alphabet, p)
        output_list.append(random_letters)

    ##############################################
    # Generate PDF

    # pdf_string = '\n'.join([' '.join(map(str,l)) for l in output_list])
    # canvas = Canvas("hello.pdf", pagesize=LETTER)
    # canvas.setFont("Times-Roman", 18)
    # [canvas.drawString(1 * inch, 10 * inch, output_list[l][0]) for l in output_list]
    # canvas.save()

    ##############################################

    return output_list