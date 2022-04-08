import os, pickle

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_recipe(self):
        print(self.name)
        for i in self.ingredients:
            print(f' - {" ".join(["".join(str(j)) for j in i])}')

# with open("recipes.dat") as reader:
#     recipebook = reader.read()

def recipe_names(list):
    for i, recipe in enumerate(list):
        print(f"{i+1}. {recipe.name}")

def add(recipe_list):
    # global recipe_list
    name = input("Recipe name: ")
    ingredients = []
    while True:
        ingredient = []
        ingr = input("Ingredient: ")
        print("Please enter values as a decimal.")
        qty = float(input("Quantity: "))
        unit = input("Unit: ")
        ingredient.append(qty)
        ingredient.append(unit)
        ingredient.append(ingr)
        ingredients.append(ingredient)
        exit = input("Add another ingredient? (yes/no): ")
        if exit == "no":
            break
        else:
            continue
    new_recipe = Recipe(name, ingredients)
    recipe_list.append(new_recipe)

def view_recipe(recipe, recipe_list):
    if recipe.isdigit():
        recipe = int(recipe)
    if isinstance(recipe, int):
        if recipe > len(recipe_list):
            print("Recipe not found.")
        else:
            recipe_list[recipe - 1].print_recipe()
    elif isinstance(recipe, str):
        for i in recipe_list:
            if recipe.lower() == i.name.lower():
                i.print_recipe()
                break
        else:
            print("Recipe not found.")

def ingredient_search(ingredient, recipe_list):
    count = 0
    for recipe in recipe_list:
        # found = False
        for index, ingr in enumerate(recipe.ingredients):
            if ingredient.lower() in recipe.ingredients[index][2].lower():
                # found = True
                count += 1
                print(recipe.name)
                break
    if count == 0:
        print("Ingredient not found.")

def increase_recipe(recipe, recipe_list):
    multiply = int(input("How many times do you want to increase the recipe? "))
    increased_recipe = recipe
    for index, ingredient in enumerate(increased_recipe.ingredients):
        increased_recipe.ingredients[index][0] = multiply * increased_recipe.ingredients[index][0]
    increased_recipe.print_recipe()

def menu():
    recipe_list = initialize()
    while True:
        os.system("clear")
        print("Recipe Book Menu Options")
        print("""
        1. View Recipe List
        2. Add Recipe
        3. View a Recipe
        4. Search by Ingredient
        5. Increase Recipe Quantity
        6. Exit
              """)
        while True:
            try:
                option = int(input("Make a selection: "))
                break
            except ValueError:
                print()
                print("Please enter the integer value for the menu item you want to select")
                print()

        if option == 1:
            recipe_names(recipe_list)
            print()
            print("Press 'enter' to continue")
            input()
        elif option == 2:
            add(recipe_list, recipe_list)
        elif option == 3:
            recipe_names(recipe_list)
            print()
            recipe = input("Which recipe do you want to see? ")
            view_recipe(recipe, recipe_list)
            print()
            print("Press 'enter' to continue")
            input()
        elif option == 4: 
            ingredient = input("Which ingredient do you want to find? ")
            ingredient_search(ingredient, recipe_list)
            print()
            print("Press 'enter' to continue")
            input()
        elif option == 5:
            recipe_names(recipe_list)
            print()
            recipe = int(input("Which recipe number do you want to multiply? "))
            recipe = recipe_list[recipe - 1]
            increase_recipe(recipe, recipe_list)
            print()
            print("Press 'enter' to continue")
            input()
        elif option == 6:
            with open("recipes.dat", "wb") as f:
                pickle.dump(recipe_list, f)
            break
        else: 
            print("That is not a valid menu option.")
            print()
            print("Press 'enter' to continue")
            input()


# recipe_1 = Recipe(
#     "PB&J",
#     [[2, "slices", "bread"], [4, "tablespoons", "smooth peanut butter"],
#      [2, "tablespoons", "strawberry jelly"]])

# recipe_2 = Recipe("Ramen Noodles",
#                   [[1, "package", "instant noodles"],
#                    [1, "packet", "seasoning"], [2, "cups", "water"]])

# recipe_3 = Recipe("Macaroni and cheese",
#                   [[1, "cup", "macaroni"],
#                    [2, "cups", "water"], [1, "cup", "shredded cheese"]])

# recipe_list = [recipe_1, recipe_2, recipe_3]



# dump = (recipe_list, get_file)

"""
0. Remove lines 13-14
1. Open the recipes.dat file and pickle.dump the list into it
2. Comment out/delete the code once we have our list data in the recipes.dat file
"""
# with open("recipes.dat", "wb") as f:
#     pickle.dump(recipe_list, f)

"""
3. Comment out/delete all of the code we used to setup our recipes
"""

"""
4. Create the initialize function below and add the function call inside the menu function and save it to recipe_list
"""
def initialize():
    with open("recipes.dat", "rb") as f:
        recipe_list = pickle.load(f)
    return recipe_list

"""
5. Modify the add function and pass recipe_list as a parameter to all the functions that need it; remove the global recipe_list
"""

"""
6. Fix search by ingredient function; change found = False to a count = 0
"""

"""
7. Add the pickle.dump code in the Exit option before exiting the program to save the recipe data
"""