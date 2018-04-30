ang11=float(input("Ingrese el ángulo 1 del triángulo 1\n"))
lad11=float(input("Ingrese el lado 1 del triángulo 1\n"))
ang12=float(input("Ingrese el ángulo 2 del triángulo 1\n"))
lad12=float(input("Ingrese el lado 2 del triángulo 1\n"))
ang13=float(input("Ingrese el ángulo 3 del triángulo 1\n"))
lad13=float(input("Ingrese el lado 3 del triángulo 1\n"))

ang21=float(input("Ingrese el ángulo 1 del triángulo 2\n"))
lad21=float(input("Ingrese el lado 1 del triángulo 2\n"))
ang22=float(input("Ingrese el ángulo 2 del triángulo 2\n"))
lad22=float(input("Ingrese el lado 2 del triángulo 2\n"))
ang23=float(input("Ingrese el ángulo 3 del triángulo 2\n"))
lad23=float(input("Ingrese el lado 3 del triángulo 2\n"))

if (ang11 == ang21 and ang12 == ang22 and ang13==ang23 and lad11 == lad21 and lad12 == lad22 and lad13==lad23):
    print("Los triángulos, son congruentes")
else:
    print("No son triángulos congruentes")
