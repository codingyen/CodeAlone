import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = 5
    b = bin(n)
    maxcon = 0
    curr = 0
    for i in range(2, len(b)):
        if int(b[i]) == 1:
            curr += 1
        else:
            curr = 0
        maxcon = max(maxcon, curr)

    print(maxcon)