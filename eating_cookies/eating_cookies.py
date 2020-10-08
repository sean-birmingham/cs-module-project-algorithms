'''
Input: an integer
Returns: an integer
'''

# recursive


def eating_cookies(n):
    # base cases
    # check how many ways to eat negative num of cookies
    if n < 0:
        return 0
    # check how many ways to eat 0 cookies
    if n == 0:
        return 1

    # recursively calling function to move towards base cases
    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
