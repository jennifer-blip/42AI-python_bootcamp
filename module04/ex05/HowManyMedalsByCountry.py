import pandas as pd
from pprint import pprint

# team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

def how_many_medals_by_country(df, country) :
	"""returns a dictionary of dictionaries giving the number and types of medals
	for each competition where the country delegation earned medals"""
	if not isinstance(df, pd.DataFrame) or not isinstance(country, str) :
		return None
	country = country.lower().capitalize()
	result={}
	cl=df[(df["Team"]==country) & (df["Medal"]!="N/A")]
	years=cl["Year"].unique()
	team_sports=df["Sport"].unique()
	for year in years :
		Y = year
		G = 0
		S = 0
		B = 0
		for ts in team_sports :
			G += cl[(cl["Year"]==year) & (cl["Sport"]==ts) & (cl["Medal"]=="Gold")]["Event"].nunique()
			S += cl[(cl["Year"]==year) & (cl["Sport"]==ts) & (cl["Medal"]=="Silver")]["Event"].nunique()
			B += cl[(cl["Year"]==year) & (cl["Sport"]==ts) & (cl["Medal"]=="Bronze")]["Event"].nunique()
			year_total={year:{'G': G, 'S': S, 'B': B}}
		result.update(year_total)
	return result


	
