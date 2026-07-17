import pandas as pd
from datetime import datetime

def youngest(df, sex) :
	"""The function returns a dictionary containing the age of the youngest"""
	return df[df['Sex']== sex]["Age"].min()
	# woman = df[df['Sex']== sex]
	# idx = woman["Age"].idxmin()
	# row = woman.loc[idx]
	# ou encore:
	# row = df[df["Sex"] == "F"].loc[df[df["Sex"] == "F"]["Age"].idxmin()]
	# puis:
	# row.to_dict()
		
def youngest_fellah(df, year) :
	"""The function returns a dictionary containing the age of the youngest woman and man
	who took part in the Olympics on that year."""
	if not isinstance(df, pd.DataFrame) or not  year in range(1896, 2025) :
		return None
	y=df[df['Year']== year]
	if not y.empty :
		youngest_f=youngest(y, "F")
		youngest_m=youngest(y, "M")
		return {'F':youngest_f, 'M':youngest_m}
	else :
		print(f"No Olympic Games this year ({year}), please choose another year")

	