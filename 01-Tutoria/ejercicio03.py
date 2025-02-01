def filtrar_pares(numeros):
   # pares = []
   # for num in numeros:
   #    if num % 2 == 0:
   #       pares.append(num)
   # return pares

   # Reducir en una linea
   return [num for num in numeros if num % 2 == 0]

lista_numeros = [10, 23, 45, 12, 8, 3, 19]
print(filtrar_pares(lista_numeros))  # Salida: [10, 12, 8]
