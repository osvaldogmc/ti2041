import pandas as pd

def cargarEvaluacion(nombreArchivo, puntajeTotal, exigencia=60):
    col_names = [
        'rut',
        'nombre',
        'n1',
        'n2',
        'n3',
        'n4',
        'n5',
        'n6',
        'n7',
    ]
    try:
        nombreArchivo = f'''{nombreArchivo}.csv'''
        # Cargamos el fichero de datos
        df = pd.read_csv(nombreArchivo, encoding='ISO-8859-1', sep=';', names=col_names)

        # Filtramos los datos
        for index, row in df.iterrows():
            puntaje = row['n1'] + row['n2'] + row['n3'] + row['n4'] + row['n5'] + row['n6'] + row['n7']
            nota = obtenerNota(0, puntajeTotal, exigencia, puntaje)
            print({
                'rut': row['rut'],
                'nombre': row['nombre'],
                'puntaje': puntaje,
                'nota': round(nota, 1)
            })

    except pd.errors.ParserError as e:
        print('No se pudo cargar el archivo')

def obtenerNota(min, max, exigencia, puntaje):
    aprobacion = min + (max - min) * exigencia / 100

    if puntaje < aprobacion:
        m = (4.0 - 1.0) / (aprobacion - min)
        n = 1.0 - m * min
    else:
        m = (7.0 - 4.0) / (max - aprobacion)
        n = 4.0 - m * aprobacion
    
    nota = m * puntaje + n
    return nota

# Mostramos los datos al 50% y al 60%
archivo = input('Introduce el nombre del archivo: ')
puntaje = int(input('Introduce el puntaje: '))
exigencia = int(input('Introduce la exigencia: '))
cargarEvaluacion(archivo, puntaje, exigencia)