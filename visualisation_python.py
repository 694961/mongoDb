# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:58:46 2022

@author: user
"""

from pymongo import MongoClient
import json
import matplotlib as plt
import numpy as np
import pandas as pd
import networkx as nx
import pandas as pd
from bokeh.plotting import figure, output_file, show

   

db_uri = "mongodb+srv://etudiant:ur2@clusterm1.0rm7t.mongodb.net/"
client = MongoClient(db_uri)
db = client["publications"]

print(db)

#Création de nos conditions dans le aggregate
"""
dico_unwinds = {"$unwind":"$title"}
dico_groups = {"$group":{"_id": {"title":"$title","authors": "$authors"}, "number" : { "$sum ": 1 } }},
dico_sorts = {"$sort": {"number": -1}}
dico_limits = {"$limit": 20}
A = [dico_unwinds, dico_groups, dico_sorts,dico_limits]   

# Notre requête
cursor_aggr = db.hal_irisa_2021.aggregate(A)
rep = list(cursor_aggr)
print(rep)  
                                                
"""

# Création de nos conditions dans le aggregate
dico_unwind = {"$unwind":"$authors"}
dico_group = {"$group":{"_id": "$authors", "number" : { "$sum" : 1 }}}
dico_sort = {"$sort": {"number": -1}}
dico_limit = {"$limit": 20}


l = [dico_unwind, dico_group, dico_sort,dico_limit]

# Notre requête
cursor_aggr = db.hal_irisa_2021.aggregate(l)
reponse = list(cursor_aggr)
print(reponse)
type(reponse)

df = pd.DataFrame(reponse)
print(df)
df.head()

print(df.iloc[0])


# Graphe

# Ajout des nodes

n=['Lefévre Sebastien','Pacchierotti Claudio','Pontonnier Charles',
                   'Guillemot Christin','Busnel Yann','Fromont Elisa', 
                   'Lecuyer Anatole','Jezequel Jean_Marc', 'Ferre Jean Christophe', 'Dumont Georges',
                   'Legeai Fabrice','Olivier Anne-Hélène', 'Pettre Julien', 'Bannier Elise',
                   'Giordano PaoloRobuffo', 'Maumet Camille', 'Martin Arnaud', 'Rubino Gerardo',
                   'Combemale Benoit', 'Maillé Patrick']
G = nx.complete_graph(n)
nx.draw(G, with_labels=True)

f=figure()
f.nx.draw(G, with_labels=True)
output_file("visualisation_pytjon.html")
show(f)
