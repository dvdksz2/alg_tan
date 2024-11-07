# Szerencseegyenleg - Teszt dokumentáció 

A szerencseegyenleg feladat teszteléséhez összesen tizenhárom darab teszteset áll rendelkezésre  (bemenetek és a hozzájuk tartozó elvárt kimenetek egyaránt). Ezen tesztesetek a [test](./test/) könyvtárban találhatóak, minden `$i in {0,1...,12}`-re az `i`-edik tesztesethez tartozó bemenet neve `input$i.txt` a hozzá tartozó elvárt kimenet neve pedig `output$i.txt`. Minden teszteset a [HackerRank - Luck Balance](https://www.hackerrank.com/challenges/luck-balance/problem) oldalról származik. A tesztesetek automatikusan lefuttathatóak az alábbi módon.

Ha a `test.sh` bash szkript nem rendelkezik futtatási jogosultsággal, akkor adjunk neki ilyet, pl.
```bash
chmod a+x test.sh
```

Ezután pedig futtassuk a bash szkriptet az alábbi módon:
```bash
./test.sh
```

Ha a tesztelés során minden rendben ment, akkor a következő kimenetet kapjuk:
```bash
test 0...passed.
test 1...passed.
test 2...passed.
test 3...passed.
test 4...passed.
test 5...passed.
test 6...passed.
test 7...passed.
test 8...passed.
test 9...passed.
test 10...passed.
test 11...passed.
test 12...passed.
```

Abban az esetben viszont ha valamelyik teszteset elbukik, akkor annál a tesztesetnél a "`passed`" helyett "`failed`" jelenik meg, pl.
```bash
test 0...failed.
```