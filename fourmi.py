# -*- coding: utf-8 -*-

import math
import networkx
import matplotlib.pyplot as plt
import pants
import csv

noeuds = []
distances = []
iteration = 10
nombre_bars = 100

"""
Récupération des données dans le fichier csv 
"""
with open('open_pubs.csv', 'r') as csvfile:
    rows = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
    for row in rows:
        try:
            x = float(row[6])
            y = float(row[7])
            noeuds.append((x, y))
        except:
            continue

"""
Calcul de la moyenne
:return: la moyenne calculée
:rtype: int
"""
def calcul_moyenne(echantillon):
    moyenne = sum(echantillon) / len(echantillon)
    return moyenne
print("Distance Moyenne = " + str(calcul_moyenne(calcul_distance)) + " km")

"""
Calcul de la variance
:return: la variance calculée
:rtype: int
"""
def calcul_variance(echantillon): 
    moyenne = calcul_moyenne(echantillon)
    variance = moyenne([(x-m)**2 for x in echantillon])
    return variance
print("Variance = " + str(calcul_variance(calcul_distance)))

"""
Calcul de l'écart type
:return: l'écart type calculé
:rtype: int
"""
def calcul_ecart_type(echantillon):
    ecart_type = variance(echantillon)**0.5
    return ecart_type
print("Ecart type = " + str(calcul_ecart_type(calcul_distance)))

"""
Calcul de la distance
:return: la distance entre les coordonées
:rtype: int
"""
def calcul_distance(a, b):
    rayon = 6378 
    x = (b[1] - a[1]) * math.cos( 0.5*(b[0]+a[0]) )
    y = b[0] - a[0]
    distance = rayon * math.sqrt( x*x + y*y )
    return distance

G=networkx.Graph()

monde = pants.World(pop, calcul_distance)
solver = pants.Solver()
solution = solver.solve(monde)

"""
Limitation des données
"""
for i in range(iteration):
    pop = noeuds[i * nombre_bars:(i + 1) * nombre_bars]
    pop = set(pop)
    pop = list(pop)
    G.clear()
    
    distances.append(solution.calcul_distance)
    G.add_edges_from([(edge.start, edge.end) for edge in solution.path])
    plt.clf()
    plt.pause(1)
    networkx.draw(G)
    
    plt.title("distance = %s" % solution.calcul_distance)
    plt.savefig("./images/d_%s.png" % i, bbox_inches="tight")
    plt.show()
    
print("Distance", i, "=", solution.calcul_distance + "km")
    






