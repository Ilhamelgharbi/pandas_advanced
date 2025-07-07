import pandas as pd
import numpy as np
columns=["Nom", "Âge", "Ville"]
# Liste des données
data=[
    ["Amine", 28, "Casablanca"],
    ["Lina", 22, "Rabat"],
    ["Youssef", 35, "Fès"],
    ["Salma", 30, "Casablanca"],
    ["Nora", np.nan, "Tanger"]
]

# Créer un DataFrame avec 3 colonnes : Nom, Âge, Ville
df = pd.DataFrame(data, columns=columns)

# Afficher les 10 premières lignes avec head()
print("Les 10 premières lignes:")
print(df.head(n:=3))
# Afficher la structure du DataFrame avec info()
print("\nStructure du DataFrame:" )
df.info()

# Afficher des statistiques descriptives avec describe()
print("\nStatistiques descriptives:")
print(df.describe())


# challenge 2
# Afficher les valeurs uniques de la colonne "Ville"
print("La colonne Ville contient les valeurs uniques suivantes :")
print(df["Ville"].unique())

# Afficher les valeurs age sup de 25 ans
print("Les personnes de plus de 25 ans:")
print(df[df["Âge"] > 25])

# Afficher les nom et la ville des personnes de casa 
print("\nLes personnes de Casablanca:")
print(df[df["Ville"] == "Casablanca"][["Nom", "Ville"]])

#Challenge 3 : Ajout et modification de colonnes
# Ajouter une colonne "date de naissance" avec la valeur "Maroc" pour toutes les lignes
df["date de naissance"] = 2025 - df["Âge"]
print(df)
# Modifier les nom majuscule 
df["Nom"] = df["Nom"].str.upper()
print(df)
# renome une colonne 
df.rename(columns={"Ville": "Localisation"}, inplace=True)
print("\nDataFrame après renommage de la colonne 'Ville' en 'Localisation':")
print(df)
#Challenge 4 : Gestion des valeurs manquantes
# remplacer lesvaleurs d age manquantes manuellemnt
print("\nDataFrame avant remplacement des valeurs manquantes:")
df.loc[2, "Âge"] = np.nan
print(df)
#Affiche les lignes contenant des valeurs manquantes avec isnull().
print("\nLignes contenant des valeurs manquantes:")
print(df[df.isnull().any(axis=1)])

# Remplace les valeurs manquantes par la moyenne des âges avec fillna().
df["Âge"].fillna(df["Âge"].mean(), inplace=True)
print("\nDataFrame après remplacement des valeurs manquantes:")
print(df)

# Challenge 5 : Tri et suppression
#Trie les lignes par âge décroissant avec sort_values(by='Âge', ascending=False)
df.sort_values(by='Âge', ascending=False, inplace=True)
print("\nDataFrame trié par âge décroissant:")
print(df)
#Supprime la colonne Année de Naissance avec drop().
df.drop(columns=["date de naissance"], inplace=True)
print("\nDataFrame après suppression de la colonne 'date de naissance':")
print(df)
#Supprime la première ligne du DataFrame avec drop(index=0).
df.drop(index=0, inplace=True)
print("\nDataFrame après suppression de la première ligne:")
print(df)