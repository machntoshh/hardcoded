def find_max(nums):
    max_so_far = float("-inf")
    if nums == []:
        return max_so_far
        
    for number in nums:
        if number > max_so_far:
            max_so_far = number
    return max_so_far 

"""
1- Caso a lista já estiver vazia, nem rode nada, só retorne a var max_so_far

2- Com o return fora do código, ele vai ficar rodando o loop até achar o maior numero da lista.
   Se estivesse dentro ele iria parar no primeiro número maior que max_so_far
"""


# ----------------- pre-setted inputs -------------------


run_cases = [([1, 2, 3, 4, 5], 5), ([1, 2, 300, 4, 5], 300)]

submit_cases = run_cases + [
    ([1, 20, 3, 4, 5], 20),
    ([-1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 21, 18], 21),
    ([], float("-inf")),
    ([-1, -2, -3, -4, -5], -1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = find_max(input1)
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