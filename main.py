import pandas as pd

# Lista de edades de 30 alumnos de segundo año de Software.
edades = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28 ,18,19,20,21,22,23,24,25,26,27,28, 19, 30, 34,34, 21, 24, 22, 26]

# Función que recibe la lista de edades y devuelve un DataFrame con un análisis básico.
def analisis_estadistico(edades: list):
    if type(edades) != list:     # Se verifica que los datos ingresados sean una lista.
        return "Los datos deben ser una lista"
    if not edades:               # Se verifica que la lista no esté vacía.
        return "La lista no debe estar vacía"
    for i in edades:             # Se verifica que los elementos de la lista sean numéricos.
        if type(i) != int and type(i) != float:
            return "Todos los elementos de la lista deben ser numéricos"
   
   # Se crea el DataFrame con los datos de la lista y se realiza el análisis.
    data_frame = pd.DataFrame(edades, columns=["Edad"])                   # Se crea el DataFrame con los datos de la lista.
    data_frame = data_frame.groupby("Edad").size().reset_index(name="fi") # Se agrupan los datos y se cuenta la frecuencia de cada uno.
    data_frame["Fi"] = data_frame["fi"].cumsum()                          # Se calcula la frecuencia acumulada.
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()          # Se calcula la frecuencia relativa.
    data_frame["Ri"] = data_frame["ri"].cumsum()                          # Se calcula la frecuencia relativa acumulada.
    data_frame["pi%"] = data_frame["ri"] * 100                            # Se calcula la frecuencia relativa en porcentaje.
    data_frame["Pi%"] = data_frame["pi%"].cumsum()                        # Se calcula la frecuencia relativa acumulada en porcentaje.
    return data_frame                                                     # Se devuelve el DataFrame con el análisis.

print(analisis_estadistico(edades))


