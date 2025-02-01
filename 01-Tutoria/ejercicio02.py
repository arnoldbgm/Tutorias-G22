notas_clase = [
    [14, 15, 12, 11, 16], #Juanito
    [10, 9, 12, 11, 13],  #Marquito
    [16, 18, 15, 14, 17], #Luchito
    [8, 11, 10, 9, 7]  #Andres
]

#RETO:> Quiero que me digan cuantos aprobados hay
# cuantos desaprobados hay (nota para aprobar mayor igual 13)
def promedio_notas_clase(notas_clase):
   # pass => significa que aqui viene codigo
   # nota => elemento
   aprobado = 0
   desprobado = 0
   for nota in notas_clase:
      # Estamos en elm  [14, 15, 12, 11, 16]
      # 14 + 15 +12 +11 + 16 / 5
      promedio = sum(nota) / len(nota)
      print(f"El promedio del alumno es {promedio}")
      if promedio >= 13:
         aprobado += 1
      else:
         desprobado+= 1
   print(f"Aprobados: {aprobado}")
   print(f"Desaprobados: {desprobado}")

promedio_notas_clase(notas_clase)