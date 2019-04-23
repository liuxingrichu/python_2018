"""
    功能：二分查找
"""


def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper)//2
        if number > sequence[middle]:
            return search(sequence, number, middle+1 , upper)
        else:
            return search(sequence, number, lower, middle)


def get_bisect(sequence, number):
    lower = 0
    upper = len(sequence) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if sequence[middle] == number:
            return middle
        elif sequence[middle] > number:
            upper = middle - 1
        else:
            lower = middle + 1
    return -1


def find_bisect(sequence, number, start, end):
    while start <= end:
        position = (start + end)//2
        if sequence[position] == number:
            return position
        if sequence[position] > number:
            end = position - 1
            return find_bisect(sequence, number, start, end)
        else:
            start = position + 1
            return find_bisect(sequence, number, start, end)
    return -1


test_list = [1, 2, 5, 8, 9, 14, 16, 19, 21, 31, 45, 65]
while True:
    guess = int(input("Enter integer: "))
    # result = search(test_list, guess, 0, len(test_list) - 1)
    # result = get_bisect(test_list, guess)
    result = find_bisect(test_list, guess, 0, len(test_list) - 1)
    print(result)
