import numpy as np
import datetime as d
import math

def edit_distance(A, B):
    n = A.size
    m = B.size
    ED = np.zeros((n + 1, m + 1), dtype='int32')
    ptr = np.zeros((n + 1, m + 1), dtype='int32')

    for i in range(n + 1):  # attention:the range is from 0 to n
        ED[i, 0] = i
        if i > 0:
            ptr[i, 0] = 4  # up
    for j in range(m + 1):
        ED[0, j] = j
        if j > 0:
            ptr[0, j] = 2  # left

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # MATRIX ED
            diff = 0 if A[i - 1] == B[j - 1] else 1
            ED[i, j] = min(ED[i - 1, j] + 1, ED[i, j - 1] + 1, ED[i - 1, j - 1] + diff)
            edInt = ED[n, m]
            # TRACE-BACK
            if (ED[i, j] == ED[i - 1, j] + 1):  # UP : DELETION
                ptr[i, j] = ptr[i, j] | 4
            if (ED[i, j] == ED[i, j - 1] + 1):  # lEFT : INSERTION
                ptr[i, j] = ptr[i, j] | 2
            if (ED[i, j] == ED[i - 1, j - 1] + diff):  # DIAGONAL : SUBSTITUTION
                ptr[i, j] = ptr[i, j] | 1
    return ED, ptr, edInt