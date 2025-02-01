def promedio_notas(notas):
    ## FISICA => 14 , 15 , 12, 11 ,16
    ##  (14 + 15 + 12 + 11 + 16 ) / 5
    ## Suma de todos los elm / nro de elmts
    promedio = sum(notas) / len(notas)
    if promedio >= 13:
        print(f"El alumno aprobo con un promedio {promedio}")
    else:
        print(f"El alumno desaprobo con un promedio {promedio}")

notas_alumno_Juanito = [14, 15, 5, 8, 16]
promedio_notas(notas_alumno_Juanito)

notas_alumno_Marquito = [14, 15, 15,18, 16]
promedio_notas(notas_alumno_Marquito)

notas_alumno_Luchito = [14, 15, 15,20, 16]
promedio_notas(notas_alumno_Luchito)

notas_alumno_Luchito = [14, 15, 15,20, 16]
promedio_notas(notas_alumno_Luchito)