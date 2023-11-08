import qrcode
import os
from sys import argv, exit

# Obtiene el nombre del archivo que contiene el script.
NOMBRE_SCRIPT = os.path.basename(__file__)

def main():
    if len(argv) != 3:
        print(f"Uso: python {NOMBRE_SCRIPT} <'Datos para el archivo'> <'nombre del archivo de salida'>")
        exit(1)
    else:
        crear_qr(argv[1], argv[2])

def crear_qr(datos: str, nombre: str):
    """
    Crea un código QR a partir de los datos proporcionados y guarda la imagen en formato PNG.
    
     Args:
        datos (int) : El contenido que se codificará en el código QR.
        nombre (int) : El nombre del archivo de imagen QR a crear (sin la extensión .png).

    Ejemplo:
    >>> crear_qr("https://www.kitomaker.com", "mi_codigo_qr")
    Archivo 'mi_codigo_qr.png' creado con éxito
    """
    extension = ".png"
    nombre_archivo = nombre + extension
    try:
        img = qrcode.make(datos)
        img.save(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' creado con éxito")
    except Exception as e:
        print(f"Error al guardar el archivo QR: {str(e)}")


if __name__ == "__main__":
    main()