import math #Hacemos uso de math para proporciona acceso a las funciones matemáticas, en este caso la raiz
print("Digite un numero que sea mayor que cero ")#Pedimos al usuario que digite un numero mayor que cero
raiz = float(input()) #Digitamos el numero, y se almacena en la variable raiz
if raiz<0: 
  print("Digite un valor mayor que 0")#Si el numero es menor que cero, entonces nos dara error, raiz(-1) es numero complejo
elif raiz > 0: #Si es mayor que cero, entonces calculara la raiz 
  print("El valor de la raiz cuadrada es: ")
  print(math.sqrt(raiz)) #Para sacar la raiz 
else:
  ("Error, vuelva a ejecutar el programa") #Caso contrario se cierra el programa.