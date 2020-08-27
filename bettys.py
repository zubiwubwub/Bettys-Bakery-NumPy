import numpy as np

cupcakes = np.array([2, .75, 2, 1, .5])
print(cupcakes)
print("--------------------------------")

recipes = np.genfromtxt("recipes.csv", delimiter=",")
print(recipes)
print("--------------------------------")

eggs = recipes[:,2]
print(eggs)
print("--------------------------------")

uno_egg = recipes[ eggs == 1]
print(uno_egg)
print("--------------------------------")

cookies = recipes[2,:]
print(cookies)
print("--------------------------------")

double_batch = cupcakes * 2
print(double_batch)

grocery_list = double_batch + cookies
print(grocery_list)
print("--------------------------------")
