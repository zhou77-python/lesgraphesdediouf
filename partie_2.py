class Noeud:
    #un noeud a un nom ,des attributs sous forme de dictionnaire avec comme cle : une liste de coordonnes (latitude, longitude), la taille de la population
    #la liste des voisins sera initialisée à la creation des arcs dans le graphe
    def __init__(self, name):
        self.name = name
        self.attributs = {}
        self.listNomvoisin = []
    
    def setAttributs(self,key,values):
        self.attributs[key]=values
    def getAttributs(self,key):
        return self.attributs[key]
    def getName(self):
        return self.name
    '''Deux noeud sont egaux s'ils ont les memes noms'''
    def egale(self,noeud):
        return self.name == noeud.getName()
    #Dans le fichier transport-relationships.csv,on a la cle "cost" recuperer sa valeur la plus petite
    def getCout(self):
        return min(self.attributs['cost'])
    #recuperer le cout d'un noeud donner en parametre 
    def getCostNoeud(self,noeud):
        return self.attributs['cost'][self.listNomvoisin.index(noeud)]