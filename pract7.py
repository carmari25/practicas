
#Pedir 2 valores y en caso de no ser iguales indicar cual es el mayor

var1= int(input("primer valor: "))
var2= int(input("segundo valor: "))

if(var1==var2):
    print("son iguales")
else : 
   if(var1<var2):

    print(" no son iguales y el segundo valor " , var2 ," es mayor")
   else : 
      if(var2<var1):

          print(" no son iguales y el primer valor " , var1 ," es mayor")
         