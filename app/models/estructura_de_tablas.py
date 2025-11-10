from config.conexion import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

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

class Ventas(Base):

        __tablename__ ='ventas'

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        fecha_venta = Column(DateTime, nullable=False)
        total= Column(Float, nullable=False)

class DetallesVenta(Base):

        __tablename__ ='detalleVentas'

        id = Column(Integer, primary_key=True, autoincrement=True, index=True)
        venta_id = Column(Integer, ForeignKey('ventas.id'))
        producto_id = Column(Integer, ForeignKey('productos.id'))
        cantidad = Column(Integer, nullable=False)
        precio_unitario = Column(Float, nullable =False)
        relacion_productos = relationship("Productos")
        relacion_ventas = relationship("Ventas")