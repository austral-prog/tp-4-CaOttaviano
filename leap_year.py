def leap_year():
    year = int(input("Ingrese un año: "))
    if year % 4 == 0 and year % 100 != 0:
        print("El año " + f"{year}" + " es bisiesto.")
    elif year % 400 == 0:
        print("El año " + f"{year}" + " es bisiesto.")
    else:
        print("El año " + f"{year}" + " no es bisiesto.")
