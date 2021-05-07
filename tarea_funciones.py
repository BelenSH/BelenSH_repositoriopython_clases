print(" Area y Perimetros de Figuras Geometricas ")

print(" ")

tri="1. Triangulo"
cua="2. Cuadrado"
cir="3. Circulo"
rec="4. Rectangulo"
print(tri)
print(cua)
print(cir)
print(rec)

print(" ")
lim=1
while lim<=1:
 numero=int(input("Ingresa el numero elegido:"))

 print(" ")


 def funcionCalcular ():
      if numero==1:
             print(tri)
             lado=int(input("Ingresa el lado del triangulo: ")) 
             p=lado+lado+lado
             base=int(input("Ingresa la Base del triangulo: "))
             altura=int(input("Ingresa la altura del triangulo: "))
             area=(base*altura)/2
             print("El perimetro del triangulo es: "+ str(p))
             print("El area del triangulo es: "+ str(area))
      elif numero==2:
               lado=int(input("Ingresa el lado del triangulo: "))
               p=lado+lado+lado+lado
               area=lado*lado
               print("El perimetro del triangulo es: "+ str(p))
               print("El area del triangulo es: "+ str(area))
      elif numero==3:
              radio=int(input("Ingresa el radio del circulo: "))
              area = int(3.1416*radio*radio)
              perimetro = int(2*3.1416*radio)
              print("El perimetro del Circulo es:" + str(perimetro))
              print("El area del Circulo es: "+ str(area))
      elif numero==4:
              baser=int(input("Ingresa la base del rectangulo: "))
              alturar=int(input("Ingresa la altura del rectangulo: "))
              ar=baser*alturar
              pr= baser+baser+alturar+alturar
              print("El perimetro del Rectangulo es:" + str(pr))
              print("El area del Rectangulo es: "+ str(ar))
      else:
             print("La opcion elegida no esta disponible intentelo nuevamente ")
 
 funcionCalcular() 
 print("")
 salir=(input("Desea salir? De clic en la tecla a o A o escriba no : "))
 if salir=="a" or salir=="A":
                break
