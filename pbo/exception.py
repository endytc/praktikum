a = 2
b = 0
# if b == 0:
#   raise Exception("var b harus lebih dari 0")
# c = a/b


try:
  c = a/b
except ZeroDivisionError as error:
  print(error)
  pass

print("Program masih berlanjut")


while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Oops!  That was no valid number.  Try again...")