import pandas as pd

def proportion_by_sport(df, year, sport, gender) :
	"""returns a float corresponding to the proportion (percentage) of participants
	who played the given sport among the participants of the given gender. "What was the percentage of female
	basketball players among all female participants in the 2016 Olympics?" """
	if not isinstance(df, pd.DataFrame) or not year in range(1896, 2025) or not isinstance(sport, str) or not gender in ("F", "M") :
		return None
	data=df[(df['Year']== year) & (df['Sex']==gender)]
	sport = sport.capitalize()
	if not data.empty :
		total = data.drop_duplicates(subset="Name").shape[0]
		nb = data[data["Sport"]==sport].drop_duplicates(subset="Name").shape[0]
		return 100 * nb/total
	else :
		print(f"No Olympic Games this year ({year}), please choose another year")
	
