#!/bin/python3

#Price per weight
shipping_cost = 1.20

#User enter the cost of the item
customer_basket_cost = float(input('Please enter cost: '))

#User enter the weight of the item
customer_basket_weight = float(input('Please enter weight: '))

# 
if customer_basket_cost > 100:
  print('Free Shippment!')
  
else:
  customer_basket_cost = customer_basket_cost + (customer_basket_weight * shipping_cost)
  print('Your total cost is: $' + str(customer_basket_cost))

#Source: TryHackMe.com