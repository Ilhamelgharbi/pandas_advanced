# Exercice : Analyse des employés d'une entreprise tech

import pandas as pd
import numpy as np

# Partie 1 : Chargement et exploration
# 1. Charger employees2.csv
df = pd.read_csv("employees2.csv")
# 2. Afficher les 5 premières lignes
print( "les 5 premières lignes sont \n:", df.head() , "\n")
# 3. Vérifier types de données
print("Les types de données sont \n:", df.dtypes, "\n")
# 4. Identifier valeurs manquantes
print("Les valeurs manquantes sont \n:", df.isnull().sum(), "\n")

# Partie 2 : Nettoyage des données
# 5. Remplacer Age manquant par médiane
df['Age'] = df['Age'].fillna(df['Age'].median())
print("Après remplacement des âges manquants par la médiane :\n", df['Age'], "\n")
# 6. Remplacer Salaire manquant par moyenne par département
df['Salary'] = df['Salary'].fillna(df.groupby('Department')['Salary'].transform('mean'))
print("Après remplacement des salaires manquants par la moyenne par département :\n", df['Salary'], "\n")
# 7. Convertir colonnes numériques
numeric_cols = ['Age', 'Salary', 'Years_Experience']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

print("Types après conversion :\n", df.dtypes, "\n")

# 8. Remplacer Yes/No par Oui/Non dans Remote
df['Remote'] = df['Remote'].replace({'Yes': 'Oui', 'No': 'Non'})

print("Valeurs Remote après remplacement :\n", df['Remote'].value_counts(), "\n")
# 9. Créer colonne Ancienneté_Catégorie (Junior/Intermédiaire/Senior/Expert)
def classer_anciennete(x):
    if x < 3:
        return 'Junior'
    elif 3 <= x <= 7:
        return 'Intermédiaire'
    elif 8 <= x <= 15:
        return 'Senior'
    else:
        return 'Expert'

df['Ancienneté_Catégorie'] = df['Years_Experience'].apply(classer_anciennete)
print("Catégories d'ancienneté :\n", df['Ancienneté_Catégorie'].value_counts(), "\n")
# Partie 3 : Analyses statistiques
# 10. Salaire moyen global
# 11. Employé avec salaire le plus élevé
# 12. Salaire moyen par département
# 13. Moyenne/médiane par groupe d'ancienneté
# 14. Nombre employés en télétravail par département

# Partie 4 : Tableaux croisés dynamiques
# 15. Salaire moyen par département et télétravail
# 16. Années d'expérience par âge et département

# Partie 5 : Calculs avancés NumPy
# 17. Colonne Performance avec np.where()
# 18. Classification âge/ancienneté avec np.select()
# 19. Différence salaire vs moyenne département

# Partie 6 : Visualisation (Bonus)
# 20. Distribution salaires, barplot départements, boxplot ancienneté

