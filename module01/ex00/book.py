import time
from datetime import datetime, date
from recipe import Recipe


class Book :
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.now()
		self.creation_date = date.today()
		self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for key, value in self.recipes_list.items() :
			for x in value :
				if name == x.name :
					print(f"{name}")
					return (x)
		print(f"{name} recipe does not exist in the {self.name} cookbook")

	def get_recipes_by_types(self, recipe_type):
		"""Gets all recipes names for a given recipe_type """
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert" :
			raise ValueError (f"{recipe_type} is not one of 'starter', 'lunch' or 'dessert' type")
		return ", ".join(x.name for x in self.recipes_list[recipe_type])
	
	def add_recipe(self, recipe):
		"""Adds a recipe to the book and updates last_update"""
		if not isinstance(recipe, Recipe) :
			raise ValueError(f"ERROR: {recipe} recipe does not exist")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now()
