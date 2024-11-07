# Szerencseegyenleg - Feladatlap

## Leírás

Léna egy fontos kódolóversenyre készül, amelyet számos, egymást követő előzetes verseny előz meg. Kezdetben a szerencseegyenlege `0`. Léna bízik a "szerencse tartalékolásában", és szeretné ellenőrizni az elméletét. Minden előzetes versenyt két egész szám `L[i]` és `T[i]` ír le:

- `L[i]` a versenyhez kapcsolódó szerencse mennyisége. Ha Léna megnyeri a versenyt, akkor szerencseegyenlege ennyivel csökken; viszont ha elveszíti, akkor ennyivel nő.

- `T[i]` a verseny fontossági besorolását jelöli. Ez egyenlő `1`-gyel, ha a verseny fontos, és egyenlő `0`-val, ha nem fontos.

Ha Léna nem veszít többet, mint `k` fontos versenyt, mennyi szerencséje lehet az összes előversenyen való részvétel után? (Megjegyezzük, hogy a szerencseegyenleg értéke negatív is lehet.)

## Példa

```
k = 2
L = [5, 1, 4]
T = [1, 1, 0]
```
| Verseny | `L[i]` | `T[i]` |
| -----------: | -----------: | -----------: |
| 1 | 5 | 1 |
| 2 | 1 | 1 |
| 3 | 4 | 0 |

Ha Léna az összes versenyt elveszíti, akkor a végső szerencseegyenlege `5+1+4=10` lesz. Mivel megengedett veszítenie két fontos versenyen, és mivel csak két fontos verseny van, így mindhárom versenyt elveszítheti, hogy maximalizálja a szerencséjét elérve a `10`-es értéket.

Ha `k=1`, akkor a kettő közül legalább az egyik fontos versenyt meg kell nyernie. Ekkor Léna úgy döntene, hogy megnyeri a legalacsonyabb szerencseértékű fontos előversenyt. A végső szerencséje ekkor `5+4-1=8` lesz.

## Függvény leírása
Írdd meg a `luckBalance` függvényt, mely a következő paraméterekkel rendelkezik:

- `int k`: hány fontos versenyt veszíthet Léna maximum

- `int contests[n][2]`: egész számok 2D tömbje, ahol mindegyik `contests[i]` két egész számot tartalmaz, amelyek az `i`-edik verseny szerencseértékét és fontosságát jelzik.

### Visszatérési értéke

- `int`: az elérhető maximális szerencseegyenleg

## Bemenet formátuma

Az első sor két, szóközzel elválasztott egész számot tartalmaz, amelyet `n`-nel és `k`-val jelölünk, ahol `n`  az előzetes versenyek száma, `k` pedig a fontos versenyek maximális száma, amelyet Léna elveszíthet.

A következő `n` sor két, szóközzel elválasztott egész számot tartalmaz, amelyet `L[i]`-vel és `T[i]`-vel jelölünk, ahol `L[i]` és `T[i]` jelöli rendre az `i`-edik verseny szerencseértékét és fontosságát.

## Megszorítások
- `1 <= n <= 100`
- `0 <= k <= N`
- `1 <= L[i] <= 10^4`
- `T[i]` eleme a  `{0, 1}` halmaznak

## Minta bemenet

```
STDIN       Függvény
-----       --------
6 3         n = 6, k = 3
5 1         contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
2 1
1 1
8 1
10 0
5 0
```
## Minta kimenet
```
29
```

## Magyarázat
Lénának `n=6` előzetes versenye van, ezek közül négy fontos, és ebből nem veszíthet többet, mint `k=3`. Léna úgy maximalizálhatja a szerencséjét, ha megnyeri a harmadik fontos előversenyt, ahol `L[i]=1`, és elveszíti az összes többi öt versenyt, hogy a szerencseegyenlege `5+2+8+10+5-1=29` legyen.

## Forrás
[HackerRank - Luck Balance](https://www.hackerrank.com/challenges/luck-balance/problem)