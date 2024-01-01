while True:
  try: 
    a = int(input("Please give me a number: "))
    break
  except ValueError:
    print("I said whole!")
    
if a > 1:
  for i in range(2, int((a/2)+1)):
    if a % i == 0:
      print("Your number is not a prime number :(")
      break
    else:
      print("Your number is a prime number!")
else:
  print("Your number is not a prime number :(")