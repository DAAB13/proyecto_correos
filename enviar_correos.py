import pandas as pd
import config
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

### -------- ESTACIÓN 1: LEER Y ENTENDER LOS DATOS ------------
load_dotenv()
mi_correo = "diego.alvarado@upch.pe"
mi_contraseña = os.getenv("GMAIL_APP_PASSWORD")

try:
  df = pd.read_excel(config.NOMBRE_ARCHIVO) # pandas lee el archivo xlsx
  #print(df.head())

### -------- ESTACIÓN 2: ORGANIZAR POR INSTRUCTOR ------------
  """ el método .unique sirve para obtener una lista de correo sin repetir """
  correos_intructores = df['Correo Institucional'].str.strip().str.lower().unique() 
  #print("---Instructores a contactar---")
  #print(correos_intructores)
except FileNotFoundError:
  print(f"no se encontro el archivo:\n{config.NOMBRE_ARCHIVO}\nAsegurate que exista el archivo")
  exit()


### -------- ESTACIÓN 3: CONSTRUIR MENSAJE PERSONALIZADO ------------
for correo in correos_intructores:
  """filtrar datos para un instructor específico"""
  df_instructor = df[df['Correo Institucional'].str.strip().str.lower() == correo] 
  print(df_instructor)
  nombre_instructor = df_instructor['Instructor'].iloc[0] #iloc toma la primera fila de la selección
  nombre_mes = df_instructor['Mes'].iloc[0]
  tabla_filtro = df_instructor.drop(columns=['Correo Institucional'])
  
  """ Convertimos la tabla a un formato HTML """
  tabla_html = tabla_filtro.to_html(index = False, border = 0) #le quitamos el índice

  """ editamos el HTML con Beautiful Soup 
      cargamos el texto HTML en Beautiful Soup para poder editarlo"""
  soup = BeautifulSoup(tabla_html, 'html.parser')

  tabla = soup.find('table')
  if tabla:
    tabla['style'] = config.ESTILO_TABLA

  for th in soup.find_all('th'):
    th['style'] = config.ESTILO_CABECERA 
  
  for td in soup.find_all('td'):
    td['style'] = config.ESTILO_CELDA
  
  tabla_html_bs = str(soup) 


  """ Creamos el cuerpo completo del correo en HTML """
  image_cid = 'logo_idiomas_cid'
  cuerpo_correo = f"""
  <html>
  <body style="font-family: sans-serif;">
      <p>Estimado(a) {nombre_instructor}</p>
      <p>Te compartimos sus accesos para el mes de {nombre_mes}:</p> 
      <div style="overflow-x:auto;">  
        {tabla_html_bs} 
      </div>
      <p>Saludos cordiales</p>
      <br>
      {config.FIRMA_HTML}
      <img src="cid:{image_cid}" width="200">
  </body>
  </html>
  """
  

  ### -------- ESTACIÓN 4: ENVIAR CORREO ------------
  try: 
    msg = EmailMessage()
    msg['Subject'] = config.ASUNTO_DEL_CORREO.format(mes=nombre_mes)
    msg['From'] = mi_correo
    msg['To'] = "diego.ab130@gmail.com" # cambiar por = correo
    #msg['Cc'] = config.EMAIL_CC
    msg.add_alternative(cuerpo_correo, subtype='html') #añadimos el cuerpo HTML

    with open('logo_idiomas.png', 'rb') as img_file:
      msg.add_attachment(img_file.read(), maintype='image', subtype='png', cid=f'<{image_cid}>')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(mi_correo, mi_contraseña)
      smtp.send_message(msg)
      print(f"Correo enviado exitosamente a {correo}")
  except Exception as e:
    print(f"Error al enviar correo a {correo}: {e}")
 