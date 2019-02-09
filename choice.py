# https://stackoverflow.com/questions/54608432/how-to-use-while-loops-with-multiple-if-elif-statements

while True:

  choice = input('What would you like to convert? \n Farenheit to Celcius (1) \n Feet to Meters (2) \n Pounds to Kilograms (3) \n Ounces to Liters (4) \n : ')

  if choice == "1":

      degreesF = float(input('Enter the temperature in degrees F: '))
      degreesC = 5/9*(degreesF - 32)
      print(degreesC, 'degrees Celcius')

  elif choice == "2":

      distanceFeet = float(input('Enter the distance in feet: '))
      distanceMeters = distanceFeet/3.28
      print(distanceMeters, 'm')

  elif choice == "3":

      Pounds = float(input('Pounds: '))
      Kilograms = Pounds*0.45359237038
      print(Kilograms, 'kg')

  elif choice == "4":

      Ounces = float(input('Ounces: '))
      Liters = Ounces*0.0295735
      print(Liters, 'L')

  else:
      break