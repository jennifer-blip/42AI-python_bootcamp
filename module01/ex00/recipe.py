import sys

class Recipe :
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description="") :
		"""initialiaze recipe attributes"""
		if name == "" :
			raise ValueError("ERROR : name cannot be empty")
		if not isinstance(name, str) :
			raise ValueError(f"{name} : name must be a string")
		self.name = name
		try :
			self.cooking_lvl = int(cooking_lvl)
		except ValueError :
			raise ValueError("ERROR : cooking_lvl must be an integer")
		if self.cooking_lvl not in range (1, 11) :
			raise ValueError("ERROR : cooking_lvl is out of (1, 11) range")
		try :
			self.cooking_time = int(cooking_time)
		except ValueError :
			raise ValueError("ERROR : cooking_time must be an integer")
		if ingredients == "" :
			raise ValueError("ERROR : ingredients cannot be empty")
		if not isinstance(ingredients, list) :
				raise ValueError(f"{ingredients}: ingredients must be a list of strings")
		for x in ingredients :
			if not isinstance(x, str) :
				raise ValueError(f"{x}: each ingredient must be a string")
		self.ingredients = ingredients
		if not isinstance(description, str) :
			raise ValueError(f"{description} description must be a string")
		self.description = description
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert" :
			raise ValueError(f"ERROR: {recipe_type} recipe_type is not one of 'starter', 'lunch' or 'dessert' type")
		self.recipe_type = recipe_type
	
	def __str__(self):
		"""Returns the string to print with the recipe's info"""
		return "\n".join([
			self.name,
			f'cooking level = {self.cooking_lvl}',
			f'cooking time = {self.cooking_time}',
			f'ingredients = {", ".join(self.ingredients)}',
			f'recipe type = {self.recipe_type}',
			f'description = {self.description}'
			])