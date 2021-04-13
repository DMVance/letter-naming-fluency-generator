import string, random

def get_lines():
    while True:
        print("Please enter the number of lines and press [Enter]:")
        try:
            lines = int(input("--> "))
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

def generate_letters():

    lines = get_lines()
    case = get_case()

    if case == "l":
        alphabet = list(string.ascii_lowercase)     # Can this section be collapsed?
    elif case == "u":
        alphabet = list(string.ascii_uppercase)
    elif case == "m":
        alphabet = list(string.ascii_letters)
    
    p = 10
    for i in range(lines):
        random_letters = random.sample(alphabet, p) # send to JSON
        print(' '.join(random_letters))

    return 

def main():

    generate_letters()  # Send output to JSON for 

    return

#######################################################################################

main()