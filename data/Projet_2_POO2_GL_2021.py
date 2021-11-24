from folium.map import Tooltip
import pandas as pd
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from folium import plugins
import os


import folium
import csv

lire = pd.read_csv("transport-nodess.csv")
print(lire.shape)
print(lire.head(15))

lire1 = pd.read_csv("transport-relationships.csv")
print(lire1.shape)
print(lire1.head(15))


#creation map objet
center=(54.72479325042186, -1.952030376476062)
map_colony = folium.Map(location=center, zoom_start=8 , control_scale=True)
#variable tooltip
tooltip='voir plus' 
#group-data
group=os.path.join('group.json')

#creation  des markers
folium.Marker([52.379189,
4.899431],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([52.092876,
5.104480 ],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([52.078663,
4.288788],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([53.612390,
-0.222190],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([53.522850,
-1.131160],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([51.977500,
4.133330],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([51.963750,
1.351100],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([52.059170,
1.155450],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([51.889210,
0.904210],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([51.509865,
-0.118092],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
folium.Marker([51.922500,
4.479170],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony)
folium.Marker([52.016670,
4.708330],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(map_colony) 
#choisir type de map 
#select


# add tiles to map
folium.raster_layers.TileLayer('Open Street Map').add_to(map_colony)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(map_colony)

# add layer control to show different maps
folium.LayerControl().add_to(map_colony)
#geojson 
folium.GeoJson(group, name='cambridge').add_to(map_colony)
# display map

map_colony.save('map.html')


"""for index, lire in lire.iterrows():
    location=[lire['latitude'], lire['longitude']]
    folium.Marker(location, popup=f'Name:{lire["Colony"]}').add_to(map_colony)
map_colony.save(map.html)"""

"""df = pd.read_csv('transport-nodes.csv')
Graphtype= nx.Graph()
G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)
nx.draw(df)"""
"""df= pd.DataFrame(lire)
df.plot()
plt.show()"""
"""G=nx.read_edgelist("transport-nodes.csv")"""
"""#visualisation
pos=nx.spring_layout(G)   			#choix de l'algorithme
nx.draw(G, pos, with_labels=True)
plt.show()
#plt.savefig("edge_colormap.png") #export dans un format donné

#analyse

print ("number of nodes : %s" % G.number_of_nodes())
print ("number of edges : %s" % G.number_of_edges())

print(G.in_degree())
print (G.out_degree())

#graphe non orienté

G=G.to_undirected()

print( "degree of node a : %s" % G.degree("a") )#sommet spécifique
print("degree (undirected) %s" % G.degree()  ) #ensemble des sommets
print ("betweenness centrality %s" % nx.betweenness_centrality(G))
print( "degree (normalized) %s" % nx.degree_centrality(G))

#transformer les mesures en attributs
deg = G.degree()
nx.set_node_attributes(G, 'degree', deg)

#visualisation"""

"""pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

#recherche des cliques
cl = list(nx.find_cliques(G))
print("cliques %s" % cl)

#plus courts chemins
pathlengths=[]

print("source vertex {target:length, }")
for v in G.nodes():
    spl=nx.single_source_shortest_path_length(G,v)
    print('%s %s' % (v,spl))
    for p in spl.values():
        pathlengths.append(p)

print('')
print("plus court chemin moyen %s" % (sum(pathlengths)/len(pathlengths)))

#distribution des plus courts
dist={}
for p in pathlengths:
    if p in dist:
        dist[p]+=1
    else:
        dist[p]=1

print('')
print("length #paths")

print("densité : %s" % nx.density(G))
print("radius : %d" % nx.radius(G))
print("diamètre : %d" % nx.diameter(G))
print("eccentricity: %s" % nx.eccentricity(G))
print("center: %s" % nx.center(G))
print("periphery: %s" % nx.periphery(G))
plt.show()"""
"""df = pd.DataFrame(eval("lire"))

df= nx.Graph()

nx.draw(df)
plt.show()"""
"""x = df['Model']
y = df['Price']
plt.xlabel('Model', fontsize=18)
plt.ylabel('Price($)', fontsize=18)
plt.scatter(x ,y)
plt.splot(x ,y)"""




"""class Pile():
    def __(self):
        self.elements = []
    def push(self,noeud):
        pass
    def countains_noeud(self,name):
        pass
    def empty(self):
        pass
    def remove(self):
        pass
    #test
f=Pile()
f.push("Mamadou")
f.push("Mnsour")
f.push("Dame")
f.push("Khady")
print(f.element)"""
