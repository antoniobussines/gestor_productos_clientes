# Sistema de Gestión de Productos y Clientes

Este proyecto permite gestionar productos y clientes mediante operaciones CRUD (crear, leer, actualizar, eliminar) y exportar los datos de las tablas a archivos Excel. Está desarrollado en Python y utiliza SQLite como base de datos.

---

##  Objetivo General

Desarrollar un sistema en Python que permita gestionar productos y clientes mediante operaciones CRUD, y exportar los datos almacenados en la base de datos a archivos Excel de forma eficiente y estructurada.

---

##  Objetivos Específicos

- Implementar una base de datos relacional en SQLite.
- Desarrollar funciones para el manejo de productos y clientes.
- Permitir la exportación de datos a archivos Excel.
- Realizar pruebas para validar el funcionamiento de las funciones.

---

##  Alcance

El sistema está diseñado para pequeñas empresas y proyectos relacionados que requieran gestionar productos y clientes de forma sencilla. Está sujeto a cambios menores en su estructura o funcionalidades, siempre que se mantenga el objetivo principal del proyecto.

---

##  Modelo Entidad-Relación (MER)

<img width="631" height="398" alt="image" src="https://github.com/user-attachments/assets/358b64c0-08bf-4fe0-b256-cf03370c5f2d" />

---

##  Entidades

- **Usuarios**: ID, Nombre, Password  
- **Productos**: ID, Nombre, Precio, Cantidad  
- **Clientes**: ID, Nombre, Teléfono, Dirección

---

##  Relaciones

La relación entre clientes y productos es de 1 a muchos (1:N), ya que un cliente puede tener muchos productos registrados, pero un producto pertenece a un solo cliente.  
La entidad **Usuarios** no tiene relación directa con las demás tablas.

---

##  Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal.
- **SQLite3**: Motor de base de datos relacional.
- **unittest**: Framework para pruebas automatizadas.
- **openpyxl**: Librería para exportar datos a archivos Excel.

---

##  Cómo Ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/tu_repositorio.git

# Entrar a la carpeta del proyecto
cd tu_repositorio

# Ejecutar el programa principal
python main.py
