import unittest
from app.models.funciones_inventario import funcionesClientes

class TestClientes(unittest.TestCase):

    def test_insertar_cliente(self):
        funcionesClientes.agregarCliente("TestCliente", 999, 888)
        clientes = funcionesClientes.mostrarClientes()
        self.assertTrue(any(c[1] == "TestCliente" for c in clientes))

    def test_modificar_cliente(self):
        funcionesClientes.agregarCliente("ClienteModificar", 111, 222)
        clientes = funcionesClientes.mostrarClientes()
        id_modificar = clientes[-1][0]  # Último insertado

        funcionesClientes.modificarClientes("Modificado", 123, 456, False, id_modificar)
        clientes_actualizados = funcionesClientes.mostrarClientes()
        self.assertTrue(any(c[0] == id_modificar and c[1] == "Modificado" for c in clientes_actualizados))

    def test_eliminar_cliente(self):
        funcionesClientes.agregarCliente("ClienteEliminar", 333, 444)
        clientes = funcionesClientes.mostrarClientes()
        id_eliminar = clientes[-1][0]

        funcionesClientes.eliminarClientes(id_eliminar, True)
        clientes_actualizados = funcionesClientes.mostrarClientes()
        self.assertFalse(any(c[0] == id_eliminar for c in clientes_actualizados))

    def test_mostrar_clientes(self):
        clientes = funcionesClientes.mostrarClientes()
        self.assertIsInstance(clientes, list)
        for c in clientes:
            self.assertIsInstance(c, tuple)
            self.assertGreaterEqual(len(c), 4)  # ID, nombre, teléfono, dirección

if __name__ == "__main__":
    unittest.main()
