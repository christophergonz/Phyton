from pip._vendor.msgpack.fallback import xrange

primernumero = input("Escribe el primer numero: ")
numero1 = float(primernumero)
segundonumero = input("Escribe el segundo numero: ")
numero2= float(segundonumero)

suma= numero1+numero2

print("El resultado es: ", suma)


lista = []
cantidad=int (input("Cuantos numeros desea ingresar: "))
i=1
total=1
while(cantidad > 0):
    numero = int(input("Numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1
    total = total * numero


print("Lista: ", lista)
print(total)


lista = []
cantidad=int (input("Cuantos numeros desea ingresar: "))
mayor=0
i=1

while(cantidad > 0):
    numero = int(input("Numero #" + str(i) + ":  "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1


mayor = max(lista)

print("Lista: ", lista)
print("Mayor: ", mayor)


def secuencia():

    num1=0
    total = 1
    while num1 != 1:
        num1 = int(input("Ingrese el numero: "))
        total = total * num1

    print("El resultado es: " + str(total))




def fibonacci(contador,n,p1,p2):
 var = ""
 if(contador!=n):
  var=fibonacci(contador+1,n,p2 , p1+p2)
  var=str(p2)+" "+var
 return var
n = int(input("Ingrese un numero entero\n"))
if(n>0):
 a=fibonacci(0,(n-1),0,1)
 print ("0 "+a)

def numero():
    num1= 0
    total=1
    while num1 !=1:
        num1 = int(input("Ingrese numero: "))
        total = total *num1
        print("Elresultado es:" +str(total))


def ciclo(n):
    pass
for n in xrange(0,30):
    pass
print (input("ingrese numero: "))


import math
num = input("Introduce un numero: ")
x = int(num)
factorial = math.factorial(x)
print("El factorial es: " , factorial)


def secuencia():

    num1=0
    total = 1
    while num1 != 1:
        num1 = int(input("Ingrese el numero: "))
        total = total * num1

    print("El resultado es: " + str(total))


secuencia()

def numerospares():
    numero= int(input("Cuantos numeros desea ingresar: "))
    primero = 0
    contador = 0
    suma = 0
    while contador < numero:
        primero = float(input("Ingrese el dato: "))
        cont = contador + 1
        if primero % 2 == 0:
            suma = suma + primero
        else:
            suma = suma
    print("El total de numeros pares es: " + str(suma))


numerospares()


