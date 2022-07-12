#User inputs year to check
year = int(input("Which year do you want to check? "))
#Determine if the year inputed is a leap year
if (year % 4 == 0):
  if (year % 100 == 0):
    if (year % 400 == 0):
      print("Leap year")
    else:
      print("Not Leap year")
  else:
    print("Leap year")
else:
  print("Not Leap year")
