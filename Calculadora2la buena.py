def obtener_datos_usuario():
    while True:
        try:
            Nombre = input("Introduce tu nombre: ")
            if not Nombre:
                raise ValueError("Debes ingresar un nombre")
            
            Apellido_Paterno = input('Introduce tu apellido paterno: ')
            if not Apellido_Paterno:
                raise ValueError('Debes ingresar un apellido')
            
            Apellido_Materno = input('Introduce tu apellido materno: ')
            if not Apellido_Materno:
                raise ValueError('Debes ingresar un apellido: ')

            Edad = int(input("Introduce tu edad: "))
            if Edad <= 0:
                raise ValueError("La edad debe ser un número")
            
            Peso= float(input("Introduce tu peso en kg: "))
            if Peso <= 0:
                raise ValueError("El peso debe ser un número")
            
            Estatura = float(input('Introduce tu estatura en mts: '))
            if Estatura <=0:
                raise ValueError('La estatura debe ser un número')
            
            return Nombre, Apellido_Paterno, Apellido_Materno, Edad, Peso, Estatura
        except ValueError as error:
             print("Error:", error)
             print("Por favor, ingresa un valor válido.\n")



Nombre, Apellido_Paterno, Apellido_Materno, Edad, Peso, Estatura = obtener_datos_usuario()

IMC = Peso / Estatura**2

print('''
      
      Resultados sobre su IMC: 
      
        ''' )

print('Nombre: '+ Nombre)
print('Apellido Paterno: ' + Apellido_Paterno)
print('Apellido Materno: ' + Apellido_Materno)
print('Su edad es: ' + str(Edad) + ' años')
print('Su peso actual es: ' + str(Peso) + ' kg')
print('Su estatura actual es: ' + str(Estatura) + ' mts')
print(f'Con los datos obtenidos su IMC es {IMC: .2f}')



if(Edad < 18):
    print(Nombre + ' Usted es menor de edad')
else:
    print(Nombre + ' es mayor de edad')

if IMC >=0 and IMC <=15.99:
    print('Con base en su IMC usted tiene delgadez severa')
elif IMC >= 16.00 and IMC <= 16.99:
    print('Con base en su IMC usted tiene delgadez moderada')
elif IMC >= 17.00 and IMC <= 18.49:
    print('Con base en su IMC usted tiene delgadez leve')
elif IMC >= 18.50 and IMC <= 24.99:
    print('Con base en su resultado usted tiene un IMC normal')
elif IMC >= 25.00 and IMC <= 29.99:
    print('Con base en su IMC usted tiene sobrepeso')
elif IMC >= 30.00 and IMC <= 34.99:
    print('Con base en su IMC usted tiene obesidad leve')
elif IMC >= 35.00 and IMC <= 39.00:
    print('Con base en su IMC usted tiene obesidad media')
elif IMC >= 40.00:
    print('Con base en su IMC usted tiene obesidad morbida')





