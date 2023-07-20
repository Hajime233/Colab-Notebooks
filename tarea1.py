        
# A partir de lista1 con los montos de dinero por trabajo
# Quiero mostrar solamente los últimos 3 trabajos de la lista

dinero1=200
dinero2=5000
dinero3=5
dinero4=100
dinero5=1






lista1 = [dinero1, dinero2, dinero3, dinero4, dinero5]

for elemento in range(2,5):
  print(lista1[elemento])




#Lo mismo pero con el While


dinero1=200
dinero2=5000
dinero3=5
dinero4=100
dinero5=1



lista1 = [dinero1, dinero2, dinero3, dinero4, dinero5]
minimo= 1

contador=2
while contador <= 4 :
  valor = lista1[contador]
  if  valor >= minimo:
    print(valor)
  contador += 1
