import string, random

def generate_letters():

    p = 10
    
    # while True:
    #     try:
    #         print("Please enter the number of lines and press [Enter]: ")
    #         lines = int(input("--> "))
    #     except ValueError:
    #         print("Error: invalid entry.")  # Research proper use of exception handling.
    #         continue

    #     if lines < 0:
    #         print("Your response must be a positive number.")
    #         continue
    #     else:
    #         break




    # while True:
    # try:
    #     age = int(input("Please enter your age: "))
    # except ValueError:
    #     print("Sorry, I didn't understand that.")
    #     continue

    # if age < 0:
    #     print("Sorry, your response must not be negative.")
    #     continue
    # else:
    #     #age was successfully parsed, and we're happy with its value.
    #     #we're ready to exit the loop.
    #     break

    while True:
    data = input("Please enter a loud message (must be all caps): ")
    if not data.isupper():
        print("Sorry, your response was not loud enough.")
        continue
    else:
        #we're happy with the value given.
        #we're ready to exit the loop.
        break

    while True:
        data = input("Pick an answer from A to D:")
        if data.lower() not in ('a', 'b', 'c', 'd'):
            print("Not an appropriate choice.")
        else:
            break

    # if case == "l":
    #     alphabet = list(string.ascii_lowercase)     # Can this section be collapsed?
    # elif case == "u":
    #     alphabet = list(string.ascii_uppercase)
    # elif case == "m":
    #     alphabet = list(string.ascii_letters)

    for i in range(lines):
        random_letters = random.sample(alphabet, p)
        print(' '.join(random_letters))



    return # ' '.join(random_letters)

def main():

    generate_letters()

#######################################################################################

main()