#### Programa para medir la longitud de una palabra #####


def verificar_longitud(palabra): # En esta linea utilizamos la función def para definir la función de medir la longitud de la palabra ingresada
    longitud = len(palabra) #definimos la variable longitud y es igual la longitud del parametro "palabra"
    if 4 <= longitud <= 8: #definimos el rango que debe taner la variable palabra 
        print(f'La palabra {palabra} es correcta.')
    elif longitud < 4: #Si es menor a 4 lanzara el siguiente mensaje 
        print(f"Hacen falta letras. La palabra {palabra} solo tiene {longitud} letras.")
    else: #Si es mayor a 8 lanzara el siguiente mensaje 
        print(f"Sobran letras. La palabra {palabra} tiene {longitud} letras.")


# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ") #una vez definida la función definimos la variable palabra que es igual al valor ingresado por el usuario
verificar_longitud(palabra) 



######### Programa para encontrar el cuadrande de 1 coordenada ingresada por el usuario #########


def determinar_cuadrante(x, y): #iniciamos definiendo la función determinar cuadrante con las dos variables que vamos a utilizar 
    if x == 0 or y == 0: #establecemos el punto cero de las variables 
        print("Las coordenadas se encuentran en el origen y no pueden ser cero.") #imprimimos un mensaje en caso que los dos valores sean cero
        return
    if x > 0 and y > 0: #para el primer cuadrante definimos los valores que pueden tomar las varibales donde deben ser (+)(+)
        print("Las coordenadas se encuentra en el I cuadrante.")
    elif x < 0 and y > 0: #para el segundo cuadrante definimos los valores que pueden tomar las varibales (-)(+)
        print("Las coordenadas se encuentra en el II cuadrante.")
    elif x < 0 and y < 0: #para el tercer  cuadrante definimos los valores que pueden tomar las varibales (-)(-)
        print("Las coordenadas se encuentra en el III cuadrante.")
    else: #finalmente no definimos los valores que puede tomar las variables ya que si no se encuentran en los rangos anteriormente mencionados por logica deben caer en el ultimo cuadrante disponible donde los valores son (+)(-)
        print("Las coordenadas se encuentra en el IV cuadrante.")

# Pedimos  al usuario que ingrese las coordenadas una vez que ya se definio la función 
x = float(input("Ingrese la coordenada x: ")) #definimos la variable 'x' y el float nos ayuda a que si se ingresen valores con punto decimal
y = float(input("Ingrese la coordenada y: ")) #definimos la variable 'y' y  el float nos ayuda a que si se ingresen valores con punto decimal

# Determinar en qué cuadrante se encuentra el punto
determinar_cuadrante(x, y)