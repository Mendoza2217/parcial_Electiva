from fastapi import FastAPI, HTTPException
import mysql.connector
from core.conexion import connection
from models.accesorios import Accesorios
from models.usuarios import Usuario

app = FastAPI()

# Obtener todos los accesorios
@app.get("/accesorios")
async def get_accesorios():
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM accesorios"

    try:
        cursor.execute(query)
        accesorios = cursor.fetchall()
        return accesorios
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al obtener los accesorios")
    finally:
        cursor.close()

# Obtener un accesorio por su ID
@app.get("/accesorios/{id_accesorio}")
async def get_accesorio(id_accesorio: int):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM accesorios WHERE id_accesorio = %s"

    try:
        cursor.execute(query, (id_accesorio,))
        accesorio = cursor.fetchone()
        if accesorio:
            return accesorio
        else:
            raise HTTPException(status_code=404, detail="Accesorio no encontrado")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al obtener el accesorio")
    finally:
        cursor.close()

# Crear un nuevo accesorio
@app.post("/accesorios")
async def create_accesorio(accesorio: Accesorios):
    cursor = connection.cursor(dictionary=True)

    query = "INSERT INTO accesorios (nombre, cantidad, descripcion, precio) VALUES (%s, %s, %s, %s)"

    try:
        cursor.execute(query, (accesorio.nombre, accesorio.cantidad, accesorio.descripcion, accesorio.precio))
        connection.commit()
        return {"message": "Accesorio creado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al crear el accesorio")
    finally:
        cursor.close()

# Actualizar un accesorio existente
@app.put("/accesorios/{id_accesorio}")
async def update_accesorio(id_accesorio: int, accesorio: Accesorios):
    cursor = connection.cursor(dictionary=True)

    query = "UPDATE accesorios SET nombre = %s, cantidad = %s, descripcion = %s, precio = %s WHERE id_accesorio = %s"

    try:
        cursor.execute(query, (accesorio.nombre, accesorio.cantidad, accesorio.descripcion, accesorio.precio, id_accesorio))
        connection.commit()
        return {"message": "Accesorio actualizado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al actualizar el accesorio")
    finally:
        cursor.close()

# Eliminar un accesorio existente
@app.delete("/accesorios/{id_accesorio}")
async def delete_accesorio(id_accesorio: int):
    cursor = connection.cursor(dictionary=True)

    query = "DELETE FROM accesorios WHERE id_accesorio = %s"

    try:
        cursor.execute(query, (id_accesorio,))
        connection.commit()
        return {"message": "Accesorio eliminado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al eliminar el accesorio")
    finally:
        cursor.close()

# Crear un nuevo usuario
@app.post("/usuarios")
async def create_usuario(usuario: Usuario):
    cursor = connection.cursor(dictionary=True)

    query = "INSERT INTO usuarios (nombre, sexo, correo, telefono) VALUES (%s, %s, %s, %s)"

    try:
        cursor.execute(query, (usuario.nombre, usuario.sexo, usuario.correo, usuario.telefono))
        connection.commit()
        return {"message": "Usuario creado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al crear el usuario")
    finally:
        cursor.close()

# buscar un usuario por su ID
@app.get("/usuarios/{id_usuario}")
async def get_usuario(id_usuario: int):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM usuarios WHERE id_usuario = %s"

    try:
        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone()
        if usuario:
            return usuario
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al obtener el usuario")
    finally:
        cursor.close()

# Eliminar un usuario existente
@app.delete("/usuarios/{id_usuario}")
async def delete_usuario(id_usuario: int):
    cursor = connection.cursor(dictionary=True)

    query = "DELETE FROM usuarios WHERE id_usuario = %s"

    try:
        cursor.execute(query, (id_usuario,))
        connection.commit()
        return {"message": "Usuario eliminado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al eliminar el usuario")
    finally:
        cursor.close()

# Actualizar un usuario existente
@app.put("/usuarios/{id_usuario}")
async def update_usuario(id_usuario: int, usuario: Usuario):
    cursor = connection.cursor(dictionary=True)

    query = "UPDATE usuarios SET nombre = %s, sexo = %s, correo = %s, telefono = %s WHERE id_usuario = %s"

    try:
        cursor.execute(query, (usuario.nombre, usuario.sexo, usuario.correo, usuario.telefono, id_usuario))
        connection.commit()
        return {"message": "Usuario actualizado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")
    finally:
        cursor.close()

