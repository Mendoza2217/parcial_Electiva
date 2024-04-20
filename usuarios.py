from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: int
    nombre: str
    sexo: str
    correo: str
    telefono: int