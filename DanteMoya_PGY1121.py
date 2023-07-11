import numpy as np

depa = 0
dep = np.empty((10,4), dtype= object)
for p in range ((10)):
    for d in range ((4)):
        depa += 1
        dep [p][d] = depa

pre = {1: 38000, 2: 3000, 3: 2800, 4: 3500,
         5: 38000, 6: 3000, 7: 2800, 8: 3500,
         9: 38000, 10: 3000, 11: 2800, 12: 3500,
         13: 38000, 14: 3000, 15: 2800, 16: 3500,
         17: 38000, 18: 3000, 19: 2800, 20: 3500,
         21: 38000, 22: 3000, 23: 2800, 24: 3500,
         25: 38000, 26: 3000, 27: 2800, 28: 3500,
         29: 38000, 30: 3000, 31: 2800, 32: 3500,
         33: 38000, 34: 3000, 35: 2800, 36: 3500,
         37: 38000, 38: 3000, 39: 2800, 40: 3500}

venta = {}

def com():
    depa =int(input("que edificio desea comprar: "))
    print(" ")
    if depa > 0 and depa < 41:
        if depa in venta:
            print("el departamento no esta disponible")
            print(" ")
        else:
            rut = int(input("ingrese su rut sin puntos ni guion y sin digito verificador: "))
            print(" ")
            print("la compra a sido un exito")
            print(" ")
            venta[depa] = rut
    else:
        print("a ingresado un dato erroneo")
        print(" ")

def dispo():
    esta = np.copy(dep)
    for p in range ((10)):
        for d in range ((4)):
            depa = esta [p][d]
            if int(depa) in venta:
                depa [p][d] = 'x'
    print(esta)
    print(" ")

def compradores():
    comprador = list(venta.items())
    comprador.sort
    for depa, rut in comprador:
        print(f"rut: {rut} departamento: {depa}")
    print(" ")

def ventas():
    ganancias = 0
    for depa in venta:
        ganancias += pre[depa]
    print(f"ganancias totales : ${ganancias}")
    print(" ")

flag = True
print("ingrese su nombre")
nombre = input()
print("ingrese su apellido")
apellido = input()
print("ingrese la fecha")
fecha = str(input())
print(" ")
while flag:
    print("-----menu-----")
    print("1) comprar un departamento")
    print("2) ver departamentos disponibles")
    print("3) ver compradores")
    print("4) ver ganacias totales")
    print("5) salir del sistema")
    opc = int(input("elija una opcion: "))
    print(" ")
    if opc == 1:
        com()
    elif opc == 2:
        dispo()
    elif opc == 3:
        compradores()
    elif opc == 4:
        ventas()
    elif opc == 5:
        flag = False
    else:
        print ("el dato ingresado no es valido")
        print(" ")
print("--------------------")
print(f"{nombre} {apellido} a salido del sistema el {fecha}")
print("--------------------")