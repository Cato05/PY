a = str(input("Give me a word: "))

b = a[len(a)::-1]

check = False

for i in range(0, len(a)):
  if a[i] == b[i]:
    check = True
  else:
    check = False
    
if check == True:
  print("Congratulations, your word is palindrome!")
else:
  print("Sorry, your word is not palindrome :(")