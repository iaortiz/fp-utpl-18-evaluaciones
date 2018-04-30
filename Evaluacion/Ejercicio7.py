ventas = float(input("Ingrese el número de ventas\n"))
sueldo = 360.40

if (ventas <= 500):
    porcent = ventas * 0.05
    sueldo = sueldo + porcent;
    print("El sueldo total es: {0}".format(sueldo))          
else:
    if (ventas > 500 and ventas <= 1000):
        porcent = ventas * 0.08;
        sueldo = sueldo + porcent;
        print("El sueldo total es: {0}".format(sueldo)) 
    else:
        if (ventas > 1000 and ventas <= 5000):
            porcent = ventas * 0.1;
            sueldo = sueldo + porcent;
            print("El sueldo total es: {0}".format(sueldo))
        else:
            if (ventas > 5000):
                porcent = ventas * 0.15;
                sueldo = sueldo + porcent;
                print("El sueldo total es: {0}".format(sueldo))
                     
                        
