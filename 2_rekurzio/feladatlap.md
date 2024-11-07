# Rekurzív számjegyösszeadás - Feladatlap

## Leírás

Egy `x` egész szám szuperszámjegyét a következő szabályok szerint definiáljuk:
- ha `x` egyetlen számjegyből áll, akkor `x` szuperszámjegye önmaga,
- különben `x` szuperszámjegye egyenlő az `x`-et alkotó számjegyek összegének szuperszámjegyével.

Például `9875` szuperszámjegyét a következőképpen számíthatjuk ki:
```
superDigit(9875)            // 9+8+7+5 = 29
  = superDigit(29)          // 2+9 = 11
  = superDigit(11)          // 1+1 = 2
  = superDigit(2)          
  = 2
```
## Példa
Legyen `n=9875` és `k=4`. A `p` számot úgy állítjuk elő, hogy az `n` számot `k`-szor egymás után írjuk, ekkor kapjuk, hogy `p=9875987598759875`.

```
superDigit(p)   
  = superDigit(9875987598759875)  // 9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
  = superDigit(116)               // 1+1+6 = 8
  = superDigit(8)                      
  = 8
```
A fentebbi számítások alapján jól látható, hogy `p` számjegyeinek összege `116`, `116` számjegyeinek összege `8`, `8` pedig egyetlen számjegyből áll, tehát már szuperszámjegy.

## Függvény leírása

Írdd meg a `superDigit` függvényt.

A `superDigit` függvény a következő bemeneti paraméterekkel rendelkezik:
- `string n`: az egész szám sztring reprezentációja
- `int k`: ahányszor egymás után kell írni `n`-et, hogy megkapjuk `p`-t

### Visszatérési értéke

- `int`: a `k`-szor egymás után írt `n` szám, azaz `p` szuperszámjegye
  
## Bemenet formátuma

Az első sor két, szóközzel elválasztott egész számot tartalmaz, rendre `n`-et és `k`-t.

## Megkötések

- `1 <= n < 10^100000`
- `1 <= k <= 10^5`

## Minta bemenet 0
```
148 3
```

## Minta kimenet 0
```
3
```

## Magyarázat 0

Mivel `n=148` és `k=3`, így `p=148148148`. Ekkor
```
superDigit(p)   = superDigit(148148148)      // 1+4+8+1+4+8+1+4+8 = 39
                = superDigit(39)             // 3+9 = 12
                = superDigit(12)             // 1+2 = 3
                = superDigit(3)              
                = 3
```

## Minta bemenet 1
```
9875 4
```

## Minta kimenet 1
```
8
```

## Magyarázat 1

Lásd a [Példánál](#példa).

## Minta bemenet 2
```
123 3
```

## Minta kimenet 2
```
9
```

## Magyarázat 2

Mivel `n=123` és `k=3`, így `p=123123123`. Ekkor
```
superDigit(p)   = superDigit(123123123)     // 1+2+3+1+2+3+1+2+3 = 18
                = superDigit(18)            // 1+8 = 9
                = superDigit(9)             
                = 9
```


## Forrás
[HackerRank - Recursive Digit Sum](https://www.hackerrank.com/challenges/recursive-digit-sum/problem)