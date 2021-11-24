'''
Implémenter le parcours en profondeur non recursif entre deux noeuds
Prendre en parametre :
-graphe
-noeud source
-noeud destination
Output :
une liste contenant les noms des noeuds explorés pour aller du noeud source vers le noeud destination 
'''
def ParcoursDFS(mygraph,noeudsource,noeuddestination):
   #Trouver un parcours Dfs en profondeur entre noeuds source et destination
    #Initialisation
    parcours = []
    parcours.append(noeudsource)
    #Parcours en profondeur
    for i in range(len(mygraph[noeudsource])):
        if mygraph[noeudsource][i] == 1:
            if i == noeuddestination:
                parcours.append(i)
                return parcours
            else:
                parcours.append(i)
                return ParcoursDFS(mygraph,i,noeuddestination)
    return parcours
