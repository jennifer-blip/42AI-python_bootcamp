class GotCharacter:
	"""Initialize attributes of the parent GotCharacter class"""
	def __init__(self, first_name, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive
	def die (self):
		self.is_alive = False
	def print_house_words(self) :
		print(self.house_words)


class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""
	def __init__(self, first_name=None, is_alive=True):
		"""Initialize attributes of the parent GotCharacter class"""
		# The super function() is a special function that helps Python make connections between the parent and the child class 
		# This line tells Python to call the __init__() method from Stark's parent class
		# The name super comes from a convention of calling the parent class a 'superclass' and the child class a 'subclass'
		super().__init__(first_name=first_name, is_alive=is_alive)
		"""Initialize attributes of the Stark family class"""
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

class Lannister(GotCharacter):
	"""A class representing the Lannister family. Or when good things happen to bad people."""
	def __init__(self, first_name=None, is_alive=True):
		"""Initialize attributes of the parent GotCharacter class"""
		super().__init__(first_name=first_name, is_alive=is_alive)
		"""Initialize attributes of the Stark family class"""
		self.family_name = "Lannister"
		self.house_words = "Hear me roar!"

class Targaryen(GotCharacter):
	"""A class representing the Targaryen family. Or when good people make good things happen with courage and stamina."""
	def __init__(self, first_name=None, is_alive=True):
		"""Initialize attributes of the parent GotCharacter class"""
		super().__init__(first_name=first_name, is_alive=is_alive)
		"""Initialize attributes of the Stark family class"""
		self.family_name = "Targaryen"
		self.house_words = "Fire and blood"	