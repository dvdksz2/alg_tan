#!/bin/python3


def luckBalance(k, contests):

    # rendezzuk a versenyeket a hozzajuk tartozo szerencseertekek szerint
    # csokkeno sorrendbe (vo. moho strategia)
    contests.sort(key=lambda x: int(x[0]), reverse=True)

    # beallitjuk Lena kezdo szerencseegyenleget
    luck = 0

    # vegigmegyunk a versenyek tombjen
    for c in contests:
        # ha a verseny nem fontos, akkor Lena nyugodtan elveszitheti
        if c[1] == 0:
            # ekkor no Lena szerencseegyenlege a versenyhez
            # tartozo szerencseertekkel
            luck += c[0]
            continue
        # ha a verseny fontos, viszont Lenanak meg van bukasi lehetosege
        if k > 0:
            # ekkor is no Lena szerencseegyenlege a versenyhez
            # tartozo szerencseertekkel
            luck += c[0]
            # viszont csokken Lena bukasi lehetosegeinek szama
            k -= 1
            continue
        # ha a verseny fontos, viszont Lenanak mar nincs tobb bukasi lehetosege,
        # akkor Lena szerencseegyenlege csokken a versenyhez tartozo
        # szerencseertekkel
        luck -= c[0]

    # visszaadjuk Lena szerencseegyenlegenek erteket a versenyek utan
    return luck


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)
