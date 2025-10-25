from tkinter import messagebox, simpledialog
from database import baseDatos

# ------------------- Inicio de sesión -------------------
class inicioSesion:

    def login(self, usuario, contraseña):
        conexion = baseDatos.crearTablas.establecerConexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password=?", (usuario, contraseña))
            resultado = cursor.fetchone()
            if resultado:
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
        conexion = baseDatos.crearTablas.establecerConexion()
        cursor = conexion.cursor()
        nombre = simpledialog.askstring("Usuario", "Ingrese nombre")
        if nombre is None:
            messagebox.showinfo("Cancelado", "Operación cancelada")
            return
        contraseña = simpledialog.askstring("Usuario", "Ingrese contraseña")
        if contraseña is None:
            messagebox.showinfo("Cancelado", "Operación cancelada")
            return
        try:
            cursor.execute("INSERT INTO usuarios(nombre, password) VALUES(?,?)", (nombre, contraseña))
            conexion.commit()
            messagebox.showinfo("Estado", "Usuario registrado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear usuario: {e}")
        finally:
            conexion.close()





        
       

        
           


        