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
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=40,
        border=4,
    )
    nombre_archivo = f"{nombre}.png"
    try:
        qr.add_data(datos)
        qr.make(fit=True)
        img = qr.make_image(fill_color=(255,236,92), back_color=(120,91,255))
        img.save(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' creado con éxito")
    except Exception as e:
        print(f"Error al guardar el archivo QR: {str(e)}")

if __name__ == "__main__":
    main()
