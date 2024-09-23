edad = int(input("Coloca tu edad:"))

if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

print(f"El precio total de la entrada es: {precio}")

