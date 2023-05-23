#Leer tres numeros y deducir si se han introducido en orden creciente

print("para saber si sus numeros estan en orden creciente ingreselos aqui ")

var1= int(input("\ncolocar valor 1: "))
var2= int(input("\ncolocar valor 2: "))
var3= int(input("\ncolocar valor 3: "))

if int(var1<var2<var3):
    print ("si esta de forma creciente")
    
else:    
    print("no aplica")
