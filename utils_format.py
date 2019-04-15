# Created by Lukas on 15.04.2019 #
# this utils file provides some nice format stuff


# Formatter
def add_start(text, symbol = "*"):
    start = " start ".center(80, symbol) +"\n"
    nice_text = start + text
    return nice_text


def add_fin(text, symbol = "*"):
    fin = "\n" + " fin ".center(80,symbol)
    nice_text = text + fin
    return nice_text


def surround_text_with_and_fin(text, symbol = "*"):
    nice_text = add_fin(add_fin(text))
    return add_fin(add_start(text))


def put_in_box(text):
    # puts the in a box
    if not isinstance(text, list):
        text = text.split("\n")

    nice_text = ""
    nice_text += "-" * 80 + "\n"

    for row in text:
        nice_text += "|{:78}|\n".format(row)

    nice_text += "-" * 80
    return nice_text


# Tests
def compare_while_ignoring_cases(*args):
    if isinstance(args[0], list):
        args = args[0]
    for _arg in args:
        if not str(_arg).lower() == str(args[0]).lower():
            return False

    return True


if __name__ == "__main__":
    test_string = ">>This is just a test<<"

    """
    print(surround_text_with_and_fin(test_string))
    print(put_in_box(test_string))
    list_of_things = ["apple", "bee", "dog"]
    print(surround_text_with_and_fin(put_in_box(list_of_things)))
    """

    print(compare_while_ignoring_cases("ab", "A"))
    print(compare_while_ignoring_cases("a", "A"))
    print(compare_while_ignoring_cases("aa", "Aa"))
    print(compare_while_ignoring_cases("Aaa", "Aaa", "AAA"))
    print(compare_while_ignoring_cases("Aaa", "Aaa", "AAb"))
    print(compare_while_ignoring_cases("a", "Aa"))
    print(compare_while_ignoring_cases(["a", "B"]))
    print(compare_while_ignoring_cases(["a", "A"]))
