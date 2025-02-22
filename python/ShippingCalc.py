# Weight Var
weight = 0.5
pricePerLb = 0
flatCharge = 0

# Ground Shipping Premium option
GSPremium = 125

print ('For a weight of ' + str(weight) + ' lbs:')
print ('')

#Ground Shipping
print ('Ground Shipping Costs')

#Ground shipping cost database
if 0 < weight <= 2:
  pricePerLb += 1.50
  flatCharge += 20.00
elif 2 < weight <= 6:
  pricePerLb += 3.00
  flatCharge += 20.00
elif 6 < weight <= 10:
  pricePerLb += 4.00
  flatCharge += 20.00
elif weight >= 10:
  pricePerLb += 4.75
  flatCharge += 20.00
else:
  print ('Invalid weight')

#Ground Shipping Total Cost
GStotalCost = (weight * pricePerLb) + flatCharge

print ('')
print ('Price per lb is £' + f'{pricePerLb:.2f}')
print ('With a flat charge of £' + f'{flatCharge:.2f}')
print ('')
print ('The total cost for Ground Shipping will be £' f'{GStotalCost:.2f}')

#Premium Ground Shipping Statment
print ('')
print ('We do offer Premium shipping at a flat rate of £' f'{GSPremium:.2f}')
print ("")

#Drone Shipping
print ('Drone Shipping Costs')

#Drone shipping cost database
# cost reset
pricePerLb = 0
flatCharge = 0

if 0 < weight <= 2:
  pricePerLb += 4.50
elif 2 < weight <= 6:
  pricePerLb += 9.00
elif 6 < weight <= 10:
  pricePerLb += 12.00
elif weight >= 10:
  pricePerLb += 14.25
else:
  print ('Invalid weight')

#Drone Shipping Total Cost
DroneTotalCost = (weight * pricePerLb) + flatCharge

print ('')
print ('Price per lb is £' + f'{pricePerLb:.2f}')
print ('With a flat charge of £' + f'{flatCharge:.2f}')
print ('')
print ('The total cost for Drone Shipping will be £' f'{DroneTotalCost:.2f}')
print ('')

# Comparison
print ('Ground Shipping: £' f'{GStotalCost:.2f}')
print ('Premium Ground Shipping: £' f'{GSPremium:.2f}')
print ('Drone Shipping: £' f'{DroneTotalCost:.2f}')
print ('')
if GStotalCost <= GSPremium and GStotalCost <= DroneTotalCost:
    print("Ground shipping is the cheapest option")
elif GSPremium <= GStotalCost and GSPremium <= DroneTotalCost:
    print("Premium Ground Shipping is the cheapest option")
else:
    print("Drone shipping is the cheapest option")