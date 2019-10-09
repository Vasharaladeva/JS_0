milista  = []
numero = ""
while numero != 0:
    numero = float(input("que numero?"))
    milista.append(numero)
    for i in milista:
        print(i)
print(milista)

milista.sort()
print(milista)
milista.sort(reverse=True)
print(milista)



ca = 0
ce = 0
ci = 0
co = 0
cu = 0

texto = input("que texto?")
for i in  texto:
    print(i)
    if i == "a" :
        ca = ca+1
    if i == "e" :
        ce = ce+1
    if i == "i" :
        ci = ci+1
    if i == "o" :
        co = co+1
    if i == "u" :
        cu = cu+1
print("A:",ca)
print("E:",ce)
print("I:",ci)
print("0:",co)
print("U:",cu)

t0 = ""
t1 = input("que texto")

for i in t1:
    print(i)
    t0=i+t0
print(t0)
if t1 == t0:
    print("Palindro")
else:
    ("No Palindro")



n = int(input("que numero"))
x = n
r = 0
while n != 0:
    n2 = n // 10
    n2 = n2 * 10
    d = n -n2
    print(d)
    r = r*10 + d
    n = n // 10
print(r)
if (x==r):
    print("Capicua")
else:
    print("No capicua")



#reynaldozeballos@gmail.com


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
print(is_prime(4))

# numeros primos
a  = 0

while a < 10:

    a += 1

    if a % 2 == 0:
        continue
        
    print(a)

#multiplos

def multiplos_hasta_limite(numero, limite):
    multiplos = []

    i = 1
    multiplo = numero

    while multiplo <= limite:
        multiplos.append(multiplo)

        i += 1

        multiplo = numero * i
    return multiplos
m = multiplos_hasta_limite(12 , 100)
print(m)

#fibonacci

def fib(n):

    a,b = 0, 1
    while a< n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

#fibonacci 2

def fib2(n):

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(2000))


#escribe lo que le das
def ask_ok(prompt, retries=4, reminder='pleace tryagain'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no','nop','nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('nope')

# prmios


def es_primo(n):
    for i in range (2,n):
        if n % i == 0: return False
        return True


    
print(es_primo(67))

#divisores de una lista

a  = 0

while a < 200:

    a += 1

    if a % 5 :
        continue


    print(a)

#

def main():
    print("DIVISORES")
    numero = int(input("Escriba un número entero mayor que cero: "))

    if numero <= 0:
        print("¡Le he pedido un número entero mayor que cero!")
    else:
        print(f"Los divisores de {numero} son ", end="")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")


if __name__ == "__main__":
    main()


#ejercicios de programacionn1

n1 = int(input("numero uno :"))
n2 = int(input(("numero dos :")))
if n1==n2:
    print("son iguales")

elif n1 > n2:
    print(n1, "es el mayor")



else:
    print(n2,"es el mayor")

#ejercicios de programacionn1

n1 = int(input("numero 1"))
n2 = int(input("numero 2"))
n3 = int(input("numero 3"))

if n1 == n2 == n3:
    print("son iguales")
else:
    if n1>n2:
        m=n1
    else:
        m=n2
    if m>n3:
        print(m,"es el mayor")
    else:
        print(n3,"es el maoyor")

#len mide el largo
texto=input("introdusca")

c=0
for i in texto:
    c=c+1
print("el largo es: ",c)        

#el 4

texto = input("introdusca un caracter")
if texto == "a":
    print("es la vocal")
elif texto =="e":
    print("es la vocal e")
elif texto =="i":
    print("es la vocal e")
elif texto =="i":
    print("es la vocal o")
elif texto =="i":
    print("es la vocal u")
else:
    print("no es una vocal")

#el

t = input("lee el texto")

if t == "a" or t == "e" or t =="i" or t == "o" or t == "u":
    print("es vocal", t)
else:
    print("no es vocal")

#sumar y multiplicar la lista

list = [4,7,3,9,5]

print(list)

s= 0
mu =1
for i in list:
    s = s+i
    mu = mu*i
print ("la suma es", s)
print ("la multli es", mu)

#la reversa

text = input("introdusca el texto")
r=""
for  i in text:
    print(i)
    r = i+r
print(r)
#reverso 
def rev(texto):
    r=""
    for i in texto:
        r=i+r
    print(r)
rev("bolivia")

#palindro

def rev(texto):
    r=""
    for i in texto:
        r=i+r
    return r
def pali(texto):
    tr = rev(texto)
    if texto == tr:
        print("palindro")
    else:
        print("no palidro")
pali("hola")

#comparar su lista
lista1 = [2,4,3]
lista2 = [7,8,9]
lista3 = [4,6,7]

def tiene_uno(lista1,lista2):
    esta = False
    for i in lista1:
        for k in lista2:
            if i == k:
                esta =True
    return esta
print(tiene_uno([2,4,3],[7,8,9,10]))
print(tiene_uno([2,4,3],[4,6,7]))

#generar caracteres

def gen_n_car(num,car):
    r=""
    for i in range(num):
        r=r+car
    print(r)
gen_n_car(3,"*")
gen_n_car(10,"X")

#generar caracteres



def procedimiento(lista):

    for i in lista:
        print(i*"^")
procedimiento([4,9,7])

#lista mas grande



def procedimiento(lista):
    m = -1
    for i in lista:
        if i > m:
            m = i


    print("el mayor es ",m )
    r =""
    c=""
    for i in lista:
        r=i*"*"
        r=r+(m - i)*"o"
        print(r)
        c=c+r
    print(c)

procedimiento( [4,9,7])
#
def max_lis(lista):
    m = lista[0]
    for i in lista:
        if i > m:
            m = i
    print(m)

max_lis([2,4,6])

#

def mas_larga(texto1,texto2):
    t1 = len(texto1)
    t2 = len(texto2)
    if t1 > t2:
        print(texto1)
    elif t1 == t2:
        print("son iguales")
    else:
        print(texto2)

mas_larga("hola","hola")

#def contar_letra(palabra, letra):
    c=0
    for i in palabra:
        if i.lower() ==letra.lower():
            c=c+1
    print(c)
contar_letra("bolivia","a")
contar_letra("Astronauta","A")
contar_letra("salid","p")

#contar vocales

def contar_vocales(palabra):
    c=0
    for i in palabra:
        if i in "aeiouAEIOU":
            c=c+1
    print(c)
contar_vocales("Bolivia")

# contruir binarios barrer al revez

def adecimal(binario):
    base = 1
    r=1
    for i in range(len(binario)-1,-1 ,-1):
        n = int(binario[i])
        r = r+base*n
        base = base*2
    print(r )
adecimal("00111111")


# contruir binarios barrer al revez

def binario(decimal):
    print(bin(decimal)[2:])
binario(255)

#escribir un pequenio programa
def Calcule_edad(nombre,anio):


    gestion = 2019
    edad = gestion - anio
    print("cumple",edad,"anios" )

qnombre=input("introduzca u nombre: ")
qanio=int(input("anio de nacimiento"))
Calcule_edad(qnombre,qanio)

#escribir un pequenio programa
def verifica_edade(edades):
    c=0
    for i in edades:
        if i > 20:
            c=c+1
    print("hay, ", c, "edades")
verifica_edade([12,43,65,12,11])

#escribir un anio viviesto

def esbisiesto(anio):
    if anio % 400 == 0 :
        print(anio,"es biciesto")
    else:
        if anio % 4 == 0 and anio % 100 != 0:
            print(anio,"es biciesto")
        else:
            print(anio,"no es llo siento")

esbisiesto(2000)
esbisiesto(2020)
esbisiesto(2024)
esbisiesto(2015)

#juego de dados

from random import  randint
d1 = randint(1,6)
d2 = randint(1,6)

s=d1+d2
print(d1,"  ",d2)
if s==7:
    print("ganaste")
else:
    print("el objetivo es:",s)
    while True:

        d1 = randint(1, 6)
        d2 = randint(1, 6)
        print(d1, "  ", d2)
        ns = d1+d2
        if ns==s:
            print("ganaste")
            break
        if ns==7:
            print("perdiste")
            break

#rimas 

texto = "bolivia"


def riman(p1,p2):
    u1=p1[-3:]
    u2=p2[-3:]
    if u1 == u2:
        print("riman")
    else:
        u1=p1[-2:]
        u2=p2[-2:]
        if u1 == u2:
            print("riman poco")
        else:
            print(("no riman"))
riman("juana","lana")
riman("vivir","sentir")

#anio bisiesto

n = int(input())
if n >= 1800 and n <= 9999:

    if n % 400 == 0:
        print("si")
    else:
        if n % 4 == 0 and n % 100 != 0:
            print("si")
        else:
            print("no")

#SUMAR EL DIGITO DE UN NUMERO

#el juego de gariel problema g
s, e = 0, 0

n = int(input())
while n != 0:
    e = n % 10
    n //= 10
    s += e
print(s)


#el juego de gariel problema g

n = int(input())
for i in range (n):
    a,b=input().split()
    s1 = 0
    for i in a:
        s1=s1+int(i)
    s2 = 0
    for i in b:
        s2=s2+int(i)
    if s1>s2: print(s1)
    else: print(s)

#el juego de ender

n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    r="nadie"
    m=0
    if a % 2==0:
        if a>m:
            r="ender"
            m=a
    if b % 2==0:
        if b > m:
            r = "petra"
            m=b
    if c % 2==0:
        if c > m: r = "bonzo"
    if a ==m and b==m:
        r="nadie"
    if a==m and c==m:
        r="nadie"
    if b==m and c==m:
        "nadie"
    print(r)

    #JURGO CEBOLLITAS

n = int(input())
for i in range (1,n+1):
    nj,de,np=map(int,input().split())
    while np>0:
        de=de+1
        np=np-1
        if de>nj: de=1
    r="Case "+str(i)+":"
    print(r,de)


#cusrso python ejercicio mesclar en base de dos
#2 binarios
n1,n2=map(int,input().split())


b1=bin(n1)[2:]
b2=bin(n2)[2:]

r=""
for i in range (len(b1)):
    r=r+b1[i]+b2[i]
print(r)

#anio bisiesto con meses
t=int(input())
for i in range (t):
    mensaje ="Fecha correcta"
    d,m,a=map(int,input().split())
    if d<1 or d>31 or m<1 or m>12:
        mensaje="Fecha incorrecta"
    if m in (4,6,9,11) and d>30:
        mensaje="Fecha incorrecta"
    if d > 29 and m == 2:
        mensaje ="Fecha incorrecta"
    if d == 29 and m == 2:
        if a%400!=0:
            if a%4==0 and a%100!=0:
                mensaje ="Fecha correcta"
            else:
                mensaje ="Fecha incorrecta"

    print(mensaje)


#nuevas clases con el otro profesor 
#numero inpar con comas
n = int(input("cual es el numero"))
for i in range (1,n+1, 2):

    print(i, end=",")