# Importation
from pyspark import SparkContext, SparkConf

#Instantiation

sparkConf = SparkConf().setAppName("WordCounts").setMaster("local")
sc = SparkContext(conf = sparkConf)



if __name__== '__main__':

    # Importation du fichier
    File = sc.textFile("sample.txt")
    
    # Lecture des mots ligne par ligne, creation des tuples (mot,1), compter le nombre d'occurence de chaque mot (mot,nombre)
    wordCounts = File.flatMap(lambda line: line.split(" ")) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a+b)

    # Afficher le résultat          
    for i in wordCounts.collect():
        print(i)

    # Exportation des resultats dans un fichier texte
    wordCounts.coalesce(1).saveAsTextFile("Resultat.txt")
    # coalesce(1): partitionnement du rdd et répartition de la tâche parmis les coeurs (ici un seul coeur et 1 partition seulement)
    

