# Módosított Fibonacci sorozat - A megoldás magyarázata

A megoldás a `fibonacci_modified.py` szkript fájlban található, azon belül is a `fibonacciModified` függvényben van lekódolva. Mielőtt azonban rátérnénk az előbb említett függvény tárgyalására, fontos megjegyezni, hogy a megoldásunkban kezelnünk kell  a nagyméretű egész számok problémáját, amelyet a feladat leírása is említett. Ehhez a Python beépített `sys` modulját fogjuk használni az alábbiak szerint:
```python
import sys

# beallitjuk, hogy a programunk tudjon kezelni 
# nagymeretu egesz szamokat is
sys.set_int_max_str_digits(1000000)
```

Ezután rátérünk a `fibonacciModified` függvény tárgyalására. Először létrehozunk egy `n` elemű listát az alábbiak szerint, amelyben a sorozat elemeit fogjuk majd eltárolni.
```python
# keszitunk egy n elemu listat csupa nulla elemekbol
arr = [0] * n
```
Ezt követően eltároljuk a sorozat első két elemét a listánkban a következők szerint:
```python
# a lista elso elemet atirjuk t1-re
arr[0] = t1
# a lista masodik elemet atirjuk t2-re
arr[1] = t2
```

Majd kiszámoljuk a sorozat hiányzó elemeit a megadott képlet segítségével egészen az `n`-edik elemig:
```python
for i in range(2, n):
    # a lista tovabbi elemeit pedig meghatarozzuk a megadott
    # keplet segitsegevel
    arr[i] = arr[i - 2] + arr[i - 1] ** 2
``` 

Listánk utolsó eleme tartalmazza a keresett sorozatelemet, így azt visszaadjuk az alábbiak szerint:
```python
# a lista utolso eleme megfelel a sorozat keresett elemenek
# igy azt visszaadjuk
return arr[n - 1]
```