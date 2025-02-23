## Loops resources

[Loops](https://www.codecademy.com/resources/docs/python/loops)

[Loop comprehension](https://www.codecademy.com/resources/docs/python/list-comprehension)

[Control flow](https://www.codecademy.com/resources/docs/general/control-flow)

[Loop CA review notes](https://www.codecademy.com/practice/tracks/cscj-22-fundamentals-of-python/modules/cscj-22-python-loops?source=syllabus)

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

# Accessing sublists

Example

```terminal
grouped_topics = [["Algorithms", "Data Structures", "AI"], ["Linear Regression", "SQL"]]

for sublist in grouped_topics:
  for sublist_element in sublist: 
    print(sublist_element)  
```
# Loop text search 

Example

```terminal
list_of_accessories = ["Signpost", "Sculpture", "Gauge", "Feeder"]
for item in list_of_accessories:
  if item == "Gauge":
    continue
  print(item)
```
