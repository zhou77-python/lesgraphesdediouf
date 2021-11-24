import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import folium
from collections import deque

from folium import elements


class Pile:  # Le debut de la classe Pile

    def __init__(self):
        self.elements = []

    def push(self, noeud):  # Cette methode ou fonction permet d'inserer un objet en tete de file
        self.elements.append(noeud)
        return noeud

    def contains_noeud(self, name):  # Cette methode ou fonction permet de retourner true si un noeud est dans la pile
        name in self

    def is_empty(self):  # Cette methode ou fonction permet de retourner true si la pile est vide
        return len(self.elements) == 0

    def remove(self):  # Cette methode ou fonction permet de retourner ou de supprimer l'element en tete de file
        self.remove(elements)  # Elle permet aussi de retourner une exception si la pile est vide


f = Pile()
f.push('Mamadou')
f.push('Mansour')
f.push('Dame')
f.push('Khady')
f.elements.reverse()
print(f.elements)
f.elements.remove('Khady')
print(f.elements)
