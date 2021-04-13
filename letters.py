import string, random

def generate_letters():

    p = 10
    
    while True:
        print("Please enter the number of lines and press [Enter]:")
        try:
            lines = int(input("--> "))
            print(type(lines))
        except ValueError:
            print("Not a valid number.")
            continue
        if lines < 0:
            print("Your response must be a positive number.")
            continue
        break

    while True:
        print("Would you like Uppercase, Lowercase or Mixed [U, L, M]?")
        case = input("--> ")
        case = case.lower()
        if case not in ('u', 'l', 'm'):
            print("Please enter either 'U', 'L', or 'M'")
            continue
        break

    if case == "l":
        alphabet = list(string.ascii_lowercase)     # Can this section be collapsed?
    elif case == "u":
        alphabet = list(string.ascii_uppercase)
    elif case == "m":
        alphabet = list(string.ascii_letters)

    for i in range(lines):
        random_letters = random.sample(alphabet, p)
        print(' '.join(random_letters))



    return # ' '.join(random_letters)

def main():

    generate_letters()

#######################################################################################

main()