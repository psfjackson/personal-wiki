## Loops resources

Loops:
https://www.codecademy.com/resources/docs/python/loops

Loop comprehension:
https://www.codecademy.com/resources/docs/python/list-comprehension

Control flow:
https://www.codecademy.com/resources/docs/general/control-flow

# Learning agenda:

- How to write a for loop.
- How to use range in a loop.
- How to write a while loop.
- What infinite loops are and how to avoid them.
- How to control loops using break and continue.
- How to write elegant loops as list comprehensions

# Copy of challenge code:

```terminal
# single digit list
single_digits = list(range(10))

# Empty square list
squares = []

# Squared - loop
for digit in single_digits:
  squares.append(digit**2)
print(squares)

# Cubed - loop comprehension
cubes = [cube**3 for cube in single_digits]
print(cubes)
```
