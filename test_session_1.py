# Created by Lukas on 15.04.2019 #


import utils_numeric
import utils_format

def test_count_digits():
    # test for util_numeric.count_digits
    assert utils_numeric.count_digits(12447) == 5
    assert utils_numeric.count_digits(124.47) == 5
    assert utils_numeric.count_digits(12447.123123, include_decimals=False) == 5
    assert utils_numeric.count_digits(0.1215) == 5


def test_compare_strings():
    # test uttil for comarision if strings are the sam while ignoring cases
    # cases set of strings
    cases = [
        [["a", "a", "a"],              True],
        [["a", "A", "a"],              True],
        [["a", "aa", "a"],             False],
        [["a", 100, "a"],              False],
        [["a", "a", "a", "Johnny"],    False],
        [["a"],                      True],
    ]

    for case in cases:
        print(case)
        print(case[0]), case[1]
        print()
        assert utils_format.compare_while_ignoring_cases(case[0]) == case[1]