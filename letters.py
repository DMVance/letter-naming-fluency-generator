import string, random

def letters_gen():

    # print("Please enter the number of letters and press [Enter]: ")
    # n = input("--> ")

    print("Lowercase, Uppercase or Mixed [L, U, M]: ")
    m = input("--> ")

    # split the string of words into individual words and eliiminate unnecessary characters
    #     words = words.replace("-", " ").replace(",", " ").replace("*", " ").split(" ") # delimiter = any character in wrdset that isn't in alphabet

    if m == "L":
        alphabet = list(string.ascii_lowercase)
    elif m == "U":
        alphabet = list(string.ascii_uppercase)
    elif m == "M":
        alphabet = list(string.ascii_letters)

    n = 26
    # m = 52

    random_letters = random.sample(alphabet, n)

    # test = random_letters[:5]

    # print(', '.join(random_lowercase[:5]))
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

    return ' '.join(random_letters)

def main():

    letters_gen()

#######################################################################################

main()