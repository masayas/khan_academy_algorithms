"""
Implementing binary search of an array
https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
"""
import math


def binary_search(min, max, l, target):
    if max < min:
        print("the target was not in the list")
        return -1

    guess = math.floor((min + max)/2)
    print("guess: ", guess)
    if l[guess] == target:
        return guess
    if l[guess] < target:
        min = guess + 1
    else:
        max = guess - 1
    return binary_search(min, max, l, target)


if __name__ == "__main__":
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    n = len(l)
    target = 67
    min = 0
    max = n-1
    print(binary_search(min, max, l, target))
