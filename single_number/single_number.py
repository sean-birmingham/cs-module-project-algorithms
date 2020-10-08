'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # [2, 2, 1]
    # loop to check if number appears once
    # i is 0, 2 appears once
    # i is 1, 2 appears again
    # i is 3, 1 appears once
    # 1 is the odd-number-out
    for i in arr:
        # does num appear once?
        if arr.count(i) == 1:
            return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
