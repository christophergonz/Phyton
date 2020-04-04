print("Ejercicio par-impar")
def parimpar(numero):

    return numero%2==0
numero = int(input("Ingresa un numero "))
if(parimpar(numero)):
 print("El numero es par")
else:
 print("El numero es impar ")




print("Producto de dos numeros")
primernumero = input("Escribe el primer numero: ")
numero1 = float(primernumero)
segundonumero = input("Escribe el segundo numero: ")
numero2= float(segundonumero)

producto= numero1*numero2

print("El resultado es: ", producto)



print("Numero mayor entre 2 numeros ")
numerouno = input("Escribe el primer numero ")
numero1 = float(numerouno)
numerodos = input("Escribe el segundo numero ")
numero2 = float(numerodos)
if numero1 > numero2:
    print("El numero mayor es", numero1 )
else:
    print("El numero mayor es", numero2 )



print("Numero mayor entre 3 numeros")
primernumero = input("Escribe el primer numero ")
unnumero = float(primernumero)
segundonumero = input("Escribe el segundo numero ")
dosnumero = float(segundonumero)
tercernumero = input("Escribe el tercer numero ")
tresnumero = float(tercernumero)
if unnumero > dosnumero> tresnumero:
    print("El numero mayor  es: ", unnumero)
elif dosnumero >tresnumero>numero1:
    print("El numero mayor es: ", dosnumero)
else:
    print("El numero mayor es:", tresnumero)


print("tabla de multiplicar")
n = int(input("Ingrese un numero positivo: "))
if n>0:
 num =1
 while num < 11:
     print(n, "X", num ,"=:", n*num)
     num += 1


print("Leer secuencia de 30 numeros y multiplicar y sumar entre ellos")
suma=0
producto =1
for i in range(1, 30):

    numerob = int(input("Ingrese un dato: "))
    suma = numerob + suma
    producto = numerob * producto

    print("El resultado de la suma es:", suma)
    print("El resultado del producto es:", producto)


def main():
    print("SUMA DE NÚMEROS")
    numerou = int(input("Escriba un número: "))
    sumatotal = 0
    while numerou >= 0:
        sumatotal += numerou
        numerou = int(input("Escriba otro número: "))
    print()
    print(f"La suma de los números positivos introducidos es {sumatotal}.")


if __name__ == "__main__":
    main()

print("Producto mediante suma")

numerok = int(input("Ingrese el primer numero: "))
numeroj = int(input("Ingrese el segundo numero: "))
productokj = int(0);
while numeroj != 0:
    productokj = productokj + numerok
    numeroj = numeroj -1

    print("El producto mediante sumas es de:", productokj)

print("Division mediante restas")
contador = int(0);
dividendo = int(input("Ingrese el primer numero: "))
divisor = int(input("Ingrese el segundo numero: "))
dividendo = dividendo - divisor
while (dividendo >= 0):
    contador = contador +1
    dividendo = dividendo - divisor
print("El resultado es de: ", contador)

def binarizar(decimal):
    print("Programa de decimal a binario")
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def enterosTresenTres(sumaTotal=0):
    i = 2
    e = 3
    for inicio in range(16):
        print(i)
        i=i+e
        p=inicio%5
        if (p == 0):
            sumaTotal+=inicio

    print("El total de las cifras que se dividen en cinco es: ", sumaTotal)


def SerieFibonacci():
    numero = int(input("Ingrese el numero de datos que va a ingresar:"))
    numero = numero - 1
    fibonacci = [0, 1]
    for i in range(2, numero + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print(fibonacci)
        return fibonacci









