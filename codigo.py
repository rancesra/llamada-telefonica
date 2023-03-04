print("-------------------------------")
print("-------llamada telefonica------")
print("-------------------------------")
# input
duracion = int(input("digite los minutos de la llamada: "))

# condicion --- resultado
if (duracion < 3):
    print("la llamada tiene un costo de 300 pesos")
else:
    rta = (duracion-3)
    total = (rta * 50)+300
    print("el costo total de la llamada es: " + str(total))
    
print("-----------------------------------------------")
print("-----------costo total de la llamada-----------")
print("-----------------------------------------------")