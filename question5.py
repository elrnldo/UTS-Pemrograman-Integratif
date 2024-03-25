def calculate_sum_with_formatting(numbers):
 total_sum = sum(numbers)
 formatted_sum = "{:,.3f}".format(total_sum)
 return formatted_sum

# Open the file and read the numbers
with open("input.txt", "r") as file:
 numbers = [int(line.strip()) for line in file]

# Calculate and print the formatted sum
formatted_total = calculate_sum_with_formatting(numbers)
print(f"Sum of numbers: {formatted_total}")