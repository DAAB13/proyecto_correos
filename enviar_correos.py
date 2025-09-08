import pandas as pd

### -------- Estación 1: leer y entender los datos ------------
nombre_archivo = 'data/tabla_accesos.xlsx'
try:
  df = pd.read_excel(nombre_archivo) # pandas lee el archivo xlsx
  #print(df.head())
### -------- Estación 2: organizar por instructor ------------
  """ el método .unique sirve para obtener una lista de correo sin repetir """
  correos_intructores = df['Correo Institucional'].unique() 
  print("---Instructores a contactar---")
  #print(correos_intructores)
except FileNotFoundError:
  print(f"no se encontro el archivo:\n{nombre_archivo}\nAsegurate que exista el archivo")


### -------- Estación 3: Construir mensaje personalizado ------------
for correo in correos_intructores:
  """filtrar datos para un instructor específico"""
  df_instructor = df[df['Correo Institucional'] == correo] 
  print(df_instructor)
  nombre_instructor = df_instructor['Instructor'].iloc[0] #iloc toma la primera fila de la selección
  tabla_para_correo = df_instructor.drop(columns=['Correo Institucional'])
  print(tabla_para_correo)