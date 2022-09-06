from to_units import days_to_units

def validate_and_execute(days_and_unit_dictionary):
  try:
    user_days_to_int = int(days_and_unit_dictionary["days"])
    if user_days_to_int > 0:
      days_to_units(user_days_to_int, days_and_unit_dictionary["unit"])
    elif user_days_to_int < 0:
      print("Enter a positive number of days")
    else:
      print("You must enter a number greater than zero")
  except ValueError:
    print("You must enter a valid number of days")
