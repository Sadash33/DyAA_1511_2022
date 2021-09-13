#Implementación busqueda lineal
def busqueda_lineal(lista, m):
  for i in lista:
    if m == i:
      return i
  return -1

lista = [17, 51, 198, 20, 7, 9, 3, 484, 22, 81, 15, 1, 37, 66]
m = 484
l = busqueda_lineal(lista, m)

if l == -1:
  print("Error: Elemento no encontrado")
else:
  print("Elemento encontrado")


  #Implementación ordenación por inserción
  def insert(x):
    for i in range(len(x)):
      for j in range(i, 0, -1):
        if (x[j-1] > x[j]):
          u = x[j]
          x[j] = x[j-1]
          x[j-1] = u
    print(x)

  x = [17, 51, 198, 20, 7, 9, 3, 484, 22, 81, 15, 1, 37, 66]
  print(x)
  insert(x)
