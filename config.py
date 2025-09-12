NOMBRE_ARCHIVO = 'data/tabla_accesos.xlsx'
ASUNTO_DEL_CORREO = "Accesos a cuentas Zoom - Cursos de {mes}"
NOMBRE_REMITENTE = "Centro de Idiomas UPCH"
EMAIL_CC = ""

#--- estilos para la tabla HTML ---
COLOR_FONDO_HEAD = '#b01333'
COLOR_TEXTO_HEAD = 'white'
COLOR_BORDE_FILA = '#ddd'

ESTILO_TABLA = 'border-collapse: collapse; width: auto; font-family: sans-serif;'
ESTILO_CABECERA = f'background-color: {COLOR_FONDO_HEAD}; color: {COLOR_TEXTO_HEAD}; text-align: center; padding: 10px; white-space: nowrap; border: 1px solid #333;'
ESTILO_CELDA = f'padding: 8px; text-align: left; border: 1px solid {COLOR_BORDE_FILA}; white-space: nowrap;'

FIRMA_HTML = """
<p style="margin:0; font-weight: bold; color: #333;">Diego Alvarado</p>
<p style="margin:0; color: #b01333;">Asistente académico</p>
<p style="margin:0; color: #333;">Centro de Idiomas</p>
<p style="margin:0; color: #333;">T. 941374233</p>
<p style="margin:0;"><a href="mailto:diego.alvarado@upch.pe">diego.alvarado@upch.pe</a></p>
"""