import sys
from recipe import Recipe
from book import Book

my_cookbook = Book("my_cookbook")
try :
	recipe1 = Recipe(
    "tomato soup",
    2,
    20,
    ["tomatoes", "onion", "garlic", "vegetable broth"],
    "starter",
    "asjkdhqwe"
	)
	recipe2 = Recipe(
    "Caesar Salad",
    3,
    15,
    ["lettuce", "croutons", "parmesan", "chicken", "caesar dressing"],
    "starter",
	"too much Caesar salad is no good for health"
)

	recipe3 = Recipe(
    "Bruschetta",
    2,
    10,
    ["bread", "tomatoes", "basil", "olive oil", "garlic"],
    "starter",
	"don't eat too much bread"
)

	recipe4 = Recipe(
    "Spaghetti Bolognese",
    4,
    60,
    ["spaghetti", "ground beef", "tomato sauce", "onion", "carrot"],
    "lunch",
	"add some vegetable and it is perfect"
)

	recipe5 = Recipe(
    "Chicken Curry",
    5,
    50,
    ["chicken", "coconut milk", "curry paste", "rice"],
    "lunch",
	"I love curry"
)

	recipe6 = Recipe(
    "Grilled Salmon",
    4,
    25,
    ["salmon", "lemon", "olive oil", "asparagus"],
    "lunch",
	"the best recipe ever"
)

	recipe7 = Recipe(
    "Chocolate Cake",
    5,
    70,
    ["flour", "eggs", "butter", "cocoa powder", "sugar"],
    "dessert",
	"I don't like chocolate but my friends do"
)

	recipe8 = Recipe(
    "Apple Pie",
    4,
    80,
    ["apples", "flour", "butter", "sugar", "cinnamon"],
    "dessert",
	"delicious"
)

	recipe9 = Recipe(
    "Vanilla Ice Cream",
    3,
    240,
    ["milk", "cream", "vanilla", "sugar"],
    "dessert",
	"fresh and perfect for summer time"
)

except ValueError as e:
	print(f"Error: {e}")
	sys.exit(1)
try :
	my_cookbook.add_recipe(recipe1)
	my_cookbook.add_recipe(recipe2)
	my_cookbook.add_recipe(recipe3)
	my_cookbook.add_recipe(recipe4)
	my_cookbook.add_recipe(recipe5)
	my_cookbook.add_recipe(recipe6)
	my_cookbook.add_recipe(recipe7)
	my_cookbook.add_recipe(recipe8)
	my_cookbook.add_recipe(recipe9)
except ValueError as e:
	print(f"Error: {e}")
	sys.exit(1)
print("---------Recipe str method----------")
to_print = str(recipe1)
print(to_print)
print ("-------cookbook creation date------")
print(my_cookbook.creation_date)
print ("-------cookbook last update------")
print(my_cookbook.last_update)
print ("-------cookbook get recipes by types------")
print (f"starter recipes : {my_cookbook.get_recipes_by_types('starter')}")
print (f"lunch recipes: {my_cookbook.get_recipes_by_types('lunch')}")
print (f"dessert recipes : {my_cookbook.get_recipes_by_types('dessert')}")
print ("-------cookbook get recipe by name------")
print (str(my_cookbook.get_recipe_by_name('Chocolate')))
