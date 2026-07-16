import sys

cookbook = {
	'Sandwich' : {
		'ingredients' : {'ham', 'bread', 'cheese', 'tomatoes'}, 
		'meal' : 
		'lunch', 
		'prep_time' : 10 
		},
	'Cake' : {
		'ingredients' : {'flour', 'sugar', 'eggs'}, 
		'meal' : 'dessert', 
		'prep_time' : 60 
		}, 
	'Salad' : {
		'ingredients' : {'avocado', 'arugula', 'tonatoes', 'spinach'}, 
		'meal' : 'lunch', 
		'prep_time' : 15
		},
	'test1' : {
		'ingredients' : {'test1', 'test1', 'test1', 'test1'}, 
		'meal' : 'test1', 
		'prep_time' : 15
		},
	'test2' : {
		'ingredients' : {'test2', 'test2', 'test2', 'test2'}, 
		'meal' : 'test2', 
		'prep_time' : 15
		}
}


def recipeName() :
	# for recipe in cookbook.values():
	# 	print ( "{}".format(recipe))
	print ( *cookbook.keys(), sep= ', ')

def recipeDetails(name) :
	status = 0
	for x, obj in cookbook.items():
		if x == name :
			print(x)
			for y in obj :
				print(y + ':', obj[y])
				status = 1
	if status == 0 :
		print ("unable to print details, recipe not found : ", name)

def recipeDelete(name) :
	status = 0
	for x, obj in cookbook.items():
		if x == name :
			cookbook.pop(x)
			recipeName()
			status = 1
			break
	if status == 0 :
		print ("unable to delete, recipe not found : ", name)

def recipeAdd() :
	newRecipe = input("Enter new recipe name : ")
	ingredients = input ("Enter ingredients : ")
	meal = input ("Enter a meal : ")
	prep_time = input ("Enter a preparation time : ")
	cookbook.update({newRecipe : {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}})
	print ("recipe successfully added to cookbook : ", newRecipe)

print("Welcome to the Python Cookbook ! \n \
		List of available options : \n \
		1: Add a recipe \n \
		2: Delete a recipe \n \
		3: Print a recipe \n \
		4: Print the cookbook \n \
		5: Quit")
while True :
	result = input ("Please select an option : ")
	if result == '1' :
		recipeAdd()
	elif result == '2' :
		rem = input("Please enter a recipe name to delete : ")
		recipeDelete(rem)
	elif result == '3' :
		recipe = input("Please enter a recipe name to print : ")
		recipeDetails(recipe)
	elif result == '4' :
		recipeName()
	elif result == '5' :
		break
