#Generar una tabla de multiplicar

def tabla_multiplicar(nro):
   # i < 11
   # 10
   resultado = []
   for i in range(1,11):
      # 1 *  5
      # 2 *  5
      resultado.append(i*nro)
   return resultado

print(tabla_multiplicar(5))