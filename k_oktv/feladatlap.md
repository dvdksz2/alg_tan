# Automata - Feladatlap

## Leírás

Egy automata különböző egész számokat tartalmazó sorozatot dolgoz fel. Egyesével balról-jobbra
haladva veszi a sorozat számait és egy sor adatszerkezet felhasználásával végez műveletet.
Kezdetben a sor üres. Az aktuális számmal az alábbi műveletek közül az első olyat hajtja végre,
amelyre a feltétel teljesül:
- ha a sor üres, a végére teszi
- ha a sor utolsójánál nagyobb, a végére teszi
- ha az utolsó kiírtnál kisebb, akkor hibajelzéssel megáll
- ha a sor elsőjénél kisebb, akkor kiírja
- amíg a sor elsőjénél nagyobb, addig kiírja a sor elsőjét (és a kiírt elemet ki is veszi a sorból);
ilyenkor, ha a sor üressé válik, akkor a bemeneti értéket a sorba teszi, különben kiírja
- az utolsó érték feldolgozása után a sorban levőket kiírja

1. Minden elem érkezése után add meg a sorban levő elemeket és a kiírt értékeket az alábbi
bemenetre: 3 4 6 1 8 2 5 9 7.

2. Mi a feltétele annak, hogy hibajelzéssel áll meg a feldolgozás? Adj meg egy konkrét sorozatot,
amire hibajelzéssel megáll!



## Forrás 

[OKTV 2023/2024. tanév, 1. forduló, Digitális kultúra II. kategória, feladatlap, 4. feladat](https://www.oktatas.hu/pub_bin/dload/kozoktatas/tanulmanyi_versenyek/oktv/oktv2023_2024_1ford/digkult2_flap1f_oktv_2324.pdf)