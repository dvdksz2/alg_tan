#!/bin/python3


def halmazt_keres(csucs, halmazok):
    # megkeressuk, hogy melyik csucshalmaz tartalmazza
    # a keresett csucsot
    for i in range(len(halmazok)):
        if csucs in halmazok[i]:
            return i


def kruskals(g_nodes, g_from, g_to, g_weight):

    # beallitjuk, hogy a kezdo teljes suly nulla legyen
    teljes_suly = 0

    # a bemenetkent kapott graf minden egyes csucsat eltaroljuk
    # egy halmazba
    halmazok = []
    for i in range(1, g_nodes + 1):
        halmazok.append({i})

    # atalakitjuk a bemenetet, hogy konnyebben kezelheto legyen
    # az eleket egy dict-be helyezzuk, ahol a kulcs az el
    # altal osszekotott ket csucs, mig az ertek az el sulya
    elek = {}
    for i in range(len(g_from)):
        elek[(g_from[i], g_to[i])] = g_weight[i]

    # rendezzuk az eleket sulyuk szerint novekvo sorrendbe
    rendezett_elek = sorted(elek.items(), key=lambda x: x[1])

    # vegigmegyunk a rendezett eleken
    for (ki, be), suly in rendezett_elek:
        # meghatarozzuk, hogy az el egyik csucsa melyik halmazban van
        ki_halmaz = halmazt_keres(ki, halmazok)
        # meghatarozzuk, hogy az el masik csucsa melyik halmazban van
        be_halmaz = halmazt_keres(be, halmazok)
        # ha a ket halmaz kulonbozik, azaz az el hozzavetele nem hoz
        # letre kort
        if ki_halmaz != be_halmaz:
            # hozzavesszuk az elt, igy a sulya beleszamit a teljes sulyba
            teljes_suly += suly
            # a ket csucshalmazt egyesitjuk
            halmazok[ki_halmaz].update(halmazok[be_halmaz])
            del halmazok[be_halmaz]

    # visszaadjuk a teljes sulyt
    return teljes_suly


if __name__ == "__main__":
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    overall_weight = kruskals(g_nodes, g_from, g_to, g_weight)

    print(overall_weight)
