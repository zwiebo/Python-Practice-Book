# Created by Lukas on 15.04.2019 #
# Basic functionalises of numbers


def show_possible_operators(a, b):
    #

    print("{} + {} = {}".format(a, b, a + b))
    print("{} - {} = {}".format(a, b, a - b))
    print("{} * {} = {}".format(a, b, a * b))
    print("{} / {} = {}".format(a, b, a / b))
    print("{} % {} = {}".format(a, b, a % b))
    print("{} ** {} = {}".format(a, b, a ** b))

def make_a_nice_output():
    # takes input from show_possible_operators and makes a nice output
    welcome_text = "this script is an example of the operators"
    print(welcome_text)
    print()
    show_possible_operators(42, 8 )
    print()

if __name__ == "__main__":
    make_a_nice_output()






