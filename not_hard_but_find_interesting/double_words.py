def double_string(string):
    double_character = []
    for character in string:
        new_character = "".join(character * 2 for character in string)
        double_character.append(new_character)
        double_character = "".join(new_character)
        return double_character
    

# ----------------- pre-setted inputs -------------------



run_cases = [
    ("Hello there", "HHeelllloo  tthheerree"),
    ("General Kenobi", "GGeenneerraall  KKeennoobbii"),
]

submit_cases = run_cases + [
    ("I am a warrior", "II  aamm  aa  wwaarrrriioorr"),
    ("Where is the nearest inn?", "WWhheerree  iiss  tthhee  nneeaarreesstt  iinnnn??"),
    (
        "what is happening to my chat?",
        "wwhhaatt  iiss  hhaappppeenniinngg  ttoo  mmyy  cchhaatt??",
    ),
    (
        "what did this potion do to me?",
        "wwhhaatt  ddiidd  tthhiiss  ppoottiioonn  ddoo  ttoo  mmee??",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = double_string(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()