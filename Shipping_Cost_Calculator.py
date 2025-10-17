# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

 # Here is a new update by cbins13
 # Input quantity and unit price
quantity = int(input("Enter the quantity of items: "))
unit_price = float(input("Enter the price per item in USD: "))

# Calculate total price
total_price = quantity * unit_price

# Display the result
print(f"Total Price: {total_price} USD")