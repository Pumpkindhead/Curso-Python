import numpy as np  #se importa la biblioteca para trabajar con arreglos multidimensionales 
import matplotlib.pyplot as plt  #Se importa la biblioteca para la visualización de datos 

def simular_maquina_galton(num_canicas, num_niveles): #Se define la primer función en donde se simulará la maquina de galton
    resultados = np.zeros(num_niveles + 1)
    for _ in range(num_canicas):
        posicion = 0 #Se inicializa la función desde el valor cero 
        for _ in range(num_niveles):
            if np.random.rand() < 0.5:
                posicion += 1 
        resultados[posicion] += 1 #en cada iteración se suma 1 para que quede registrado el resultado 
    # Regresa los valores de contenedores y sus frecuencias
    return resultados

def graficar_histograma(resultados): #Se define la segunda función se utilizará para graficar los resultados obtenidos en un histograma 
    plt.hist(np.arange(len(resultados)), weights=resultados, bins=np.arange(len(resultados)+1)-0.5, edgecolor='black', alpha=0.8) #En esta línea de código se utiliza para crear el histograma 
    plt.xlabel('Contenedor') #Se asigna el nombre al eje de las x
    plt.ylabel('Número de Canicas') #Se asigna el nombre al eje de las y
    plt.title('Simulación de una Máquina de Galton') #Se agrega el título al histograma
    plt.xticks(np.arange(len(resultados))) # se establecen las ubicaciones de los resultados en el eje de las x para el gráfico 
    plt.grid(axis='y')
    plt.show() #se grafica 

num_canicas = 3000 #Número de veces que se repetira el experimento
num_niveles = 12 #Número de contenedores disponibles 

resultados = simular_maquina_galton(num_canicas, num_niveles)
graficar_histograma(resultados)
