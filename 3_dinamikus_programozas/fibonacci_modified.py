#!/bin/python3

import sys

# beallitjuk, hogy a programunk tudjon kezelni
# nagymeretu egesz szamokat is
sys.set_int_max_str_digits(1000000)


def fibonacciModified(t1, t2, n):
    # keszitunk egy n elemu listat csupa nulla elemekbol
    arr = [0] * n

    # a lista elso elemet atirjuk t1-re
    arr[0] = t1
    # a lista masodik elemet atirjuk t2-re
    arr[1] = t2

    for i in range(2, n):
        # a lista tovabbi elemeit pedig meghatarozzuk a megadott
        # keplet segitsegevel
        arr[i] = arr[i - 2] + arr[i - 1] ** 2

    # a lista utolso eleme megfelel a sorozat keresett elemenek
    # igy azt visszaadjuk
    return arr[n - 1]


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    print(result)
