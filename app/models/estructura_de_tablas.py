from config.conexion import Base
from sqlalchemy import *

class Clientes(Base):


    __tablename__ ='clientes'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    direccion = Column(String, nullable=False) 

class Productos(Base):

    __tablename__ ='productos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False )
    cantidad = Column(Integer, nullable=True)

class Personal(Base):
    
    __tablename__ ='personal'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    password = Column(String, nullable=False)