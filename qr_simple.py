import qrcode

def main():
    data = input("Dato a guardar en el qr: ")
    filename = input("Nombre del archivo qr: ")
    crear_qr(data, filename)


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
