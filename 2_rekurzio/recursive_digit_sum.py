#!/bin/python3


def superDigit(n, k):

    # ha n mar eleve egy szamjegybol all, amelyet pontosan
    # egyszer kell egymas utan irni, akkor visszaadjuk n-et
    if len(n) < 2 and k == 1:
        return n

    # kulonben kiszamoljuk n szamjegyeinek osszeget
    sum = 0
    for digit in n:
        sum += int(digit)

    # majd vesszuk azt a szamot, amelyet ugy kapunk, hogy
    # n szamjegyeinek osszeget k-szor egymas utan irjuk;
    # az egymas utan iras, azaz k erteket 1-re allitjuk
    return superDigit(str(sum) * k, 1)


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)
