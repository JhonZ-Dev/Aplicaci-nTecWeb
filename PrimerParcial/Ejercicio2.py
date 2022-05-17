#Calcular la formula de la velocidad.
#Primero tenemos que tener en cuenta que existes dos movimientos difentes
#Movimiento Rectilinio Uniforme [MRU]
#Movimiento Rectilinio Uniformemente Variado [MRUV]
#Tendremos en cuenta las fórmulas a usar:
#En MRU = V = d / t 
#En MRUV = Vf = Vo + a * t
#---------Desde Aqui va código---------------

#Printiamos las opcines a escoger.
print("""Estimado usuario existen dos tipo de velocidad, velocidad en MRU(Movimiento Rectilinio Uniforme variado
        y la velocidad en movimiento rectilinio uniformente variado)
        Elige la opción desee.
          [1] Velocidad en MRU
          [2] Velocidad en MRUV""")

# Aqui creamos la variable para que el usuario escoga una opcion
opciones = input("Digite una opción del 1 al 2: ")
#Usaremos condicional if
#Si opcines = 1, el usuario digita distancia y tiempo.
if opciones =='2':
    #distancia, representa el dato que el usuario ingresará que puede ser un vide flotante o entero ya que si hay distancia de 4.7m
    distancia = float(input("Digite el valor de la distancia:   "))
    #tiempo, de valor será entero o flotante ya que en fisica si hay tiempo de 8.9 segundos
    tiempo = float(input("Digite el valor del tiempo:     "))
    #Creamos el sistema o la ecuación a resolver el problema.
    velocidad = distancia / tiempo #Formula v= d/t