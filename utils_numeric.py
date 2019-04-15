# Created by Lukas on 15.04.2019 #
# some utils for numeric interactions


def count_digits(number, include_decimals=True):
    number_str = str(number)

    if include_decimals == False:
        number_str = number_str.split(".")
        number_str = number_str[0]

    number_str = number_str.replace(".", "")
    return len(number_str)


if __name__ == "__main__":
    print(count_digits(128129))
    print(count_digits(12.9))
    print(count_digits(12.9, include_decimals=False))
