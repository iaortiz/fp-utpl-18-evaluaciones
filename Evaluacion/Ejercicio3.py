num = int(input("Ingrese la cantidad de segundos"))
hor= int(num / 3600)
minu= int((num - (3600 * hor)) / 60)
seg = int(num - ((hor * 3600) + (min * 60)))
print("La cantidad de minutos es: ",minu," y segundos es: ",seg)

