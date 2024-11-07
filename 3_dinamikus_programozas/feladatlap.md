# Módosított Fibonacci sorozat - Feladatlap

## Leírás

Írdd meg a módosított Fibonacci sorozatot generáló függvényt a következő definíció felhasználásával:

> Adott a sorozat `t[i]` és `t[i+1]` eleme, ahol `1 <= i <= ∞`, akkor a sorozat `t[i+2]` elemét a következő módon számítjuk ki:
> `t_{i+2} = t_i + (t_{i+1})^2`.

Adott három egész szám `t_1`, `t_2` és `n`, számítsd ki és írdd ki az `n`-edik elemét a módosított Fibonacci sorozatnak.

## Példa

Legyen

```
t_1 = 0
t_2 = 0
n = 6
```

Ekkor

```
t_3 = 0 + 1^2 = 1
t_4 = 1 + 1^2 = 2
t_5 = 1 + 2^2 = 5
t_6 = 2 + 5^2 = 27
```

Az eredmény `27`.

## Függvény leírása

Írdd meg a `fibonacciModified` függvényt.

A `fibonacciModified` függvénynek a következő paraméterei vannak:
- `int t1`: egy egész szám
- `int t2`: egy egész szám
- `int n`: egész szám, ahányadik elemét keressük a sorozatnak

### Visszatérési értéke

- `int n`: a sorozat `n`-edik eleme

**Megjegyzés:** `t_n` értéke meghaladhatja a `64` bites egész ábrázolási tartományát. A legtöbb programozási nyelvnek vannak könyvtárai ennek kezelésére, de azoknak, amelyeknek nincs ilyen (pl. C++), ott meg kell oldani ezt is.

## Bemenet formátuma

Egyetlen sor, amely három, szóközzel elválasztott egész számot tartalmaz, rendre a `t_1`, `t_2`, és `n` értékét.

## Megszorítások

- `0 <= t_1, t_2 <= 2`
- `3 <= n <= 20`
- `t_n` meghaladhatja a `64` bites egész ábrázolási tartományát

## Minta bemenet
```
0 1 5
```

## Minta kimenet
```
5
```

## Magyarázat

A sorozat első két eleme `t_1 = 0` és `t_2 = 0`, amely alapján kapjuk a módosított Fibonacci sorozatot: `{0, 1, 1, 2, 5, 27, ...}`. Az `5`. eleme `5`.

## Forrás
[HackerRank - Fibonacci Modified](https://www.hackerrank.com/challenges/fibonacci-modified/problem)