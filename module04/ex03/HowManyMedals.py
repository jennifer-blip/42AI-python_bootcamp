import pandas as pd
from pprint import pprint

def how_many_medals(df, name) :
	if not isinstance(df, pd.DataFrame) or not isinstance(name, str):
		return None
	# name = name.lower().capitalize()
	# recuperer les medailles d un athlete
	athlete=df[(df["Name"]==name) & (df["Medal"]!="NA")]
	# recuperer les annees de medailles
	years=athlete["Year"].unique()
	result = {}
	for year in years :
		# construire le resultat de l'annee en cours
		medals=athlete[athlete["Year"]==year]
		G = medals[medals["Medal"]=="Gold"].shape[0]
		S = medals[medals["Medal"]=="Silver"].shape[0]
		B = medals[medals["Medal"]=="Bronze"].shape[0]
		year_result={year:{'G': G, 'S': S, 'B' : B}}
		# ajouter le resultat de l'annee en cours au resultat global
		result.update(year_result)
	pprint(result)