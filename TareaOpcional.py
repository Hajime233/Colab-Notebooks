# Para la lista1 que tiene los montos en dólares de cada trabajo.

# 1. Carga la lista pidiendo que el usuario
#    ingrese por teclado los 5 valores



dinero1=200
dinero2=5000
dinero3=5
dinero4=100
dinero5=10



listaUSD= []

for elemento in range(5):
  valor=input(f"{elemento} - Ingrese el numero ")
  if int(valor)>0:
    listaUSD.append(valor)

print(listaUSD)
