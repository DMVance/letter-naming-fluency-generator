import string, random

def get_lines():
    while True:
        print("Please enter the number of lines and press [Enter]:")
        try:
            lines = int(input("--> ")) # How to get input from HTML?
        except ValueError:
            print("Not a valid number.")
            continue
        if lines < 0:
            print("Your response must be a positive number.")
            continue
        break

    return lines

def get_case():
    while True:
        print("Would you like Uppercase, Lowercase or Mixed [U, L, M]?")
        case = input("--> ")
        case = case.lower()
        if case not in ('u', 'l', 'm'):
            print("Please enter either 'U', 'L', or 'M'")
            continue
        break

    return case

def generate_letters(lines, case):

    # lines = get_lines()  # Get from HTML input or app.js rather than function
    # case = get_case()    # Get from HTML input or app.js rather than function

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
        print(' '.join(random_letters))

    return random_letters # Return a JSON that can be pulled into JS.

# def main():

#     generate_letters()

#     return

# Here in python generate the printable PDF of the generated letters.
# Research how to format the PDF for aesthetically pleasing results.

#######################################################################################

# main()