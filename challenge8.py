def convert_prefix():
  '''convert_prefix() -> str
  converts between different metric prefixes'''
  
  # get info of original number
  print("Convert from:")
  number = float(input("Number:"))
  prefix = input('Prefix (type "unit" if no prefix):')
  while prefix not in ['tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'unit', 'deci', 'centi', 'milli', 'micro', 'nano', 'pico']:
    print("That is not a valid prefix!")
    prefix = input('Prefix (type "unit" if no prefix):')
  
  # get info of what to convert to
  print("Convert to:")
  newPrefix = input('Prefix (type "unit" if no prefix):')
  while newPrefix not in ['tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'unit', 'deci', 'centi', 'milli', 'micro', 'nano', 'pico']:
    print("That is not a valid prefix!")
    newPrefix = input('Prefix (type "unit" if no prefix):')

  prefixDict = {'tera':1000000000000, 'giga':1000000000, 'mega':1000000, 'kilo':1000, 'hecto':100, 'deca':10, 'unit':1, 'deci':0.1, 'centi':0.01, 'milli':0.001, 'micro':0.000001, 'nano':0.000000001, 'pico':0.000000000001}

  # multiply by the right amount
  prefixChange = number * (prefixDict[prefix] / prefixDict[newPrefix])

  # concatenate returned sentence
  returnString = str(number) + " " + prefix + " equals " + str(prefixChange) + " " + newPrefix

  return returnString

def convert_volume():
  '''convert_volume -> str
  converts between the customary volume units gallons, quarts, pints, and cups'''
  
  # get info of original number
  print("Convert from:")
  number = float(input("Number:"))
  unit = input('Unit (gallons, quarts, pints or cups):')
  while unit not in ['gallons', 'quarts', 'pints', 'cups']:
    print("That is not a valid unit!")
    unit = input('Unit (gallons, quarts, pints or cups):')

  # get info of what to convert to
  print("Convert to:")
  newUnit = input('Unit (gallons, quarts, pints or cups):')
  while newUnit not in ['gallons', 'quarts', 'pints', 'cups']:
    print("That is not a valid unit!")
    newUnit = input('Unit (gallons, quarts, pints or cups):')

  unitsDict = {"gallons": 16, "quarts": 4, "pints": 2, "cups": 1}

  # multiply by the right amount
  unitChange = number * (unitsDict[unit] / unitsDict[newUnit])

  # concatenate returned sentence
  returnString = str(number) + " " + unit + " equals " + str(unitChange) + " " + newUnit

  return returnString

def convert_mass():
  '''convert_mass -> str
  converts between the customary mass units tons, pounds, and ounces'''
  
  # get info of original number
  print("Convert from:")
  number = float(input("Number:"))
  unit = input('Unit (tons, pounds, and ounces):')
  while unit not in ['tons', 'pounds', 'ounces']:
    print("That is not a valid unit!")
    unit = input('Unit (tons, pounds, and ounces):')

  # get info of what to convert to
  print("Convert to:")
  newUnit = input('Unit (tons, pounds, and ounces):')
  while newUnit not in ['tons', 'pounds', 'ounces']:
    print("That is not a valid unit!")
    newUnit = input('Unit (tons, pounds, and ounces):')

  unitsDict = {"tons": 32000, "pounds": 16, "ounces": 1}

  # multiply by the right amount
  unitChange = number * (unitsDict[unit] / unitsDict[newUnit])

  # concatenate returned sentence
  returnString = str(number) + " " + unit + " equals " + str(unitChange) + " " + newUnit

  return returnString

def convert_units():
  '''convert_units -> str
  puts convert_prefix(), convert_volume(), and convert_mass() together'''
  
  # user chooses program
  print("Welcome to the units converter!")
  print("If you want to convert between metrix prefixes, type 1.")
  print("If you want to convert between customary volume units, type 2.")
  print("If you want to convert between customary mass units, type 3.")
  programNumber = input("Your answer:")
  
  # execute the right program
  if programNumber == "1":
    return convert_prefix()
  if programNumber == "2":
    return convert_volume()
  if programNumber == "3":
    return convert_mass()

print(convert_units())
