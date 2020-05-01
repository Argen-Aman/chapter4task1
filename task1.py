#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    list_of_brackets = []
    brackets = {'}': '{', ']': '[', ')': '('}
    for i in s:
        if i in brackets and list_of_brackets and brackets[i] == list_of_brackets[-1]:
            list_of_brackets.pop()
        else:
            list_of_brackets.append(i)

    if list_of_brackets:
        return("NO")
    else:
        return("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
