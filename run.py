from config.conexion import Base, engine_creator
from app.models.funcion_iniciar_Sesion import inicioSesion
from app.controlers.interfaz import App


class funciones_generales:

    def crear_tablas():

        engine = engine_creator
        Base.metadata.create_all(bind=engine)
    
    def crear_persona():

       datos = inicioSesion.crearUsuario()
       inicioSesion.login(datos[1], datos[2])

    def ejecutar_programa():

        instancia = App()

funciones_generales.ejecutar_programa()
    





