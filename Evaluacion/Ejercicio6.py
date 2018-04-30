mes = int(input("Ingrese el  mes \n"))
if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    print("El mes {0}, tiene 31 días".format(mes))
else:
    if(mes==4 or mes==6 or mes==9 or mes==11):
       print("El mes {0},tiene 30 días".format(mes))
    else:
        if(mes==2):
             print("El mes {0},tiene 28 días".format(mes))
        else:
                print("El mes {0},es incorrecto".format(mes))
