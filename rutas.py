from pathlib import Path

# Con cwd() identificamos la ruta hacia la carpeta donde nos encontramos.
current_path = Path.cwd()

# En una variable, almacenamos el nombre de la carpeta donde se localizan nuestros archivos.
archivos = 'Archivos'

# Concatenamos la ruta principal + la ruta de la carpeta con nuestros archivos.
carpeta_archivos = current_path / archivos

# En las variablea 'destination', indicamos nuevas las rutas hácia donde se moveran nuestros archivos. 
destination_txts = current_path / 'txts/'
destination_jpgs = current_path / 'jpgs/'
destination_jpegs = current_path / 'jpegs/'
destination_pngs = current_path / 'pngs/'
destination_pdfs = current_path / 'pdfs/'
destination_mp3s = current_path / 'mp3s/'
destination_mp4s = current_path / 'mp4s/'