"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import sys

def read_csv():
    with open('data.csv', 'r') as data:  
        table = []
        for line in data:
            words = line.split('\t')
            # words += words[4].split(',')
            # words.pop(4)
            words[-1] = words[-1][:-1]
            table.append(words)
    return table

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    
    """
    table = read_csv()
    sum_total = 0
    for row in table:
        number = int(row[1])
        sum_total += number
    return sum_total

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    table = read_csv()
    dictionary = {}
    for row in table:
        letter = row[0]
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    keys = sorted(dictionary)

    sorted_dictionary = {}
    for key in keys:
        sorted_dictionary[key] = dictionary[key]

    final_list = [(key, sorted_dictionary[key]) for key in sorted_dictionary]

    return final_list

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    table = read_csv()
    dictionary = {}
    for row in table:
        letter = row[0]
        value = int(row[1])
        if letter in dictionary:
            dictionary[letter] += value
        else:
            dictionary[letter] = value

    final_dict = {key: dictionary[key] for key in sorted(dictionary)}

    final_list = [(key, final_dict[key]) for key in final_dict]

    return final_list

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    table = read_csv()

    dictionary = {}
    for row in table:
        date_month = str(row[2]).split("-")[1]
        if date_month in dictionary:
            dictionary[date_month] += 1
        else:
            dictionary[date_month] = 1

    date_list = [(key, dictionary[key]) for key in sorted(dictionary)]

    return date_list

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    table = read_csv()

    dictionary = {}
    for row in table:
        letter = row[0]
        number = row[1]
        if letter not in dictionary:  
            dictionary[letter] = [number, number]
        else:
            dictionary[letter][0] = number if (number > dictionary[letter][0]) else dictionary[letter][0]
            dictionary[letter][1] = number if (number < dictionary[letter][1]) else dictionary[letter][1]

    list_values = [(key, int(dictionary[key][0]), int(dictionary[key][1])) for key in sorted(dictionary)]

    return list_values

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """

    table = read_csv()

    dictionary = {}
    for row in table:
        col4 = row[4].split(",")
        for group in col4:
            key, value = group.split(":")  
            value = int(value)    
            if key not in dictionary:  
                dictionary[key] = [value, value]
            else:
                dictionary[key][0] = value if (value < dictionary[key][0]) else dictionary[key][0]
                dictionary[key][1] = value if (value > dictionary[key][1]) else dictionary[key][1]

    list_values = [(key, dictionary[key][0], (dictionary[key][1])) for key in sorted(dictionary)]

    return list_values

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """

    return 

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """

    return 

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    return 

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """

    return 

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """

    return 

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    return 