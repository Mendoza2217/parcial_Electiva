from pydantic import BaseModel

class Accesorios(BaseModel):
    id_accesorio: int
    nombre: str
    cantidad: int
    descripcion: str = None
    precio: int