
# 2. Recorre la lista con un ciclo for,
#    si el trabajo es mayor o igual a 10 dólares,
#    entonces suma ese dinero en un contador.


dinero1=200
dinero2=5000
dinero3=5
dinero4=100
dinero5=10
 
 
ListaUsd=[dinero1,dinero2,dinero3,dinero4,dinero5]


def sumar(ListaUsd):
  contador = 0
  for elemento in ListaUsd:
     if elemento >= dinero5:
        contador += elemento
  return contador

# 3. Muestra cuánto dinero podes ganar en total,
#    si sólo aceptas hacer los trabajos de 10 dólares o más.

SumaResultado=sumar(ListaUsd)
print(SumaResultado)




