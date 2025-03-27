from starlette import status


class PokeException(Exception):
    # Excepción personalizada para manejar errores en la aplicación
    def __init__(self, message: str, process: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.message = message
        self.process = process
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        # Representación en cadena de la excepción
        return f"{self.message} (Process: {self.process}, Status Code: {self.status_code})"

    def to_dict(self):
        # Convierte la excepción en un diccionario para facilitar la serialización
        return {
            "message": self.message,
            "process": self.process,
            "status_code": self.status_code
        }
