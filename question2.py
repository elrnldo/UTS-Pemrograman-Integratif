def factorial(number):
  if number == 0:
    return 1
  else:
    return number * factorial(number - 1)

# Get the test date from the user (replace with actual input method if needed)
test_date = int(input("Enter today's test date (non-negative integer): "))

# Input validation (check for non-negative integer)
if test_date < 0:
  print("Error: Please enter a non-negative integer.")
else:
  # Calculate and print the product
  product = factorial(test_date)
  print(f"Product of values from 1 to {test_date}: {product}")
