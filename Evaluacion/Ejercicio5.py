calf1= float(input("Ingrese la calificación 1\n"))
calf2= float(input("Ingrese la calificación 2\n"))
calf3= float(input("Ingrese la calificación 3\n"))
calf4= float(input("Ingrese la calificación 4\n"))
prom= ((calf1 + calf2 + calf3 + calf4) / 4)
if(prom >= 90 and prom <= 100):
    print("El estudiante con un promedio de: {0}, tiene una puntuacion de A\n".format(prom))
else:
        if(prom >= 80 and prom <= 89):
            print("El estudiante con un promedio de: {0}, tiene una puntuación B\n".format(prom))
        else:
                if(prom >= 70 and prom <= 79):
                    print("El estudiante con un promedio de: {0}, tiene una puntuación C\n".format(prom))
                else:
                        if(prom >= 0 and prom <= 69):
                            print("El estudiante con un promedio de: {0} ,tiene una puntuación D\n".format(prom))

                        
