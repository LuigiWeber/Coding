"""
Write a function VowelSum that takes as input a string, and return a number that is the sum of the vowels in that string. To do so,
the vowels must be considered as numbers, and their values are the following:

Vowel   Value
A       4
E       3
I       1
O,U     0

Example:
Input: "hello"
Output: 3

Input: "hello there"
Output: 9
"""

def VowelSum(input_string):
    # just in case you need these lists :)
    vowels = ['a', 'e', 'i', 'o', 'u']
    values = [4, 3, 1, 0, 0]


    result = 0

    # write your instructions here

    return result

# Write your test code inside this statement
if __name__ == "__main__":
    VowelSum("")