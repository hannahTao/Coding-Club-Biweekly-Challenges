import math
print('What do you want to do with this calculator?')
userInput = input('Type "add" "multiply" "divide" (input negative numbers in "add" to subtract). Or, type "more" to see more options: ')
if userInput == "more":
  print("You can type:")
  print('"degree/radian" to convert angle measures')
  print('"trig" for trig functions (mode radian)')
  print('"log" to find logarithm of x to a base')
  print('"Ln" to find natural logarithm of x')
  print('"x^y" to raise x to the y power')
  print('"e^x" to raise e to the x power')
  print('"sqrt" to find square root of x')
  print('"remainder" to find remainder when x/y')
  print('"factorial" to find x (integer) factorial')
  print('"gcd" to find gcd of integers x and y')
  print('"hypotenuse" to find hypotenuse of a right triangle with legs of length x and y')
  userInput = input("Choose one: ")
if userInput in ["add", "multiply", "divide"]:
  numOfNumbers = int(input("How many numbers do you want to " + userInput + "?"))
  for i in range(numOfNumbers):
    if i == 0:
      value = float(input("Input a number: "))
    else:
      if userInput == "add":
        value += float(input("Input a number: "))
      if userInput == "multiply":
        value *= float(input("Input a number: "))
      if userInput == "divide":
        value /= float(input("Input a number: "))
  print(str(value))
if userInput == "degree/radian":
  conversion = input('Type "radians" to convert degrees to radians and "degrees" to convert radians to degrees: ')
  angleMeasure = float(input("Angle measure: "))
  if conversion == "degrees":
    print(math.degrees(angleMeasure))
  if conversion == "radians":
    print(math.radians(angleMeasure))
if userInput == "trig":
  trigFunction = input('Type "sin", "cos", "tan", "asin", "acos", or "acot": ')
  if trigFunction in ["sin", "cos", "tan"]:
    angleMeasure = float(input("Angle measure: "))
    if trigFunction == "sin":
      print(math.sin(angleMeasure))
    if trigFunction == "cos":
      print(math.cos(angleMeasure))
    if trigFunction == "tan":
      print(math.tan(angleMeasure))
  if trigFunction in ["asin", "acos", "acot"]:
    x = float(input("x: "))
    if trigFunction == "asin":
      print(math.asin(x))
    if trigFunction == "acos":
      print(math.acos(x))
    if trigFunction == "atan":
      print(math.atan(x))
if userInput == "log":
  base = float(input("Base: "))
  x = float(input("x: "))
  print(math.log(x, base))
if userInput == "Ln":
  x = float(input("x: "))
  print(math.log(x))
if userInput == "x^y":
  x = float(input("x: "))
  y = float(input("y: "))
  print(math.pow(x,y))
if userInput == "e^x":
  x = float(input("x: "))
  print(math.exp(x))
if userInput == "sqrt":
  x = float(input("x: "))
  print(math.sqrt(x))
if userInput == "remainder":
  x = float(input("x: "))
  y = float(input("y: "))
  print(math.fmod(x,y))
if userInput == "factorial":
  x = int(input("x: "))
  print(math.factorial(x))
if userInput == "gcd":
  x = int(input("x: "))
  y = int(input("y: "))
  print(math.gcd(x,y))
if userInput == "hypotenuse":
  x = float(input("x: "))
  y = float(input("y: "))
  print(math.hypot(x,y))
