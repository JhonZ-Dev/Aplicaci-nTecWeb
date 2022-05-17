#Primer Ejercicio
print("""
[1] Dias a Años
[2] Semana a Dias""")
opciones = input("Estimado usuario eliga una opcion:    ")
if opciones == '1':
    dias = int(input("Digite el numero de dias que va a transformar a años: "))
    año = dias * (1 / 365)
    print("El numeros de años es :  {}".format(año))
