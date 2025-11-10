import unittest
from app.models.funciones_inventario import funcionesProductos

class TestProductos(unittest.TestCase):

    def test_insertar_producto(self):
        nuevo_id = funcionesProductos.agregarProducto("soda",976, 10, True)
        self.assertIsInstance(nuevo_id, int)
        
        productos = funcionesProductos.mostrarProductos()
        self.assertTrue(any(p[0] == nuevo_id and p[1] == "TestProducto" for p in productos))

    def test_modificar_producto(self):
        nuevo_id = funcionesProductos.agregarProducto("ModificarProducto", 50.0, 5, True)
        funcionesProductos.modificarProducto("Modificado", 55.0, 8, False, nuevo_id)

        productos = funcionesProductos.mostrarProductos()
        self.assertTrue(any(p[0] == nuevo_id and p[1] == "Modificado" for p in productos))

    def test_eliminar_producto(self):
        nuevo_id = funcionesProductos.agregarProducto("EliminarProducto", 20.0, 2, True)
        funcionesProductos.eliminarProducto(nuevo_id, True)

        productos = funcionesProductos.mostrarProductos()
        self.assertFalse(any(p[0] == nuevo_id for p in productos))

    def test_mostrar_productos(self):
        productos = funcionesProductos.mostrarProductos()
        self.assertIsInstance(productos, list)
        for p in productos:
            self.assertIsInstance(p, tuple)
            self.assertGreaterEqual(len(p), 4)  # ID, nombre, precio, cantidad

if __name__ == "__main__":
    unittest.main()
