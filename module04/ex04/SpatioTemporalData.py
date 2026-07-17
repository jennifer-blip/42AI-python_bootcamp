import pandas as pd
from pprint import pprint

class SpatioTemporalData:
	def __init__ (self, df):
		if not isinstance(df, pd.DataFrame) :
			return None
		self.df=df
	def when(self, location):
		"""takes a location as an argument and returns a list containing the
		years where games were held in the given location"""
		if not isinstance(location, str) :
			return None
		location=location.lower().capitalize()
		location=self.df[self.df["City"]==location]
		pprint (location["Year"].unique().tolist())
		

	def where(self, date): 
		"""takes a date as an argument and returns the location where the
		Olympics took place in the given year"""
		if not date in range(1896, 2025) :
			return None
		year=self.df[self.df["Year"]==date]
		pprint (year["City"].unique().tolist())
		