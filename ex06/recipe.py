bocadillo = {
	'ingredients': ['jamón', 'pan', 'queso', 'tomate'],
	'meal': 'almuerzo',
	'prep_time': 10
}
tarta = {
	'ingredients': ['harina', 'azúcar', 'huevos'],
	'meal': 'postre',
	'prep_time': 60
}
ensalada = {
	'ingredients': ['aguacate', 'rúcula', 'tomates', 'espinacas'],
	'meal': 'almuerzo',
	'prep_time': 15
}
cookbook = {
	'bocadillo': bocadillo,
	'tarta': tarta,
	'ensalada': ensalada
}

def printRecipeNames():
	names = list(cookbook.keys())
	print(names)

def printRecipeDetails():
	recipeName = input("Enter the name of the recipe:\n")
	recipeDetails = cookbook[recipeName]
	print(f'Recipe for {recipeName}:')
	print(f'\tIngredients list: {recipeDetails["ingredients"]}.')
	print(f'\tTo be eaten for {recipeDetails["meal"]}.')
	print(f'\tTakes {recipeDetails["prep_time"]} minutes of cooking.')

def deleteRecipe():
	recipeName = input("Enter the name of the recipe:\n")
	del cookbook[recipeName]

def addRecipe():
	name = input('Enter a name:\n')
	ingredients = []
	print("Enter ingredients:")
	while True:
		s = input();
		if not s:
			break
		ingredients.append(s)
	meal = input("Enter a meal type:\n")
	prepTime = input("Enter a preparation time:\n")
	newRecipe = {
		'ingredients': ingredients,
		'meal': meal,
		'prep_time': prepTime
	}
	cookbook[name] = newRecipe

print("Welcome to the Python Cookbook !")

while True:
	print("List of available options:")
	print("\t 1: Add a recipe")
	print("\t 2: Delete a recipe")
	print("\t 3: Print a recipe")
	print("\t 4: Print the cookbook")
	print("\t 5: Quit")
	print("")
	print("Please select an option:")
	option = int(input())
	if option == 1:
		addRecipe()
	elif option == 2:
		deleteRecipe()
	elif option == 3:
		printRecipeDetails()
	elif option == 4:
		printRecipeNames()
	elif option == 5:
		print("")
		break
	else:
		print("Sorry, this option does not exist")
	print("")

print("Cookbook closed. Goodbye !")