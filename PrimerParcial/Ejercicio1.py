#Primer Ejercicio
print("""
[1] Dias a Años
[2] Semana a Dias""")
opciones = input("Estimado usuario eliga una opcion:    ") #Se elige una variable que alcenará la opcion que eligirá el usuario.
if opciones == '1': # Si opcion == 1 entonces calculará el numero de dias a años
    #Tiene como argumentos los días como los años
    #Dias = representa los dias que se van a transformar a ños, este valor netamente es entero
    dias = int(input("Digite el numero de dias que va a transformar a años: "))
    #Año = Sistema de solución o fórmula a usar 
    año = dias * (1 / 365)
    #Finalmente se usa el format que es nos permite incluir en una cadena, texto ordinario y caracteres de formateo,
    print("El numeros de años es :  {}".format(año))
elif opciones == '2': #Uso del elif: es una forma común de controlar el flujo de un programa, lo que te permite ejecutar bloques de código específicos según el valor de algunos datos
    #Representa los dias, y netamente es un valor entero
    diasSemana = int(input("Digite el numero de dias que va a transformar a semanas"))
    #Representa la formula a usar, donde sabemos que 1 semana tiene 7 dias
    semana = diasSemana * (1 / 7 )
    print("El numero de dias a semanas es:  {}".format(semana))#Printiamos el resultado
else:
    print("Digite un valor correcto:    x-x") #Caso contrario si el usuario digita algún valor incorrecta el sistema le mandará un mensaje
