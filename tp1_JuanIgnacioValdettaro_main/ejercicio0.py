i1 = 3
i2 = 5
i3 = i2 + i1
print("valor de i1:") #valor de i1:
print(i1) #3
print("valor de i2:") #valor de i2:
print(i2) #5
print("valor de i3:")#valor de i3:
print(i3) #8
print(i1 + i2 + i3) #16-->no lo guarda, se muestra pero la informacion se pierde necesitamos i4=i1 + i2 + i3

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3) #Python is awsome

x = y = z = "Naranja"
print("valor de x: " + x + ", valor de y: " + y + ", valor de z: " + z)#valor de x: Naranja + valor de y: Naranja + valor de z: Naranja
#era , no +
z1 = i3 /i2 #siempre da decimal, aunque sea .0 8/5
print(z1) #1.6
z2 = i3 % i2 
print(z2) #resto de la divicion entera 3
f1 = -.5 #-0.5
f2 = 10
f3 = f1 + f2  #9.5
i3 = int(f3) #9
print("entero i3:")#entero i3:
print(i3) # 8 porque da 9, no entiendo
print("variable f3:") #variable f3:
print(f3) #9.5
f2 += i1 #(es lo mismo que decir f2=f2+i1)
print("el valor de")#el valor de
print(f2) #10-->13
print("más")#más
print(f1) #-0.5
print("es:")#es:
print(f2 + f1)#9.5-->12.5
