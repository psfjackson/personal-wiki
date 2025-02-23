# My solution for Carly Clipper project:

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# total price var
total_price = 0

# loop adding to total price 
for price in prices:
  total_price += price

#average price
average_price = total_price / len(prices)
print(f'Average Haircut Price: £{average_price:.2f}')

# New prices with £5 reduction
new_prices = [price - 5 for price in prices]

print ('New prices:')
print(new_prices)

# Total revenuce calculation
total_revenue = 0

# Total revenue loop
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print(f'Total Revenue: £{total_revenue:.2f}')

# Average daily revenue
average_daily_revenue = total_revenue / 7
print(f'Average daily revenue: £{average_daily_revenue:.2f}')

# Loop to identify haircuts cheaper that £30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)

