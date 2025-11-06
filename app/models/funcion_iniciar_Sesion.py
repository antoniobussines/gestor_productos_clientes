from tkinter import messagebox, simpledialog
from config.conexion import sesion_local
from app.models.estructura_de_tablas import Personal
from sqlalchemy import *
# ------------------- Inicio de sesión -------------------
class inicioSesion:

    def login(usuario, contraseña):
        conexion = sesion_local()
        
        try:
            registro = conexion.query(Personal).filter(and_(Personal.nombre == usuario, Personal.password == contraseña)).first()
            if registro:
                messagebox.showinfo("Estado", "Inicio de sesión correcto")
                return True
            else:
                messagebox.showinfo("Estado", "Usuario o contraseña incorrectos")
                return False
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def crearUsuario():
        
        conexion = sesion_local()

        nombre_tratado = simpledialog.askstring("Usuario", "Ingrese nombre")

        if nombre_tratado is None:
            messagebox.showinfo("Cancelado", "Operación cancelada")
            return
        
        contraseña = simpledialog.askstring("Usuario", "Ingrese contraseña")
        if contraseña is None:
            messagebox.showinfo("Cancelado", "Operación cancelada")
            return

        nuevo = Personal(
            nombre = nombre_tratado,
            password = contraseña
        )

        try:
            conexion.add(nuevo)
            conexion.commit()
            messagebox.showinfo("Estado", "Usuario registrado correctamente")

            return [True, nombre_tratado, contraseña]
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear usuario: {e}")
        finally:
            conexion.close()





        
       

        
           


        