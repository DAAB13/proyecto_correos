import pandas as pd

### -------- Estación 1: leer y entender los datos ------------
nombre_archivo = 'data/tabla_accesos.xlsx'
try:
  df = pd.read_excel(nombre_archivo) # pandas lee el archivo xlsx
  #print(df.head())
### -------- Estación 2: organizar por instructor ------------
  """ el método .unique sirve para obtener una lista de correo sin repetir """
  correos_intructores = df['Correo Institucional'].unique() 
  #print("---Instructores a contactar---")
  #print(correos_intructores)
except FileNotFoundError:
  print(f"no se encontro el archivo:\n{nombre_archivo}\nAsegurate que exista el archivo")


### -------- Estación 3: Construir mensaje personalizado ------------
for correo in correos_intructores:
  """filtrar datos para un instructor específico"""
  df_instructor = df[df['Correo Institucional'] == correo] 
  print(df_instructor)
  nombre_instructor = df_instructor['Instructor'].iloc[0] #iloc toma la primera fila de la selección
  nombre_mes = df_instructor['Mes'].iloc[0]
  tabla_filtro = df_instructor.drop(columns=['Correo Institucional'])
  
  """ Convertimos la tabla a un formato HTML """
  tabla_html = tabla_filtro.to_html(index = False) #le quitamos el índice

  """ Creamos el cuerpo completo del correo en HTML """
  cuerpo_correo = f"""
  <html>
  <body>
      <p>Estimado(a) {nombre_instructor}</p>
      <p>Te compartimos sus accesos para el mes de {nombre_mes}:</p> 
      {tabla_html}
      <p>Saludos cordiales</p>
  <body>
  <html>
  """
  print(cuerpo_correo)