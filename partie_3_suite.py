import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import folium
from collections import deque

from folium import elements

from partie_3 import Pile


class File(Pile):
    def remove(self):
        self.retire(elements)


p = File()

p.push('Mamadou')
p.push('Mansour')
p.push('Dame')
p.push('Khady')
print(p.elements)
p.remove()
print(p.elements)
