import os

os.system("cls")
#Elegir una tematica de un negocio que vende 3 productos
productos=["helado","coca","doritos nacho"]
precios=[75,25,20]

#Funcion para calcular el total
def calcular_total(cantidades,precios):
    total=0
    for i in range (len(cantidades)):
        total+=cantidades[i]*precios[i]
    return total

#Menu de usuario
salida=False
while(salida!=True):
    print("---- Tienda ----\n")
    print("Sistema para calcular los precios")
    nombre=input("Ingresar tu nombre ‣ ")
    try:
        descuento=int(input("Ingrese la cantidad de descuento para este usuario ‣ "))
    except ValueError:
        os.system("cls")
        print("Ingrese solo valores numericos de porcentaje para asignar un descuento ...")
        os.system("pause")
        os.system("cls")
        continue 

    cantidades=[]
    print("\nSelecciona tu pedido:")
    verif=False
    for i in range(len(productos)):
        print(f"\n{i+1}. {productos[i]} - ${precios[i]}")
        try:
            cantidad=int(input(f"Cuantos {productos[i]} quieres? "))
            cantidades.append(cantidad)
        except ValueError:
            os.system("cls")
            print("Ingrese solo valores numericos para la cantidad de productos a comprar...")
            os.system("pause")
            os.system("cls")
            verif=True
            break
    if verif==True:
        continue

    total=calcular_total(cantidades,precios)

    os.system("cls")

    #Imprimir tiket
    print("\n\t\t---------------------- super xd ---------------------------")
    print(f"\n\t\t|  Usuario referido: {nombre}\n")
    print(f"\t\t{'-'*59}\n")
    for i in range(len(productos)):
        if(cantidades[i]!=0):
            print(f'{f"\t\t|  {productos[i]} ‣ precio({precios[i]}) ":<35}'+f"| unidades compradas: {cantidades[i]}")
    print(f"\n\t\t{'-'*59}\n") 
    print(f"\t\t|  Subtotal: {total}")
    print(f"\t\t|  Descuento ({descuento}%)* : {(total*descuento)/100}")
    print(f"\t\t|  Total a pagar: {total-((total*descuento)/100)}")  
    print(f"\n\t\t{'-'*59}") 
    print("")
    salida=True