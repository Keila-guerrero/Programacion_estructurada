from conexionBD import *
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,gmail,contraseña):
    try:
       contraseña=hash_password(contraseña)
       sql="insert into usuarios (nombre,gmail,contraseña) values (%s,%s,%s)"
       val=(nombre,gmail,contraseña)
       cursor.execute(sql,val)
       conexion.commit()
       return True
    except Exception as e:
        print(f"Error al registrar: {e}")
        return False    
    
def iniciar_sesion(email,contrasena):
    try:
       contrasena=hash_password(contrasena)
       sql="select * from usuarios where gmail=%s and contraseña=%s"
       val=(email,contrasena)
       cursor.execute(sql,val)
       registro=cursor.fetchone()
       if registro:
           return registro
       else:
           return None
    except:
        return None   