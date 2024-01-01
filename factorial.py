while True:
  try:
    a = int(input("Please give me a whole number: "))
    break
  except ValueError:
    print("I said whole number, and in digits, if possible.")
b = 0
i = 0

if a != 0:
  b = 1

while i != a:
  i +=1
  b = b * i


if b == 0:
  print("The factorial of your number is 1!")
else:
  print("The factorial of your number is", b)