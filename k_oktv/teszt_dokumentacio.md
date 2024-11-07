# Automata - Teszt dokumentáció 

Az automata feladat teszteléséhez összesen két darab teszteset áll rendelkezésre  (bemenetek és a hozzájuk tartozó elvárt kimenetek egyaránt). Ezen tesztesetek a [test](./test/) könyvtárban találhatóak, minden `$i in {0,1}`-re az `i`-edik tesztesethez tartozó bemenet neve `input$i.txt` a hozzá tartozó elvárt kimenet neve pedig `output$i.txt`. Mindkét teszteset az [OKTV 2023/2024. tanév, 1. forduló, Digitális kultúra II. kategória, javítási-értékelési útmutató, 4. feladat](https://www.oktatas.hu/pub_bin/dload/kozoktatas/tanulmanyi_versenyek/oktv/oktv2023_2024_1ford/digkult2_javut1f_oktv_2324.pdf) oldalról származik. A tesztesetek automatikusan lefuttathatóak az alábbi módon.

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
```

Abban az esetben viszont ha valamelyik teszteset elbukik, akkor annál a tesztesetnél a "`passed`" helyett "`failed`" jelenik meg, pl.
```bash
test 0...failed.
```