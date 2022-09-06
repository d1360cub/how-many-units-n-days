"""def days_to_units(num_of_days, name_of_unit):
    unit = 1
    if name_of_unit == "seconds":
      unit = 24*60*60
    elif name_of_unit == "minutes":
      unit = 24*60
    elif name_of_unit == "hours":
      unit = 24
    else:
      print("You must enter a valid unit to convert")
    
    print(f"There are {(num_of_days*unit)} {name_of_unit} in {num_of_days} days")

def validate_and_execute():
  try:
    user_days_to_int = int(days_and_unit_dictionary["days"])
    if user_days_to_int > 0:
      days_to_units(user_days_to_int, days_and_unit_dictionary["unit"])
    elif user_days_to_int < 0:
      print("Enter a positive number of days")
    else:
      print("You must enter a number greater than zero")
  except ValueError:
    print("You must enter a valid number of days")"""

from validate import validate_and_execute

answer = "y"
while answer == "y":
  user_input = input("Enter number of days and convertion units, separated by comma\n")
  days_and_unit = user_input.split(", ")
  days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
  validate_and_execute(days_and_unit_dictionary)
  answer = input("Do you want to continue? (y/n):\n")
