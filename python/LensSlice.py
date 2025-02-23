# CA Project - testing learnings on lists and functions in Python.

# List of toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olivers', 'anchovies', 'mushrooms']

# Pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# print(len(prices))

# Number of $2 pizza slices
num_two_dollar_slices = prices.count(2)

# Lenth of pizza toppings list
num_pizzas = len(toppings)

# Statement on number of pizza types on sale
print ('We sell', str(num_pizzas), 'different kinds of pizza!')

# Combining in to a 2D list
pizza_and_prices = list(zip(prices, toppings))
print ('')
print (pizza_and_prices)

# Sorting pizzas by cost
pizza_and_prices.sort()
print ('')
print (pizza_and_prices)

# Cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# Most expensive pizza
priciest_pizza = pizza_and_prices[-1]

# Most expensive is now sold out
pizza_and_prices.pop()

# Adding Peppers topping, and sorting
pizza_and_prices.insert(0, (2.5, 'peppers'))
pizza_and_prices.sort()
print ('')
print (pizza_and_prices)

# Three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print ('')
print (three_cheapest)
