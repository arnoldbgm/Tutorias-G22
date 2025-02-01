[<img src="https://daiderd.com/nix-darwin/images/nix-darwin.png" width="200px" alt="logo" />](https://github.com/LnL7/nix-darwin)

### Ejercicio 1: Promedio de Notas

**Descripción:**
Crea una función llamada `promedio_notas` que reciba una lista de enteros que representan las notas de un alumno y devuelva el promedio de esas notas. La función debe también imprimir un mensaje indicando si el alumno aprobó o no. Se considera que el alumno aprueba si su promedio es mayor o igual a 13.

**Ejemplo:**

```python
def promedio_notas(notas):
    ## AQUI VA TU CODIGO
    pass

notas_alumno = [14, 15, 12, 11, 16]
promedio_notas(notas_alumno)

```

**Resultado esperado:**

```
El alumno aprobó con un promedio de 13.60

```

---

### Ejercicio 1 para Alumnos: Promedio de Notas por Clase

**Descripción:**
Crea una función llamada `promedio_notas_clase` que reciba una lista de listas, donde cada sublista contiene las notas de un alumno. La función debe devolver el promedio de cada alumno y el promedio de toda la clase. Además, debe imprimir cuántos alumnos aprobaron y cuántos no.

**Ejemplo:**

```python
def promedio_notas_clase(notas_clase):
    ## AQUI VA TU CODIGO
    pass

notas_clase = [
    [14, 15, 12, 11, 16],
    [10, 9, 12, 11, 13],
    [16, 18, 15, 14, 17],
    [8, 11, 10, 9, 7]
]
promedio_notas_clase(notas_clase)

```

**Resultado esperado:**

```
Promedio del alumno: 13.60
Promedio del alumno: 11.00
Promedio del alumno: 16.00
Promedio del alumno: 9.00

Promedio de toda la clase: 12.40
Alumnos aprobados: 2
Alumnos desaprobados: 2

```

---

### Ejercicio 2: Filtrar Números Pares

**Descripción:**
Crea una función llamada `filtrar_pares` que reciba una lista de números enteros y devuelva una nueva lista con solo los números pares.

**Ejemplo:**

```python
def filtrar_pares(numeros):
    ## Aqui va tu codigo
    pass

lista_numeros = [10, 23, 45, 12, 8, 3, 19]
print(filtrar_pares(lista_numeros))  # Salida: [10, 12, 8]

```

**Resultado esperado:**

```
[10, 12, 8]

```

---

### Ejercicio 2 para Alumnos: Filtrar Números Impares y Contar

**Descripción:**
Crea una función llamada `filtrar_y_contar_pares` que reciba una lista de números enteros. La función debe devolver una nueva lista con solo los números impares y también el total de números impares encontrados.

**Ejemplo:**

```python
def filtrar_y_contar_pares(numeros):
   ## Aqui va tu codigo
   pass

lista_numeros = [10, 23, 45, 12, 8, 3, 19]
print(filtrar_y_contar_pares(lista_numeros))
```

**Resultado esperado:**

```
Números impares: [23, 45, 3, 19]
Cantidad de números impares: 4

```

---

### Ejercicio 3: Generar Tabla de Multiplicar

**Descripción:**
Crea una función llamada `tabla_multiplicar` que reciba un número entero `n` y genere una lista con la tabla de multiplicar de ese número desde 1 hasta 10.

**Ejemplo:**

```python
def tabla_multiplicar(n):
    ## Aqui va tu codigo
    pass

print(tabla_multiplicar(5))  # Salida: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

```

**Resultado esperado:**

```
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

```

---

### Ejercicio 3 para Alumnos: Generar Tablas de Multiplicar

**Descripción:**
Crea una función llamada `tablas_multiplicar_hasta` que reciba un número entero `m` y genere una lista de listas, donde cada sublista es la tabla de multiplicar desde 1 hasta `m`.

**Ejemplo:**

```python
def tablas_multiplicar_hasta(m):
    ## Aqui va tu codigo
    pass

print(tablas_multiplicar_hasta(3))
# Salida:
# [
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
#  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# ]

```

**Resultado esperado:**

```
[
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
 [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
]

```

---

### Ejercicio 4: Encontrar Palabras con Más de 5 Letras

**Descripción:**
Crea una función llamada `palabras_largas` que reciba una lista de palabras y devuelva una nueva lista con solo las palabras que tienen más de 5 letras.

**Ejemplo:**

```python
def palabras_largas(lista_palabras):
    ## Aqui va tu codigo
    pass

palabras = ["python", "es", "genial", "para", "programar"]
palabras_largas(palabras)  # Salida: ['python', 'genial', 'programar']

```

**Resultado esperado:**

```
['python', 'genial', 'programar']

```

---

### Ejercicio 4 para Alumnos: Palabras con Más de 5 Letras y Contar

**Descripción:**
Crea una función llamada `filtrar_y_contar_palabras_largas` que reciba una lista de palabras. La función debe devolver una nueva lista con solo las palabras que tienen más de 5 letras y también el total de estas palabras.

**Ejemplo:**

```python
def filtrar_y_contar_palabras_largas(lista_palabras):
    ## Aqui va tu codigo
    pass

palabras = ["python", "es", "genial", "para", "programar"]
filtrar_y_contar_palabras_largas(palabras)
```

**Resultado esperado:**