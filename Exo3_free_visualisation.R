library(mongolite)
library(plotly)


url="mongodb://etudiant:ur2@clusterm1-shard-00-00.0rm7t.mongodb.net:27017,clusterm1-shard-00-01.0rm7t.mongodb.net:27017,clusterm1-shard-00-02.0rm7t.mongodb.net:27017/?ssl=true&replicaSet=atlas-l4xi61-shard-0"
mdb = mongo(collection="NYfood", db="food",
             url=url,
             verbose=TRUE)
mdb


############
#Quels sont les 10 restaurants (nom, quartier, addresse et score) avec le plus grand score moyen ?
############
qry='[ { "$unwind": "$grades" },
  { "$group": { 
    "_id": { "na": "$name", "id": "$restaurant_id", 
      "bo": "$borough",
    "sc": { "$avg": "$grades.score" }
  }},
  { "$sort": { "sc": -1 }},
  { "$limit": 10 },
  { "$project": {
    "_id": 0,
    "name": "$_id.na",
    "address": { "$concat": [ 
      "$_id.ad.building", " ", "$_id.ad.street", ", ", "$_id.bo"
    ]},
    "score": "$sc"
  }}


          
  ]'

#visualisation : 

resta <- mdb$aggregate(pipeline = qry)
plot<-plot_ly(x = ~resta$name, y = ~resta$score, color = ~resta$address) %>% 
  layout(title = "Top 10 des  restaurants avec le plus grand score moyen", xaxis = list(title = "noms de
            "), yaxis = list(title = "score_moyen"), barmode = 'stack')  




