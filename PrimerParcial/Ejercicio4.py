
#Formulas: 
#1 kilogramo tien 2.2046 libras
#1 libra tiene 453.59 gramos
#Con estas formulas ya tenemos el código resuelto.
#Imprimimos las opciones disponibles dentro del programa
print("""
[1] Libras(lb) a Kilosgramos(kg)
[2] Libras(lb) a Gramos(gr)""")
menu = int(input("Digite la opcion que desee:   ")) #Creamos una variable menu de tipo entero
#Este menu solo tiene dos opcines 1 y 2 caso contrario si digitamos otra opcion mostrará un error
if menu == 1: #Si menú es igual a 1 
  print("Ha elegido transformar libras a kilogramos") #Imprimimos el mensaje para que el usuario sepa que eliguió
  libra = float(input("Digite el valor de libra:  ")) #Digita el valor de la libro, de tipo float
  kilogramos = libra * (1/2.2040) #Formula para pasar de libras a kilogramos
  print("El valor de libras a kilgramos es: {}".format((kilogramos))) #Imprimimos el resultado.
elif menu ==2:#Si menu es igual a 2 
  print("Ha elegido transformar libras a gramos")#Imprimimos mensaje al usuaroio
  libra2 = float(input("Digite el valor de libra:   ")) #Tipo float para pedir la libra
  gramos = libra2 * (453.59/1.0)
  print("El valor de libras a gramos es:  {}".format(gramos)) #Imprimimos mensajes
else:
  print("Digite un valor correcto y vuelva a ejecutar el prgrama.") #Caso contrario, error
  ###Ejercicio Terminado
