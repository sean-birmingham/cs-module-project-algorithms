'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # counting all zeros
    zeros = arr.count(0)
    next_index = 0

    for n in arr:
        if n != 0:
            arr[next_index] = n
            next_index += 1

    for zero in range(1, zeros + 1):
        arr[-zero] = 0

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
