def classifyNum(num):
  '''classifyNum(num) -> str
  Takes a decimal, fraction, or integer and classifies it as natural, whole, integer, rational, real'''
  # number is integer
  if (num * 10) % 10 == 0:
    if num == 0:
      return "whole, integer, rational, real"
    if num < 0:
      return "integer, rational, real"
    if num > 0:
      return "natural, whole, integer, rational, real"
  # number is not integer
  else:
    return "rational, real"

def letterInUserNum(userNum):
  '''letterInUserNum(userNum) -> bool
  checks if the user inputted invalid letters or other strange symbols'''
  for char in userNum:
    if char == "a" or char == "b" or char == "c" or char == "d" or char == "f" or char == "g" or char == "h" or char == "j" or char == "k" or char == "l" or char == "m" or char == "n" or char == "o" or char == "p" or char == "q" or char == "r" or char == "s" or char == "t" or char == "u" or char == "v" or char == "w" or char == "x" or char == "y" or char == "z" or char == "*" or char == "^":
      return True
  if "+" in userNum[1:-1] or userNum[-1] == "+" or "-" in userNum [1:-1] or userNum[-1] == "-" or userNum[0] == "/" or userNum[-1] == "/":
    return True

print("Welcome to the Number Type Classifier!")
print("You can classify decimals, fractions, integers, π, e and i.")
userNum = input("Type what you would like to classify: ")

# check for invalid characters in input
while letterInUserNum(userNum):
  userNum = input("Type what you would like to classify: ")
    
# special numbers
if userNum == "eiπ" or userNum == "eπi" or userNum == "ieπ" or userNum == "iπe" or userNum == "πei" or userNum == "πie":
  print(userNum + " = -1")
  print("So, your number is: integer, rational, real")
elif "i" in userNum:
  print("Your number is: imaginary")
elif ("e" in userNum) or ("π" in userNum):
  print("Your number is: irrational, real")
# fractions
elif "/" in userNum:
  print("Your number is: rational, real")
# normal numbers
else:
  userNum = float(userNum)
  print("Your number is: " + classifyNum(userNum))
