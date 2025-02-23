## Notes from CA learning


## .insert()
Add elements to a list by index

## .pop()
Remove elements from a list by index

## range()
Generate a numberical range list

## .len()
Get the length of a list

## Slicing
Select portions of a list using slicing syntax

## .count
Count the number of times that an element appears in a list 

## .sort and .sorted
Sort a list of items


## code from lesson
```terminal
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Inventory length
inventory_len = len(inventory)

# First inventory item
first = inventory[0]

# Last inventory item
last = inventory[-1]

# Range from inventory
inventory_2_6 = inventory[2:6]

# First 3 items of inventory
first_3 = inventory[:3]

# Number of 'twin bed' in inventory
twin_beds = inventory.count('twin bed')

# Removing 5th item from the inventory
removed_item = inventory.pop(4)

# Adding '19c Bed Frame' as 11th item in list. 
inventory.insert(10, '19th Century Bed Frame')

# Sort the inventory
inventory.sort()
print (inventory)

# Or stored 
sorted_inventory = sorted(inventory)
print (sorted_inventory)
```