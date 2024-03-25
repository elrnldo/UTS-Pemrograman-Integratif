class Person:

  def __init__(bmi, weight, height):

    bmi.weight = weight
    bmi.height = height

  def BMI_Value(bmi):
    if bmi.height == 0:
      return 0  # Avoid division by zero
    return bmi.weight / (bmi.height * bmi.height)

  def __eq__(bmi, other):
    if not isinstance(other, Person):
      return False  # Only compare with Person objects
    return bmi.weight == other.weight and bmi.height == other.height

# Example usage
person1 = Person(float(input("Enter the Person 1 weight in Kilogram : ")), float(input("Enter the Person 1 height in meter: ")))
person2 = Person(float(input("Enter the Person 2 weight in Kilogram : ")), float(input("Enter the Person 2 height in meter: ")))

# Compare BMI values (not recommended)
bmi1 = person1.BMI_Value()
bmi2 = person2.BMI_Value()

if bmi1 == bmi2:  # Not ideal due to floating-point precision issues
  print("Person 1 and Person 2 have the same BMI (Compared using BMI_Value).")
else:
  print("Peerson 1 and Person 2 have different BMI(Compared using BMI_Value)")

# Compare Person objects using the overridden __eq__ method
if person1 == person2:
  print("Person 1 and Person 2 are equal (using __eq__).")
else:
  print("Person 1 and Person 2 are not equal.")
