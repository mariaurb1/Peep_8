#-------------------------------------------------------------------------------
# Name:         Ejercicio resuelto 2
# Purpose:      Ejercicio resuelto # 2: Escribir programa que convierta las
#               temperaturas de:
#               a.)    Grados Celsius a grados Fahrenheit
#               b.)    Grados Celsius a gados Kelvin
#               c.)    Grados Kelvin a grados Fahrenheit
#               d.)    Grados Kelvin a grados Celsius
#               e.)    Grados Fahrenheit a grados Kelvin
#               f.)    Grados Fahrenheit a grados Celsius
#
# Author:       Jose David Montesino Hoyos
# Created:     21/04/2024
#-------------------------------------------------------------------------------
# Función para parar el programa en cada una de las opciones
def parar():
    p=input("Presione <ENTER> para continuar")

# Función que permite capturar los números que seran objetos de la operación
def capturar ():
    try:
        T=float(input("Por favor digite la temperatura: "))
        return T
    except Exception as ex:
        print(ex)

def  CelsiusFahrenheit(C):
    ## F=(°C × 9/5) + 32
    return (C * 9/5) + 32

def CelsiusKelvin(C):
    ## K=°C + 273.15
    return C + 273.15

def KelvinFahrenheit(K):
    ## F=(K − 273.15) × 9/5 + 32
    return (K - 273.15) * 9/5 + 32

def KelvinCelsius(K):
    ## C=K − 273.15
    return K - 273.15

def FahrenheitKelvin(F):
    ## K=(°F − 32) × 5/9 + 273.15
    return (F - 32) * 5/9 + 273.15

def FahrenheitCelsius(F):
    ## C=(°F − 32) × 5/9
    return (F - 32) * 5/9

def main():
    try:
        continuar=True
        T=0
        while continuar==True:
                opcion=input("Seleccione una opción:"+chr(13)+\
                "1--> Capturar Temperatura"+chr(13)+"2--> Celsius a Fahrenheit"\
                +chr(13)+"3--> Celsius a Kelvin"+chr(13)+"4--> Kelvin a Fahrenheit"\
                +chr(13)+"5--> Kelvin a Celsius"+chr(13)+"6--> Fahrenheit a Kelvin"\
                +chr(13)+"7--> Fahrenheit a Celsius"+chr(13)+"0--> Salir")
                if opcion == '1':
                    T=capturar()
                elif opcion=='2':
                    print(f"{T}°C = {CelsiusFahrenheit(T)} °F")
                    parar()
                elif opcion=='3':
                    print(f"{T}°C = {CelsiusKelvin(T)} °K")
                    parar()
                elif opcion=='4':
                    print(f"{T}°K = {KelvinFahrenheit(T)} °F")
                    parar()
                elif opcion=='5':
                    print(f"{T}°K = {KelvinCelsius(T)} °C")
                    parar()
                elif opcion=='6':
                    print(f"{T}°F = {FahrenheitKelvin(T)} °K")
                    parar()
                elif opcion=='7':
                    print(f"{T}°F = {FahrenheitCelsius(T)} °C")
                    parar()
                elif opcion=='0':
                    print("Bye bye bye santiago 2")
                    continuar=False
                else:
                    print("Seleccione una opción valida")

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()

#Hola
#Esto es una prueba para el cambio de git 