## Notes from CA learning


## .insert()
Add elements to a list by index

```terminal
# insert an item at position 5 / index 4
VAR.insert(4, 'item')
```

## .pop()
Remove elements from a list by index

```terminal
# splice the last item
VAR.pop()

#splice the first iteam
VAR.pop(0)
```

## range()
Generate a numberical range list

```terminal
# create a list range on numbers, starting at 0, up to 100, with intervals of 10.
VAR_Range = range(0, 100, 10)
```

## .len()
Get the length of a list

```terminal
len(VAR)
```

## Slicing
Select portions of a list using slicing syntax

## .count
Count the number of times that an element appears in a list 

```terminal
# count number of items in list
VAR.count()
```

## .sort and .sorted
Sort a list of items

```terminal
# .sort sortes the current list
VAR.sort()

# can be reversed
#VAR.sort(reverse=True)

# .sorted creates a new list, and therefore should be put in to a new var
VAR_2 = sorted(VAR)
```

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