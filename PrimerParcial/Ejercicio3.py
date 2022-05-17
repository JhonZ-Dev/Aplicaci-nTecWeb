#Ingresar calificaciones de cinco materias y calcular el total, el promedio y el porcentaje.
#Tenemos en cuenta que para este ejercicio hay dos formas de hacerlo
#Una de ella es ir pidiendo calificacion por calificaion
#Y la otra es crear un bucle for que pida las notas hasta la quinta materia.
#Para este caso implementaremos un for, ya que consume menos lineas de código y en mi
#opinion es más práctico.

#Creamos un print para indicar al usuario de que va a tratar el tema.
print("""El siguiente sistema calculará
[1] Promedio total de calificaciones
[2] Suma total
[3] Porcentaje total
"""
)
#Creamos una variable almacenadora para digitar el numero de materias que va a eleguir.
materias = int(input("Digite el numero de materias:     "))
#Creamos la variable suma que se va a inicializar en cero
suma = 0
#Creamos una variable i para inicializarla en 1, ya que esta va a ir aumentando de 1 en 1.
i = 1
#Inicio del bucle for
for n in range(1, materias+1): #Escogemos el rango que va a empezar a 1, y llegara hasta el numeros de materias que el usuario digite
   print("Ingrese el nombre de la materia") #se repetirá segun el numero de materias
   Nombremateria = (input()) #Digitamos el nombre de la materia 
   print("Ingrese la calificación de la materia : " + Nombremateria ) #Decimos al usuario que digite la calificacion
   cali1 = int(input()) #Se almacena la calificacion
   i+=1 #Le decimos qu el valor de i va a ir incrementando
   suma = suma + cali1 # Formula para la suma
   prom = suma / materias #Formula para calcular el promedio
   porcentaje = (suma / prom) * 100 #Formula para calcular el porcentaje