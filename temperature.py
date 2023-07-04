print("1-CELCIUS TO FAHRENHEIT\n2-CELCIUS TO KELVIN\n3-FAHRENHEIT TO CELCIUS\n4-KELVIN TO CELCIUS\n5-FAHRENHEIT TO KELVIN\n6-KELVIN TO FAHRENHEIT\n7-EXIT")

while True:
    choice = int(input("Your Choice (1-7): "))

    if choice == 1:
        celcius = float(input("Degree: "))
        fahrenheit = (celcius * 1.8) + 32
        print(f"{celcius} degree celcius is equal to {fahrenheit} degree fahrenheit.")
    elif choice == 2:
        celcius = float(input("Degree: "))
        kelvin = celcius + 273.15
        print(f"{celcius} degree celcius is equal to {kelvin} degree kelvin.")
    elif choice == 3:
        fahrenheit = float(input("Degree: "))
        celcius = (fahrenheit - 32)/1.8
        print(f"{fahrenheit} degree fahrenheit is equal to {celcius} degree celcius.")
    elif choice == 4:
        kelvin = float(input("Degree: "))
        celcius = kelvin - 273.15
        print(f"{kelvin} degree kelvin is equal to {celcius} degree celcius.")
    elif choice == 5:
        fahrenheit = float(input("Degree: "))
        kelvin = (fahrenheit + 459.67)*(5/9)
        print(f"{fahrenheit} degree fahrenheit is equal to {kelvin} degree kelvin.")
    elif choice == 6:
        kelvin = float(input("Degree: "))
        fahrenheit = 1.8*(kelvin - 273.15)+32
        print(f"{kelvin} degree kelvin is equal to {fahrenheit} degree fahrenheit.")
    elif choice ==7:
        break
    else:
        print("Wrong Choice. Please choice a number between 1-7.")






