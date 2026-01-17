def funcion1():
    if numopcion == 1:
        print('\n')
        funcionsuma()
    elif numopcion == 2:
        print('\n')
        funcionresta()
    elif numopcion == 3:
        print('\n')
        funciondividir()
    elif numopcion == 4:
        print('\n')
        funcionmultiplicar()
    else: print('opcion invalida')
        
            
def funcionsuma():
    print('-----SUMA-----')
    num1= float(input("ingresa el primer numero: "))
    num2= float(input("ingresa el segundo numero: "))
    suma = num1 + num2
    
    print('La suma es de: {0}' .format(suma)) 

def funcionresta():
    print('-----RESTA-----')
    num1= float(input("ingresa el primer numero: "))
    num2= float(input("ingresa el segundo numero: "))
    resta = num1 - num2
    
    print('La resta es de: {0}' .format(resta)) 

    
def funcionmultiplicar():
     print('-----Multiplicacion-----')
     num1= float(input("ingresa el primer numero: "))
     num2= float(input("ingresa el segundo numero: "))
     multiplicar = num1 * num2
     
     print('La multiplicacion es de: {0}' .format(multiplicar)) 



def funciondividir():
     print('-----DIVISION-----')
     num1= float(input("ingresa el primer numero: "))
     num2= float(input("ingresa el segundo numero: "))
     
     if num2 == 0:
         print('No se puede dividir entre 0 papu')
         return
     
     dividir = num1 / num2
     
     print('La division es de: {0}' .format(dividir)) 
    
numopcion=int(input('1-.Suma \n'
                    '2-.Resta \n'
                    '3-.Division \n'
                    '4-.Multiplicacion \n'
                    'Selecciona una opcion tilin: '))
funcion1()