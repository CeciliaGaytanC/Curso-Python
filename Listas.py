# Las listas  son el equivalente a los arrays, estructura de datos que guarda cant. de valores
# Es como una variable que guarda un valor a diferencia que la lista tiene varios espacios para guardar varios valores

# Sintaxis:
# nombreLista =[elem1, elem1, elem3]
# Empieza desde 0-1-2-3..... y si contamos desde el final hacia el principio, se lee como negativo,
# Los valores pueden ser de cualquir tipo
# los valores son elem1, elem2, elem3
# Test
miLista=["Ana", "Cecilia", "Jose"]

# Lo que se hace es imprimir la posicion 1, entonces imprime "Cecilia"
print(miLista[1])
# Si queremos ver todos los valores, le pondemos un ":"
print(miLista[:])
# Tambien podemos mostrar un rango de valor, por ejemplo
print(miLista[0:2])

# Se pueden sumar las listas
miLista1=["Maria", "Paloma"]

miLista3= miLista+miLista1
print(miLista3)
# Y tambien se puede repetir
miLista1=["Maria", "Paloma"] *2
print(miLista1)
