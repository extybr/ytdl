from base64 import decodebytes
from pathlib import Path
from tempfile import gettempdir
from img import svg


def decode_b64() -> str:
    """
    Переменные окружения.
    Декодирование файла из base64.
    Сохранение иконки
    """
    pic = 'youtube.svg'
    try:
        path_temp = Path(gettempdir()) / pic
        if Path.exists(path_temp):
            print(str(path_temp))
            return str(path_temp)
        else:
            dec = decodebytes(svg.encode())
            with open(path_temp, 'wb') as file:
                file.write(dec)
            return str(path_temp)
    except Exception:
        return 'favicon.ico'
