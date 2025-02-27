## Function resources

[Functions doc](https://www.codecademy.com/resources/docs/python/functions)

# function definition

```terminal
def function_name():
  # functions tasks go here
  # parameters can be input in to the ()
```

# Calling a function

```terminal
def TestFunction():
  print("Test")

TestFunction()
```

# Arguments & parameters

[A & P doc](https://www.codecademy.com/resources/docs/python/functions/arguments-parameters)

The distinction between a parameter and an argument:

- The parameter is the name defined in the parenthesis of the function and can be used in the function body.

- The argument is the data that is passed in when we call the function, which is then assigned to the parameter name.

# Multiple Parameters

We can call multiple parameters. This is an example method:

```terminal
# define multi-parameter function
def my_function(parameter1, parameter2, parameter3):

# Call multi-parameter function
my_function(argument1, argument2)
```

CA example mockup
```terminal
# Write your code below: 

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  return trip_total
# Step 5: call your function
print(calculate_expenses(200, 100, 100, 5))
```
