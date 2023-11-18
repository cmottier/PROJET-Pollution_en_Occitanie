#%%

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#Extrait des données pour Mtp Près d'Arènes et NO2 - Données téléchargées

Mtp = pd.read_csv("Donnees_pour_test.csv")
Mtp_PA_NO2 = Mtp.loc[(Mtp["nom_station"]=="Montpellier - Prés d Arènes Urbain") & (Mtp["nom_poll"]=="NO2"),["valeur","date_debut"]]
Date = Mtp_PA_NO2["date_debut"]
Releve = Mtp_PA_NO2["valeur"]


# Création du DatFrame

data = {
    'Date': Date,
    'Valeur1': Releve
}
df = pd.DataFrame(data)
df = df.sort_values(by=['Date'], ascending=[True])
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d %H:%M:%S%z')

# Création du graphique avec les dates en abscisse et les valeurs en ordonnée

plt.figure(figsize=(20, 6))
plt.plot(df['Date'], df['Valeur1'], label='Valeur1',ls='-')

# Spécifiez les emplacements des ticks (ici, tous les jours)
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Faites pivoter les labels des dates pour une meilleure lisibilité
plt.xticks(rotation=45)

# Ajouter des étiquettes aux axes et un titre
plt.xlabel('Dates')
plt.ylabel('Relevé (en $\mu g/m^3$)')
plt.title('Concentration en $NO_2$ - Montpellier Près d\'Arènes')

# Afficher le graphique
plt.tight_layout()
plt.show()

# %%