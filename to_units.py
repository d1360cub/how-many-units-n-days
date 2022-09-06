def days_to_units(num_of_days, name_of_unit):
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
