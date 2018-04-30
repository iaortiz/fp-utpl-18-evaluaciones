v1=input("Ingrese la primera letra\n")
v2=input("Ingrese la segunda letra\n")
v3=input("Ingrese la tercera letra\n")

if v1<v2 and v1<v3:
    print("La primera letra es: %s"%(v1))
else:
    if v2<v1 and v2<v3:
     print("La primera letra es: %s"%(v2))
    else:
        if v3<v1 and v3<v2:
          print("La primera letra es: %s"%(v3))

        
    
