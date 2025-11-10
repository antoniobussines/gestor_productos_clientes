import tkinter as tk
from tkinter import ttk, messagebox
from app.models import funciones_inventario
from app.models.funcion_iniciar_Sesion import inicioSesion
from tkinter.ttk import Combobox 

# ------------------- Aplicación -------------------
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x450")
        self.root.title("Inicio de Sesión / Inventario")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)

        # Inicializar login
        self.crear_login()
        self.root.mainloop()

    # ------------------- Login -------------------
    def crear_login(self):
        self.frame_login = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center", width=350, height=180)

        tk.Label(self.frame_login, text="Acceso al Sistema", font=("Arial", 16, "bold"),
                 bg="white", fg="#333").grid(row=0, column=0, columnspan=2, pady=(10,15))

        tk.Label(self.frame_login, text="Usuario:", font=("Arial", 11), bg="white").grid(row=1, column=0, sticky="e", padx=(10,5), pady=5)
        self.input_nombre = tk.Entry(self.frame_login, font=("Arial", 11), width=20, bd=1, relief="solid")
        self.input_nombre.grid(row=1, column=1, sticky="w", padx=(5,10), pady=5)

        tk.Label(self.frame_login, text="Contraseña:", font=("Arial", 11), bg="white").grid(row=2, column=0, sticky="e", padx=(10,5), pady=5)
        self.input_password = tk.Entry(self.frame_login, font=("Arial", 11), width=20, bd=1, relief="solid", show="*")
        self.input_password.grid(row=2, column=1, sticky="w", padx=(5,10), pady=5)

        boton_inicio = tk.Button(self.frame_login, text="Iniciar Sesión", font=("Arial", 11, "bold"),
                                 bg="#f4f4f4", relief="raised", cursor="hand2", command=self.iniciar_sesion)
        boton_inicio.grid(row=3, column=0, columnspan=2, pady=(15,5), ipadx=10, ipady=3)
        boton_inicio.bind("<Enter>", lambda e: boton_inicio.config(bg="#3a7ff6", fg="white"))
        boton_inicio.bind("<Leave>", lambda e: boton_inicio.config(bg="#f4f4f4", fg="black"))

    def iniciar_sesion(self):
        usuario = self.input_nombre.get().strip()
        contraseña = self.input_password.get().strip()
        if not usuario or not contraseña:
            messagebox.showwarning("Advertencia", "Ingrese usuario y contraseña")
            return
        if inicioSesion.login(usuario, contraseña):
         self.frame_login.place_forget()
         self.crear_inventario()

    # ------------------- Inventario -------------------
    def crear_inventario(self):
        self.root.title("Inventario")
        self.root.resizable(True, True)
        FRAME_BG = "#f6f7f9"
        FORM_BG = "#fff6e6"
        BTN_BG = "#007ACC"
        BTN_FG = "white"
        self.root.configure(bg=FRAME_BG)

        # Estilos
        style = ttk.Style(self.root)
        try:
            style.theme_use('clam')
        except:
            pass
        style.configure('TButton', font=("Segoe UI", 10))
        style.configure('Treeview.Heading', font=("Segoe UI", 10, "bold"))
        style.configure('Treeview', rowheight=24, font=("Segoe UI", 10))

        # Header
        header = tk.Frame(self.root, bg="#113f67")
        header.pack(fill='x')
        tk.Label(header, text="Sistema de Inventario", bg="#113f67", fg="white",
                 font=("Segoe UI", 18, "bold"), pady=10).pack()

        # Menu
        menu = tk.Frame(self.root, bg=FRAME_BG)
        menu.pack(fill='x', pady=(8,6))

        # Frames principales
        main = tk.Frame(self.root, bg=FRAME_BG)
        main.pack(fill='both', expand=True, padx=10, pady=6)
        left = tk.Frame(main, bg=FORM_BG, width=300)
        left.pack(side='left', fill='y', padx=(0,8))
        left.pack_propagate(False)
        right = tk.Frame(main, bg=FRAME_BG)
        right.pack(side='right', fill='both', expand=True)

        # ------------------- Formulario Productos -------------------
        self.frm_prod = tk.Frame(left, bg=FORM_BG, padx=10, pady=10)
        tk.Label(self.frm_prod, text="Ingreso de Producto", bg=FORM_BG, font=("Segoe UI",12,"bold")).pack(anchor='w', pady=(0,8))
        self.entry_nombre = tk.Entry(self.frm_prod); self.entry_nombre.pack(fill='x', pady=4)
        self.entry_precio = tk.Entry(self.frm_prod); self.entry_precio.pack(fill='x', pady=4)
        self.entry_cantidad = tk.Entry(self.frm_prod); self.entry_cantidad.pack(fill='x', pady=4)

        self.entry_nombre.insert(0, "escribe el nombre")
        self.entry_precio.insert(0, "escribe el precio")
        self.entry_cantidad.insert(0, "escriba la cantidad")

        # Placeholders
        def set_placeholder(entry, text):
            def on_focus_in(event):
                if entry.get() == text:
                    entry.delete(0, tk.END)
                    entry.config(fg="black")
            def on_focus_out(event):
                if entry.get() == "":
                    entry.insert(0, text)
                    entry.config(fg="gray")
            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)
            entry.config(fg="gray")
        set_placeholder(self.entry_nombre, "escribe el nombre")
        set_placeholder(self.entry_precio, "escribe el precio")
        set_placeholder(self.entry_cantidad, "escriba la cantidad")

        # Botones Productos
        btn_frame = tk.Frame(self.frm_prod, bg=FORM_BG)
        btn_frame.pack(fill='x', pady=(8,0))
        bton_agregar = tk.Button(btn_frame, text="Agregar", bg=BTN_BG, fg=BTN_FG, relief='flat',
                         command=lambda: botonAgregar())
        

        bton_agregar.pack(side='left', expand=True, fill='x', padx=(0,2))
        bton_limpiar = tk.Button(btn_frame, text="Limpiar", relief='ridge',
                         command=lambda: limpiarCampos('producto'))
        bton_limpiar.pack(side='left', expand=True, fill='x', padx=(2,2))

        btn_frame_mod = tk.Frame(self.frm_prod, bg=FORM_BG)
        btn_frame_mod.pack(fill='x', pady=(4,0))
        self.btn_modificar = tk.Button(btn_frame_mod, text="Modificar", bg=BTN_BG, fg=BTN_FG,
                               command=lambda: botonModificar())
        self.btn_modificar.pack(side='left', expand=True, fill='x', padx=(0,2))
        self.btn_eliminar = tk.Button(btn_frame_mod, text="Eliminar", relief='ridge',
                                      command= lambda: eliminar_productos())
        self.btn_eliminar.pack(side='left', expand=True, fill='x', padx=(2,0))

        def eliminar_productos ():

            funciones_inventario.funcionesProductos.eliminarProducto(self.tree_prod)
            funciones_inventario.funcionesProductos.mostrarProductos(self.tree_prod)
           

        frm_button_export_p = tk.Frame(self.frm_prod); frm_button_export_p.pack(fill="x",pady=(4,0))

        button_export_p = tk.Button(frm_button_export_p, text="Exportar", fg=BTN_FG, bg=BTN_BG,
                                    command=lambda: funciones_inventario.ExportadorExcel.exportar(self.tree_prod, self.tree_cli)); button_export_p.pack(fill="x", expand=True)
        
        # ------------------- Formulario Clientes -------------------
        self.frm_cli = tk.Frame(left, bg=FORM_BG, padx=10, pady=10)
        tk.Label(self.frm_cli, text="Ingreso de Cliente", bg=FORM_BG, font=("Segoe UI",12,"bold")).pack(anchor='w', pady=(0,8))
        self.entry_cli_nombre = tk.Entry(self.frm_cli); self.entry_cli_nombre.pack(fill='x', pady=4)
        self.entry_cli_tel = tk.Entry(self.frm_cli); self.entry_cli_tel.pack(fill='x', pady=4)
        self.entry_cli_dir = tk.Entry(self.frm_cli); self.entry_cli_dir.pack(fill='x', pady=4)

        self.entry_cli_nombre.insert(0, "escribe el nombre")
        self.entry_cli_tel.insert(0, "escribe el telefono")
        self.entry_cli_dir.insert(0,"escribe la direccion")

        set_placeholder(self.entry_cli_nombre, "escribe el nombre")
        set_placeholder(self.entry_cli_tel, "escribe el telefono")
        set_placeholder(self.entry_cli_dir, "escribe la direccion")

        # Botones Clientes
        btn_frame_cli = tk.Frame(self.frm_cli, bg=FORM_BG)
        btn_frame_cli.pack(fill='x', pady=(8,0))
        bton_cli_agregar = tk.Button(btn_frame_cli, text="Agregar ", bg=BTN_BG, fg=BTN_FG, relief='flat',
                             command=lambda: [funciones_inventario.funcionesClientes.agregarCliente(self.entry_cli_nombre.get(), self.entry_cli_tel.get(), self.entry_cli_dir.get()),
                                              funciones_inventario.funcionesClientes.mostrarClientes(self.tree_cli),  
                                              funciones_inventario.ExportadorExcel.exportar(self.tree_prod, self.tree_cli)])
        bton_cli_agregar.pack(side='left', expand=True, fill='x', padx=(0,2))
        bton_cli_limpiar = tk.Button(btn_frame_cli, text="Limpiar", relief='ridge',
                             command=lambda: limpiarCampos('cliente'))
        bton_cli_limpiar.pack(side='left', expand=True, fill='x', padx=(2,2))

        frm_cli_mod = tk.Frame(self.frm_cli, bg=FORM_BG)
        frm_cli_mod.pack(fill="x", pady=(4,0))
        bton_cli_mod = tk.Button(frm_cli_mod, text="Modificar", bg=BTN_BG, fg=BTN_FG, 
                         command=lambda: modificarCliente())
        bton_cli_mod.pack(side='left', expand=True, fill='x', padx=(0,2))
        bton_cli_elim = tk.Button(frm_cli_mod, text="Eliminar", relief='ridge',
                                  command= lambda: eliminarClientes())
        bton_cli_elim.pack(side='left', expand=True, fill='x', padx=(2,0)) 

        def eliminarClientes():

            funciones_inventario.funcionesClientes.eliminarClientes(self.tree_cli)
            funciones_inventario.funcionesClientes.mostrarClientes(self.tree_cli)
        


        frm_button_export_c = tk.Frame(self.frm_cli); frm_button_export_c.pack(fill="x",pady=(4,0))

        button_export_c = tk.Button(frm_button_export_c, text="Exportar", fg=BTN_FG, bg=BTN_BG,
                                    command=lambda: funciones_inventario.ExportadorExcel.exportar(self.tree_prod, self.tree_cli)); button_export_c.pack(fill="x", expand=True)
        
        # ---------------------- Ventas ----------------------
        self.frm_ventas = tk.Frame(left, bd=2, padx=10, pady=10, bg=FORM_BG)
        self.frm_ventas.pack(fill="x", pady=10)

        # Título
        tk.Label(self.frm_ventas, text="Registro de Ventas", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 10))

        # Combobox de productos
        self.combo_productos = ttk.Combobox(self.frm_ventas, values=[], state="readonly", font=("Arial", 11))
        self.combo_productos.pack(fill="x", pady=5)
        self.combo_productos.set("Selecciona un producto")

        # Entrada de cantidad
        self.entry_ventas_cantidad = tk.Entry(self.frm_ventas, font=("Arial", 11))
        self.entry_ventas_cantidad.pack(fill="x", pady=5)
        self.entry_ventas_cantidad.insert(0, "escribe la cantidad")

        # Botón de registrar venta
        self.btn_registrar_venta = tk.Button(
            self.frm_ventas,
            text="Registrar Venta",
            fg=BTN_FG,
            bg=BTN_BG,
            font=("Arial", 11, "bold"),
            command=lambda: insertar_venta()
        )
        self.btn_registrar_venta.pack(fill="x", padx=20, pady=10)

        def  insertar_venta():
            
            funciones_inventario.ventas.insertar_venta(self.combo_productos.get(), self.entry_ventas_cantidad.get())
            funciones_inventario.ventas.mostrar_ventas(self.tree_ventas)
       
        def optionCombobox(event):

            listOptionCombobox = funciones_inventario.funcionesProductos.mostrarProductos()
            self.combo_productos.config(values=listOptionCombobox)
            
    
        self.combo_productos.bind("<Button-1>", optionCombobox)

        def placeholderVentaIn(event):

            if self.entry_ventas_cantidad.get() =="escribe la cantidad":

                self.entry_ventas_cantidad.delete(0,tk.END)

        def placeholderVentaOut(event):

            if self.entry_ventas_cantidad.get()  == "":

                self.entry_ventas_cantidad.insert(0, "escribe la cantidad")

        
        self.entry_ventas_cantidad.bind("<FocusIn>", placeholderVentaIn)
        self.entry_ventas_cantidad.bind("<FocusOut>", placeholderVentaOut)



        # ------------------- Treeviews -------------------
        self.tree_prod = ttk.Treeview(right, columns=("id", "nombre", "precio", "cantidad", "total"), show='headings')
        for col, txt in zip(("id", "nombre", "precio", "cantidad","total"), ("ID", "Nombre", "Precio", "Cantidad","Total")):
            self.tree_prod.heading(col, text=txt)
            self.tree_prod.column(col, width=100, anchor='center')

        self.tree_cli = ttk.Treeview(right, columns=("id", "nombre","telefono","direccion"), show='headings')
        for col, txt in zip(("id","nombre","telefono","direccion"), ("ID","Nombre","Teléfono","Dirección")):
            self.tree_cli.heading(col, text=txt)
            self.tree_cli.column(col, width=100, anchor='center')
        
        self.tree_ventas = ttk.Treeview(right, columns=("id", "fecha_venta" ,"producto", "cantidad", "precio_unitario", "total"), show="headings")
        for col, txt in zip(("id", "fecha_venta", "producto", "cantidad", "precio_unitario", "total"),("ID", "Fecha venta", "Producto", "Cantidad", "Precio unitario", "Total")):
            self.tree_ventas.heading(col, text=txt)
            self.tree_ventas.column(col, width= 100, anchor="center")

        # ------------------- Funciones auxiliares -------------------
        def botonAgregar():

            if self.entry_nombre.get() == "" or self.entry_nombre.get() == "escribe el nombre":

                messagebox.showwarning("estado", "no se permiten valore snulos")
                      
            else:

                 funciones_inventario.funcionesProductos.agregarProducto(self.entry_nombre.get(), self.entry_precio.get(), self.entry_cantidad.get())
                 funciones_inventario.funcionesProductos.mostrarProductos(self.tree_prod)                
                 limpiarCampos('producto')
           

        def botonModificar():
            cantidad = self.entry_cantidad.get()
            precio = self.entry_precio.get()
            funciones_inventario.funcionesProductos.modificarProducto(self.entry_nombre.get(),precio , cantidad , True,self.tree_prod)
            funciones_inventario.funcionesProductos.mostrarProductos(self.tree_prod)

        def modificarCliente():

            nombre = self.entry_cli_nombre.get()
            telefono = self.entry_cli_tel.get()
            direccion = self.entry_cli_dir.get()
 

            if nombre == "" or nombre == "escriba el nombre":

                    messagebox.showwarning("estado", "escriba el nombre")
                    return

            if  telefono == "" or  telefono == "escribe el telefono":

                    messagebox.showwarning("estado", "escribe el telefono")
                    return
                
            if direccion == "" or direccion == "escribe la direccion":

                    messagebox.showwarning("estado", "escribe el telefono")
                    return
                
            funciones_inventario.funcionesClientes.modificarClientes(nombre, telefono, direccion, True, self.tree_cli)
            funciones_inventario.funcionesClientes.mostrarClientes(self.tree_cli)


        def limpiarCampos(tipo):
            if tipo=='producto':
                self.entry_nombre.delete(0, tk.END)
                self.entry_precio.delete(0, tk.END)
                self.entry_cantidad.delete(0, tk.END)
                self.entry_nombre.insert(0,"escribe el nombre")
                self.entry_precio.insert(0,"escribe el precio")
                self.entry_cantidad.insert(0,"escriba la cantidad")
            elif tipo=='cliente':
                self.entry_cli_nombre.delete(0, tk.END)
                self.entry_cli_tel.delete(0, tk.END)
                self.entry_cli_dir.delete(0, tk.END)
                self.entry_cli_nombre.insert(0,"escribe el nombre")
                self.entry_cli_tel.insert(0,"escribe el telefono")
                self.entry_cli_dir.insert(0,"escribe la direccion")

        # ------------------- Función mostrar -------------------
        def mostrar_treeview(tipo):
            # Ocultar todo
            self.tree_prod.pack_forget()
            self.tree_cli.pack_forget()
            self.frm_prod.pack_forget()
            self.frm_cli.pack_forget()
            self.tree_ventas.pack_forget()
            self.frm_ventas.pack_forget()

            if tipo=='productos':
                self.frm_prod.pack(fill='both', expand=True)
                self.tree_prod.pack(fill='both', expand=True)
                dale = funciones_inventario.funcionesProductos.mostrarProductos(self.tree_prod)
                return dale
            elif tipo=='clientes':
                self.frm_cli.pack(fill='both', expand=True)
                self.tree_cli.pack(fill='both', expand=True)
                funciones_inventario.funcionesClientes.mostrarClientes(self.tree_cli)
            elif tipo=='ventas':

                self.frm_ventas.pack(fill="both", expand=True)
                self.tree_ventas.pack(fill="both", expand=True)
                funciones_inventario.ventas.mostrar_ventas(self.tree_ventas)

            elif tipo=='reportes':
                self.tree_prod.pack(fill='both', expand=True)
                self.tree_cli.pack(fill='both', expand=True)
                funciones_inventario.funcionesProductos.mostrarProductos(self.tree_prod)
                funciones_inventario.funcionesClientes.mostrarClientes(self.tree_cli)

        # ------------------- Botones menú -------------------
        tk.Button(menu, text="Productos", bg=BTN_BG, fg=BTN_FG, relief='flat',
                  command=lambda: mostrar_treeview('productos')).pack(side='left', expand=True, fill='x', padx=4)
        tk.Button(menu, text="Clientes", bg=BTN_BG, fg=BTN_FG, relief='flat',
                  command=lambda: mostrar_treeview('clientes')).pack(side='left', expand=True, fill='x', padx=4)
        tk.Button(menu, text="Reportes", bg=BTN_BG, fg=BTN_FG, relief='flat',
                  command=lambda: mostrar_treeview('reportes')).pack(side='left', expand=True, fill='x', padx=4)
        tk.Button(menu, text="ventas", bg=BTN_BG, fg=BTN_FG, relief="flat", 
                  command= lambda: mostrar_treeview('ventas')).pack(side ="left", expand=True, fill="x", padx=4)

        # Mostrar productos por defecto
        mostrar_treeview('productos')
        


