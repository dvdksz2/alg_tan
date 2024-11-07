#!/usr/bin/env bash

# tesztelendo szkript neve
SCRIPT_NAME=luck_balance.py

# tesztesetek szama
NUM_OF_TESTS=12

for i in $(seq 0 $NUM_OF_TESTS); do
    echo -n "test $i..."

    # lefuttatjuk a szkriptet az adott tesztbemenetre, majd
    # a kimenetkent kapott eredmenyt eltaroljuk a valtozoban
    RESULT=$(cat "test/input$i.txt" | python3 $SCRIPT_NAME)

    # eltaroljuk az tesztesethez tartozo elvart kimenet 
    # erteket a valtozoban
    EXPECTED=$(cat "test/output$i.txt")

    # ha a kapott es az elvart kimenet megegyezik
    if [[ $RESULT -eq $EXPECTED ]]; then
        # a teszteset sikeres
        echo "passed."
    else
        # a teszteset sikertelen
        echo "failed."
    fi
done