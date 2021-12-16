import csv
import pandas as pd
import os


def leer_csv(path, lista):
    """Se lee el csv de entrada y lo guarda en una lista"""
    try:
        with open(path) as csvfile:
            exampleReader = csv.reader(csvfile, delimiter='|')
            for row in exampleReader:
                lista.append(row)
    except IOError:
        print("ERROR: no se encuentra el archivo " +path)

    return lista


def escribir_csv(path, lista):
    """Escribe un CSV con los datos de la lista origen"""
    with open(path, 'w', newline='') as csvfile:
        outputWriter = csv.writer(csvfile, delimiter='|')
        outputWriter.writerows(lista)


current_directory=os.getcwd()

path_alumnos=current_directory+"/alumnos.csv"
header_alumnos= ['dni', 'nombre', 'apellido', 'email', 'fecha_ingreso','carrera']
listaAlumnos=[]

path_notas=current_directory+"/notas.csv"
header_notas= ['dni', 'materia', 'nota']
listaNotas=[]

path_out=current_directory+"/alumnos_notas.csv"


listaAlumnos=leer_csv(path_alumnos, listaAlumnos)
listaNotas=leer_csv(path_notas, listaNotas)

dfAlumnos = pd.DataFrame(listaAlumnos, columns=header_alumnos)
dfNotas = pd.DataFrame(listaNotas, columns=header_notas)

#Se realiza inner join entre ambos files
join=pd.merge(dfAlumnos,dfNotas,on='dni')

listaMerge=join.values.tolist()

#Se genera nuevo CSV con resultado del join
escribir_csv(path_out,listaMerge)