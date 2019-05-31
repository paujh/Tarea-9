#Jorge Hinostrosa Paula
#paulajhinostrosa@ciencias.unam.mx

import matplotlib.pyplot as plt
import random as r
import math as m 

##Calcular datos 
archivo = open("Datos.txt","r")
archivoa = open("DatosA.txt","w")
nm1 = 0
nh1 = 0
nm2 = 0
nh2 = 0
for linea in archivo: 
  datos = linea.split (",")
  if float(datos[2])>=18.0 and float(datos[2])<=30.0:
    if datos[0]=="Femenino":
      nm1 = nm1 + 1
    else:
      nh1 =  nh1 + 1
  elif float(datos[2])>=31.0 and float(datos[2])<=70.0:
    if datos[0]=="Femenino":
      nm2 = nm2 + 1
    else:
      nh2 =  nh2 + 1
archivoa.write("Numero de mujeres entre 18 y 30 años: " + str(nm1) + "\nNumero de hombres entre 18 y 30 años: " + str(nh1) + "\nNumero de mujeres entre 31 y 70 años: " + str(nm2) + "\nNumero de hombres entre 31 y 70 años: " + str(nh2))
archivo.close() 
archivoa.close()  

#A)
plt.figure()
x = [1,2]
d = [57,94]
plt.bar(x,d,width = 0.5, color = ['m', 'b'])
plt.title("Personas entre 18 y 30 años.")
plt.xticks(x,["Mujeres","Hombres"])
plt.xlabel("Genero",fontsize=15)
plt.ylabel("Cantidad",fontsize=15)
plt.savefig("IncisioA.png")
plt.show() 

#B) 
plt.figure() 
plt.pie([57,94,184,160],autopct='%1.1f%%',colors=['b','g','c','y'])
plt.legend(["Mujeres entre 18 y 30 años.","Hombres entre 18 y 30 años.","Mujeres entre 31 y 70 años.","Hombres entre 31 y 70 años."])
plt.title("Edades de hombres y mujeres.",fontsize=20)
plt.axis('equal')
plt.savefig("IncisoB.png")
plt.show()

#C) 
archivoc = open("Datos.txt","r")
archivoc2 = open("IncisoC.txt","w")
sumaeh = 0.0
nh = 0
suma = 0.0
for linea in archivoc:
  datos = linea.split(",")
  if datos[0]=="Masculino":
    nh = nh +1
    sumaeh = sumaeh + float(datos[3])
for linea in archivoc:    
  datos = linea.split(",")
  if datos[0]=="Masculino":
    nh = nh +1
    sumaeh = sumaeh + float(datos[3])
    suma = suma + (float(datos[3]) - (sumaeh/nh))**2.0

archivoc2.write("El promedio de estatura de hombres es: " + str(sumaeh/nh) + "\nLa deviacion estandar de las estaturas de los hombres es: " + str(m.sqrt(suma/nh)))
archivoc.close()
archivoc2.close()  

#D) 
##Edades de las mujeres
archivod = open("Datos.txt","r")
archivod2 = open("Edadesmujeres.txt","w")
for linea in archivod:
  datos = linea.split(",")
  if datos[0]=="Femenino":
    cadena = datos[2] + ","
    archivod2.write(cadena)
archivod.close()
archivod2.close()

archivof = open("IncisoD.txt","w")
l = [51,18,56,52,56,40,55,22,23,24,25,60,22,56,56,61,26,68,21,35,57,53,39,23,22,48,69,68,52,19,58,40,47,30,31,18,35,37,40,30,53,66,44,57,61,51,35,39,71,40,36,56,55,57,36,64,43,58,63,46,38,56,60,44,63,49,41,41,67,72,70,68,44,59,25,56,31,29,59,63,52,23,43,49,54,40,62,44,60,69,47,25,18,67,50,47,63,57,62,38,63,18,56,70,37,64,53,54,67,52,59,34,72,19,57,29,67,36,28,49,70,56,51,67,57,55,47,59,23,66,32,25,58,51,67,61,35,46,46,29,32,51,39,26,52,22,30,27,65,28,30,30,35,56,24,41,42,38,65,62,66,45,32,35,40,38,47,34,60,36,33,60,48,51,24,45,63,27,67,34,18,47,55,38,51,52,64,20,62,67,65,48,24,28,29,27,40,68,18,68,60,22,30,43,72,28,39,70,71,24,46,18,18,62,52,63,37,57,47,34,65,65,23,20,53,35,54,24,30,54,35,48,55,51,57,39,20,57,18,58,30,64,42,41,42,24]
l.sort()
n = len(l)
if n%2==1:
  m = l[n//2]
else:
  m = (l[n//2] + l[(n//2)-1])/2.0
d = {}
for i in l:
  if i in d:
    d[i] = d[i] + 1
  else:
    d[i] = 1
maxRep = 0
eleMasRep = l[0]
for i in d:
  if d[i] > maxRep:
    maxRep = d[i]
    eleMasRep = i
mx = eleMasRep
archivof.write("La mediana de la edad de las mujeres es: " + str(m) + "\nLa moda de la edad de las mujeres es: " + str(mx))
archivof.close()
