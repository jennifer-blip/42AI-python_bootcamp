import pandas as pd

class FileLoader:
	def __init__(self):
		pass

	def load(self, path): 
		"""takes as an argument the file path of the dataset to load,
		displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
		returns the dataset loaded as a pandas.DataFrame."""
		if not isinstance(path, str):
			return None
		# data = pd.read_csv(path, sep=';')
		data = pd.read_csv(path)
		print(f"Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}")
		return data
		
	def display(self, df, n): 
		"""takes a pandas.DataFrame and an integer as arguments,
		displays the first n rows of the dataset if n is positive, or the last n rows if n is
		negative."""
		if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
			return None
		if n > 0:
			print(df.head(n))
		else:	
			print(df.tail(-n))