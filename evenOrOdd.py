while True:
  try: 
    a = int(input("Give me a number: "))
    if type(a) == int:
      if a % 2 != 0:
        print("The number is odd!")
    else:
      print("The number is even!")
    break
  except: 
      print("Please give me a whole number in digits!")