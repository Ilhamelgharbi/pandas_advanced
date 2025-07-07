import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Partie 1 : Chargement et exploration du dataset

# Charger le fichier employees2.csv dans un DataFrame Pandas
df = pd.read_csv("employees2.csv")
print("Données brutes :\n", df, "\n")

# Afficher les premières lignes du DataFrame
print("Premières lignes du DataFrame :\n", df.head(), "\n")

# Vérifier les types de données de chaque colonne
print("Types de données par colonne :\n", df.dtypes, "\n")

# Identifier les valeurs manquantes par colonne
print("Valeurs manquantes par colonne :\n", df.isnull().sum(), "\n")

# Partie 2 : Nettoyage des données

# Remplacer les valeurs manquantes dans la colonne Age par la médiane de cette colonne
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
print(f"Médiane d'âge utilisée : {median_age}")

# Remplir les valeurs manquantes dans Salaire en utilisant la moyenne par département
df["Salary"] = df.groupby("Department")["Salary"].transform(lambda x: x.fillna(x.mean()))
print("Salaire moyen par département utilisé pour remplissage :")
print(df.groupby("Department")["Salary"].mean(), "\n")

# Convertir toutes les colonnes numériques en type approprié (float ou int)
df["Age"] = df["Age"].astype(int)
df["Years_Experience"] = df["Years_Experience"].astype(int)
df["Salary"] = df["Salary"].astype(float)

# Remplacer les valeurs 'Yes'/'No' dans Remote par 'Oui'/'Non'
df["Remote"] = df["Remote"].replace({"Yes": "Oui", "No": "Non"})

# Créer une nouvelle colonne Ancienneté_Catégorie qui classe les années d’expérience
conditions = [
    df["Years_Experience"] < 3,
    df["Years_Experience"].between(3, 7),
    df["Years_Experience"].between(8, 15),
    df["Years_Experience"] > 15
]
categories = ["Junior", "Intermédiaire", "Senior", "Expert"]
df["Ancienneté_Catégorie"] = np.select(conditions, categories, default="Non classifié")

print("Données après nettoyage :\n", df, "\n")

# Partie 3 : Analyses exploratoires et statistiques

# Calculer le salaire moyen global
salaire_moyen = df["Salary"].mean()
print("Salaire moyen global :", salaire_moyen)

# Trouver l’employé(e) avec le salaire le plus élevé
print("Employé avec le salaire le plus élevé :\n", df[df["Salary"] == df["Salary"].max()])

# Calculer le salaire moyen par département
print("Salaire moyen par département :\n", df.groupby("Department")["Salary"].mean())

# Calculer la moyenne et la médiane des salaires par groupe d’ancienneté
print("Moyenne et médiane des salaires par groupe d’ancienneté :\n", df.groupby("Ancienneté_Catégorie")["Salary"].agg(["mean", "median"]))

# Compter combien d’employés travaillent en télétravail (Remote) par département
print("Nombre d’employés en télétravail par département :\n", df[df["Remote"] == "Oui"].groupby("Department")["Remote"].count())

# Partie 4 : Tableaux croisés dynamiques (pivot tables)

# Créer un tableau croisé dynamique montrant le salaire moyen par département et par télétravail
pivot_salaire = df.pivot_table(values="Salary", index="Department", columns="Remote", aggfunc="mean")
print("Salaire moyen par département et mode de travail :\n", pivot_salaire)

# Créer un autre tableau croisé dynamique montrant le nombre moyen d’années d’expérience par groupe d’âge et par département
df["Tranche_Age"] = pd.cut(df["Age"], bins=[20, 30, 40, 50, 60, 70], labels=["20-30", "30-40", "40-50", "50-60", "60-70"])
pivot_experience = df.pivot_table(values="Years_Experience", index="Tranche_Age", columns="Department", aggfunc="mean")
print("Années d'expérience moyennes par tranche d'âge et département :\n", pivot_experience)

# Partie 5 : Calculs avancés avec NumPy

# Utiliser np.where() pour créer une colonne Performance
df["Performance"] = np.where(
    df["Salary"] < 60000, "Bon",
    np.where(df["Salary"] < 80000, "Moyen", "Haut")
)

# Utiliser np.select() pour classer les employés selon leur âge et leur ancienneté
conditions_age_experience = [
    (df["Age"] < 40) & (df["Years_Experience"] < 5),
    (df["Age"] < 40) & (df["Years_Experience"] >= 5),
    (df["Age"] >= 40) & (df["Years_Experience"] < 5),
    (df["Age"] >= 40) & (df["Years_Experience"] >= 5)
]
choices_age_experience = ["Jeune & Nouveau", "Jeune & Expérimenté", "Senior & Nouveau", "Senior & Expérimenté"]
df["Profil_Age_Exp"] = np.select(conditions_age_experience, choices_age_experience, default="Non classifié")
print("Colonne Profil_Age_Exp ajoutée :\n", df["Profil_Age_Exp"].value_counts(), "\n")

# Calculer la différence entre le salaire de chaque employé et le salaire moyen de son département
df["Diff_Salaire_Dept"] = df["Salary"] - df.groupby("Department")["Salary"].transform("mean")

# Partie 6 : Visualisation (Bonus)

# Afficher la distribution des salaires
plt.figure(figsize=(6, 4))
sns.histplot(df["Salary"], bins=20, kde=True)
plt.title("Distribution des salaires")
plt.xlabel("Salaire")
plt.ylabel("Nombre d'employés")
plt.tight_layout()
plt.show()

# Comparer les salaires moyens par département sous forme de barplot
plt.figure(figsize=(6, 4))
sns.barplot(x=df.groupby("Department")["Salary"].mean().index, y=df.groupby("Department")["Salary"].mean().values)
plt.title("Salaires moyens par département")
plt.xlabel("Département")
plt.ylabel("Salaire moyen")
plt.tight_layout()
plt.show()

# Boxplot des salaires par groupe d’ancienneté
plt.figure(figsize=(6, 4))
sns.boxplot(x="Ancienneté_Catégorie", y="Salary", data=df)
plt.title("Boxplot des salaires par ancienneté")
plt.tight_layout()
plt.show()
