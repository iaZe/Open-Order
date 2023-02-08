import sqlite3
import tkinter
import customtkinter
from sqlite3 import Error
from datetime import date

customtkinter.set_appearance_mode("dark")

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("database.db")
    except Error as error:
        print(error)
    return connection

def select(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def execute(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

class ScrollableRadiobuttonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        radiobutton = customtkinter.CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable)
        if self.command is not None:
            radiobutton.configure(command=self.command)
        radiobutton.grid(row=len(self.radiobutton_list), column=0, pady=(0, 10))
        self.radiobutton_list.append(radiobutton)

    def remove_item(self, item):
        for radiobutton in self.radiobutton_list:
            if item == radiobutton.cget("text"):
                radiobutton.destroy()
                self.radiobutton_list.remove(radiobutton)
                return

    def get_checked_item(self):
        return self.radiobutton_variable.get()

class Login(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Login")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_user = customtkinter.CTkLabel(self, text="User")
        self.label_user.grid(row=1, column=0, padx=10, pady=10)

        self.entry_user = customtkinter.CTkEntry(self)
        self.entry_user.grid(row=1, column=1, padx=10, pady=10)

        self.label_password = customtkinter.CTkLabel(self, text="Password")
        self.label_password.grid(row=2, column=0, padx=10, pady=10)

        self.entry_password = customtkinter.CTkEntry(self, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        self.button_login = customtkinter.CTkButton(self, text="Login", command=self.master.login)
        self.button_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

class Menu(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="OrderFlow")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.button_cadastrar_pedido = customtkinter.CTkButton(self, text="Cadastrar pedido", command=self.master.order_registration)
        self.button_cadastrar_pedido.grid(row=1, column=0, padx=10, pady=10)

        self.button_listar_pedidos = customtkinter.CTkButton(self, text="Listar pedidos", command=self.master.order_list)
        self.button_listar_pedidos.grid(row=2, column=0, padx=10, pady=10)

        self.button_cadastrar_cliente = customtkinter.CTkButton(self, text="Cadastrar cliente", command=self.master.client_registration)
        self.button_cadastrar_cliente.grid(row=1, column=1, padx=10, pady=10)

        self.button_listar_clientes = customtkinter.CTkButton(self, text="Listar clientes", command=self.master.client_list)
        self.button_listar_clientes.grid(row=2, column=1, padx=10, pady=10)

        self.button_contabilidade = customtkinter.CTkButton(self, text="Contabilidade")
        self.button_contabilidade.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_sair = customtkinter.CTkButton(self, text="Sair", command=quit)
        self.button_sair.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

class OrderRegistration(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.scrollable_checkbox_frame = ScrollableRadiobuttonFrame(self, width=300, item_list=self.getClients())
        self.scrollable_checkbox_frame.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        self.label_data = customtkinter.CTkLabel(self, text="Data")
        self.label_data.grid(row=1, column=0, padx=10, pady=10)

        self.entry_data = customtkinter.CTkEntry(self)
        self.entry_data.grid(row=1, column=1, padx=10, pady=10)
        self.entry_data.insert(0, date.today().strftime("%d/%m/%Y"))

        self.label_entrega = customtkinter.CTkLabel(self, text="Entrega")
        self.label_entrega.grid(row=2, column=0, padx=10, pady=10)

        self.entry_entrega = customtkinter.CTkEntry(self)
        self.entry_entrega.grid(row=2, column=1, padx=10, pady=10)
        self.entry_entrega.insert(0, date.today().strftime("%d/%m/%Y"))

        self.label_pago = customtkinter.CTkLabel(self, text="Pago")
        self.label_pago.grid(row=3, column=0, padx=10, pady=10)

        self.entry_pago = customtkinter.CTkEntry(self)
        self.entry_pago.grid(row=3, column=1, padx=10, pady=10)
        self.entry_pago.insert(0, "R$ 0,00")

        self.label_total = customtkinter.CTkLabel(self, text="Total")
        self.label_total.grid(row=4, column=0, padx=10, pady=10)

        self.entry_total = customtkinter.CTkEntry(self)
        self.entry_total.grid(row=4, column=1, padx=10, pady=10)
        self.entry_total.insert(0, "R$ 0,00")

        self.label_observacao = customtkinter.CTkLabel(self, text="Observação")
        self.label_observacao.grid(row=5, column=0, padx=10, pady=10)

        self.entry_observacao = customtkinter.CTkEntry(self)
        self.entry_observacao.grid(row=5, column=1, padx=10, pady=10)

        self.label_status = customtkinter.CTkLabel(self, text="Status")
        self.label_status.grid(row=6, column=0, padx=10, pady=10)

        self.combobox_status = customtkinter.CTkComboBox(self, values=["Confirmado", "Pago", "Entregue"])
        self.combobox_status.grid(row=6, column=1, padx=10, pady=10)

        self.button_cadastrar = customtkinter.CTkButton(self, text="Cadastrar", command=self.cadastrar_pedido)
        self.button_cadastrar.grid(row=7, column=0, padx=10, pady=10)

        self.button_voltar = customtkinter.CTkButton(self, text="Cancelar", command=self.back_menu)
        self.button_voltar.grid(row=7, column=1, padx=10, pady=10)

    def getClients(self):
        clientes = select("SELECT nome FROM clientes")
        client_list = ','.join([str(cliente[0]) for cliente in clientes]).split(',')
        return client_list

    def cadastrar_pedido(self):
        cliente = self.scrollable_checkbox_frame.get_checked_item()
        data = self.entry_data.get()
        entrega = self.entry_entrega.get()
        pago = self.entry_pago.get()
        total = self.entry_total.get()
        observacao = self.entry_observacao.get()
        status = self.combobox_status.get()
        try:
            execute("CREATE TABLE IF NOT EXISTS pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT, data TEXT, entrega TEXT, pago TEXT, total TEXT, observacao TEXT, status TEXT)")
            execute(f"INSERT INTO pedidos (cliente, data, entrega, pago, total, observacao, status) VALUES ('{cliente}', '{data}', '{entrega}', '{pago}', '{total}', '{observacao}', '{status}')")
            tkinter.messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso")
            self.master.back_menu()
        except:
            tkinter.messagebox.showerror("Error", "Erro ao cadastrar pedido")

    def back_menu(self):
        self.master.back_menu()
        self.destroy()

class OrderList(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def getPedidos():
            pedidos = select("SELECT * FROM pedidos")
            for i in pedidos:
                if i[7] == "Pago":
                    self.tv.insert("", "end", values=i, tag="paid")
                elif i[7] == "Cancelado":
                    self.tv.insert("", "end", values=i, tag="canceled")
                elif i[7] == "Entregue":
                    self.tv.insert("", "end", values=i, tag="delivered")
                elif i[7] == "Confirmado":
                    self.tv.insert("", "end", values=i, tag="confirmed")
                else:
                    self.tv.insert("", "end", values=i)
                
                self.tv.tag_configure("paid", background="#90EE90")
                self.tv.tag_configure("canceled", background="#FFA07A")
                self.tv.tag_configure("delivered", background="#87CEFA")
                self.tv.tag_configure("confirmed", background="#FFFFE0")



        self.tv=tkinter.ttk.Treeview(self, columns=(1,2,3,4,5,6,7,8), show="headings", height="5")
        self.tv.column(1, width=50, anchor='c')
        self.tv.column(2, width=100, anchor='c')
        self.tv.column(3, width=100, anchor='c')
        self.tv.column(4, width=100, anchor='c')
        self.tv.column(5, width=100, anchor='c')
        self.tv.column(6, width=100, anchor='c')
        self.tv.column(7, width=100, anchor='c')
        self.tv.column(8, width=100, anchor='c')

        self.tv.heading(1, text="ID")
        self.tv.heading(2, text="Cliente")
        self.tv.heading(3, text="Data")
        self.tv.heading(4, text="Entrega")
        self.tv.heading(5, text="Pago")
        self.tv.heading(6, text="Total")
        self.tv.heading(7, text="Observação")
        self.tv.heading(8, text="Status")
        self.tv.pack()
        getPedidos()
        self.tv.bind("<Double-1>", self.onDoubleClick)
        self.ipady()

        self.button_voltar = customtkinter.CTkButton(self, text="Voltar", command=self.back_menu)
        self.button_voltar.grid(row=1, column=0, padx=10, pady=10)

    def ipady(self):
        rows = select("SELECT ID FROM pedidos")
        if len(rows) < 11:
            self.tv.grid(row=0, column=0, ipady=60, padx=10, pady=10)
        elif len(rows) < 16:
            self.tv.grid(row=0, column=0, ipady=110, padx=10, pady=10)
        elif len(rows) < 21:
            self.tv.grid(row=0, column=0, ipady=160, padx=10, pady=10)
        elif len(rows) >= 21:
            self.tv.grid(row=0, column=0, ipady=210, padx=10, pady=10)
        

    def onDoubleClick(self, event):
        item = self.tv.identify('item', event.x, event.y)
        values = self.tv.item(item, "values")
        self.destroy()
        self.editar_pedido = OrderEdit(self.master, values)
        self.editar_pedido.grid(row=0, column=0, padx=10, pady=10)
    
    def back_menu(self):
        self.master.back_menu()
        self.destroy()

class OrderEdit(customtkinter.CTkFrame):
    def __init__(self, master, values, **kwargs):
        super().__init__(master, **kwargs)

        self.label_id = customtkinter.CTkLabel(self, text="ID")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)

        self.entry_id = customtkinter.CTkEntry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_id.insert(0, values[0])

        self.label_cliente = customtkinter.CTkLabel(self, text="Cliente")
        self.label_cliente.grid(row=0, column=0, padx=10, pady=10)

        self.entry_cliente = customtkinter.CTkEntry(self)
        self.entry_cliente.grid(row=0, column=1, padx=10, pady=10)
        self.entry_cliente.insert(0, values[1])

        self.label_data = customtkinter.CTkLabel(self, text="Data")
        self.label_data.grid(row=1, column=0, padx=10, pady=10)

        self.entry_data = customtkinter.CTkEntry(self)
        self.entry_data.grid(row=1, column=1, padx=10, pady=10)
        self.entry_data.insert(0, values[2])

        self.label_entrega = customtkinter.CTkLabel(self, text="Entrega")
        self.label_entrega.grid(row=2, column=0, padx=10, pady=10)

        self.entry_entrega = customtkinter.CTkEntry(self)
        self.entry_entrega.grid(row=2, column=1, padx=10, pady=10)
        self.entry_entrega.insert(0, values[3])

        self.label_pago = customtkinter.CTkLabel(self, text="Pago")
        self.label_pago.grid(row=3, column=0, padx=10, pady=10)

        self.entry_pago = customtkinter.CTkEntry(self)
        self.entry_pago.grid(row=3, column=1, padx=10, pady=10)
        self.entry_pago.insert(0, values[4])

        self.label_total = customtkinter.CTkLabel(self, text="Total")
        self.label_total.grid(row=4, column=0, padx=10, pady=10)

        self.entry_total = customtkinter.CTkEntry(self)
        self.entry_total.grid(row=4, column=1, padx=10, pady=10)
        self.entry_total.insert(0, values[5])

        self.label_observacao = customtkinter.CTkLabel(self, text="Observação")
        self.label_observacao.grid(row=5, column=0, padx=10, pady=10)

        self.entry_observacao = customtkinter.CTkEntry(self)
        self.entry_observacao .grid(row=5, column=1, padx=10, pady=10)
        self.entry_observacao.insert(0, values[6])

        self.label_status = customtkinter.CTkLabel(self, text="Status")
        self.label_status.grid(row=6, column=0, padx=10, pady=10)

        self.entry_status = customtkinter.CTkEntry(self)
        self.entry_status.grid(row=6, column=1, padx=10, pady=10)
        self.entry_status.insert(0, values[7])

        self.button_salvar = customtkinter.CTkButton(self, text="Salvar", command=self.salvar)
        self.button_salvar.grid(row=7, column=0, padx=10, pady=10)

        self.button_cancelar = customtkinter.CTkButton(self, text="Cancelar", command=self.cancelar)
        self.button_cancelar.grid(row=7, column=1, padx=10, pady=10)

    def salvar(self):
        id = self.entry_id.get()
        cliente = self.entry_cliente.get()
        data = self.entry_data.get()
        entrega = self.entry_entrega.get()
        pago = self.entry_pago.get()
        total = self.entry_total.get()
        observacao = self.entry_observacao.get()
        status = self.entry_status.get()
        try:
            execute(f"UPDATE pedidos SET cliente = '{cliente}', data = '{data}', entrega = '{entrega}', pago = '{pago}', total = '{total}', observacao = '{observacao}', status = '{status}' WHERE id = {id}")
            tkinter.messagebox.showinfo("Sucesso", "Pedido editado com sucesso")
        except:
            tkinter.messagebox.showerror("Erro", "Não foi possível editar o pedido")
        self.master.order_list()
        self.destroy()

    def cancelar(self):
        self.master.order_list()
        self.destroy()

class ClientRegistration(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_nome = customtkinter.CTkLabel(self, text="Nome")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = customtkinter.CTkEntry(self)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.label_telefone = customtkinter.CTkLabel(self, text="Telefone")
        self.label_telefone.grid(row=1, column=0, padx=10, pady=10)

        self.entry_telefone = customtkinter.CTkEntry(self)
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=10)

        self.label_endereco = customtkinter.CTkLabel(self, text="Endereço")
        self.label_endereco.grid(row=2, column=0, padx=10, pady=10)

        self.entry_endereco = customtkinter.CTkEntry(self)
        self.entry_endereco.grid(row=2, column=1, padx=10, pady=10)

        self.label_cidade = customtkinter.CTkLabel(self, text="Cidade")
        self.label_cidade.grid(row=3, column=0, padx=10, pady=10)

        self.entry_cidade = customtkinter.CTkEntry(self)
        self.entry_cidade.grid(row=3, column=1, padx=10, pady=10)

        self.label_estado = customtkinter.CTkLabel(self, text="Estado")
        self.label_estado.grid(row=4, column=0, padx=10, pady=10)

        self.entry_estado = customtkinter.CTkEntry(self)
        self.entry_estado.grid(row=4, column=1, padx=10, pady=10)

        self.button_salvar = customtkinter.CTkButton(self, text="Salvar", command=self.salvar)
        self.button_salvar.grid(row=5, column=0, padx=10, pady=10)

        self.button_cancelar = customtkinter.CTkButton(self, text="Cancelar", command=self.cancelar)
        self.button_cancelar.grid(row=5, column=1, padx=10, pady=10)

    def salvar(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()
        cidade = self.entry_cidade.get()
        estado = self.entry_estado.get()
        try:
            execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, telefone TEXT, endereco TEXT, cidade TEXT, estado TEXT)")
            execute(f"INSERT INTO clientes (nome, telefone, endereco, cidade, estado) VALUES ('{nome}', '{telefone}', '{endereco}', '{cidade}', '{estado}')")
            tkinter.messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso")
        except:
            tkinter.messagebox.showerror("Erro", "Não foi possível cadastrar o cliente")
        self.master.back_menu()
        self.destroy()
    
    def cancelar(self):
        self.master.back_menu()
        self.destroy()

class ClientList(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def getCliente():
            clientes = select("SELECT * FROM clientes")
            for i in clientes:
                self.tv.insert("", "end", values=i)

        self.tv=tkinter.ttk.Treeview(self, columns=(1,2,3,4,5,6), show="headings", height="5")
        self.tv.column(1, width=50, minwidth=50, stretch=tkinter.NO)
        self.tv.column(2, width=100, minwidth=100, stretch=tkinter.NO)
        self.tv.column(3, width=100, minwidth=100, stretch=tkinter.NO)
        self.tv.column(4, width=100, minwidth=100, stretch=tkinter.NO)
        self.tv.column(5, width=100, minwidth=100, stretch=tkinter.NO)
        self.tv.column(6, width=100, minwidth=100, stretch=tkinter.NO)
        self.tv.heading(1, text="ID")
        self.tv.heading(2, text="Nome")
        self.tv.heading(3, text="Telefone")
        self.tv.heading(4, text="Endereço")
        self.tv.heading(5, text="Cidade")
        self.tv.heading(6, text="Estado")
        self.tv.pack()
        getCliente()
        self.tv.bind("<Double-1>", self.onDoubleClick)
        self.tv.grid(row=0, column=0, padx=10, pady=10)
    
        self.button_voltar = customtkinter.CTkButton(self, text="Voltar", command=self.back_menu)
        self.button_voltar.grid(row=1, column=0, padx=10, pady=10)

    def onDoubleClick(self, event):
        item = self.tv.identify('item', event.x, event.y)
        values = self.tv.item(item, "values")
        self.destroy()
        self.editar_pedido = ClientEdit(self.master, values)
        self.editar_pedido.grid(row=0, column=0, padx=10, pady=10)

    def back_menu(self):
        self.master.back_menu()
        self.destroy()

class ClientEdit(customtkinter.CTkFrame):
    def __init__(self, master, values, **kwargs):
        super().__init__(master, **kwargs)

        self.label_id = customtkinter.CTkLabel(self, text="ID")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)

        self.entry_id = customtkinter.CTkEntry(self)
        self.entry_id.insert(0, values[0])
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_nome = customtkinter.CTkLabel(self, text="Nome")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = customtkinter.CTkEntry(self)
        self.entry_nome.insert(0, values[1])
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.label_telefone = customtkinter.CTkLabel(self, text="Telefone")
        self.label_telefone.grid(row=1, column=0, padx=10, pady=10)

        self.entry_telefone = customtkinter.CTkEntry(self)
        self.entry_telefone.insert(0, values[2])
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=10)

        self.label_endereco = customtkinter.CTkLabel(self, text="Endereço")
        self.label_endereco.grid(row=2, column=0, padx=10, pady=10)

        self.entry_endereco = customtkinter.CTkEntry(self)
        self.entry_endereco.insert(0, values[3])
        self.entry_endereco.grid(row=2, column=1, padx=10, pady=10)

        self.label_cidade = customtkinter.CTkLabel(self, text="Cidade")
        self.label_cidade.grid(row=3, column=0, padx=10, pady=10)

        self.entry_cidade = customtkinter.CTkEntry(self)
        self.entry_cidade.insert(0, values[4])
        self.entry_cidade.grid(row=3, column=1, padx=10, pady=10)

        self.label_estado = customtkinter.CTkLabel(self, text="Estado")
        self.label_estado.grid(row=4, column=0, padx=10, pady=10)

        self.entry_estado = customtkinter.CTkEntry(self)
        self.entry_estado.insert(0, values[5])
        self.entry_estado.grid(row=4, column=1, padx=10, pady=10)

        self.button_salvar = customtkinter.CTkButton(self, text="Salvar", command=self.salvar)
        self.button_salvar.grid(row=5, column=0, padx=10, pady=10)

        self.button_voltar = customtkinter.CTkButton(self, text="Voltar", command=self.back_menu)
        self.button_voltar.grid(row=5, column=1, padx=10, pady=10)

    def salvar(self):
        id = self.entry_id.get()
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()
        cidade = self.entry_cidade.get()
        estado = self.entry_estado.get()

        try:
            execute(f"UPDATE clientes SET nome='{nome}', telefone='{telefone}', endereco='{endereco}', cidade='{cidade}', estado='{estado}' WHERE id={id}")
            tkinter.messagebox.showinfo("Sucesso", "Cliente editado com sucesso")
            self.master.client_list()
            self.destroy()
        except:
            tkinter.messagebox.showerror("Error", "All fields are required")
        
    def back_menu(self):
        self.master.client_list()
        self.destroy()

class Aplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("OrderFlow")
        self.resizable(False, False)

        self.login = Login(self)
        self.login.grid(row=0, column=0, padx=10, pady=10)

    def login(self):
        user = self.login.entry_user.get()
        password = self.login.entry_password.get()
        try:
            result = select(f"SELECT * FROM usuarios WHERE usuario='{user}' AND senha='{password}'")
            if result != []:
                self.login.destroy()
                self.menu = Menu(self)
                self.menu.grid(row=0, column=0, padx=10, pady=10)
            else:
                tkinter.messagebox.showerror("Error", "User or password invalid")
        except:
            tkinter.messagebox.showerror("Error", "Invalid user or password")
        

    def back_menu(self):
        self.menu.destroy()
        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, padx=10, pady=10)

    def order_registration(self):
        self.menu.destroy()
        self.cadastrar_pedido = OrderRegistration(self)
        self.cadastrar_pedido.grid(row=0, column=0, padx=10, pady=10)

    def order_list(self):
        self.menu.destroy()
        self.listar_pedido = OrderList(self)
        self.listar_pedido.grid(row=0, column=0, padx=10, pady=10)
    
    def client_registration(self):
        self.menu.destroy()
        self.cadastrar_cliente = ClientRegistration(self)
        self.cadastrar_cliente.grid(row=0, column=0, padx=10, pady=10)

    def client_list(self):
        self.menu.destroy()
        self.listar_cliente = ClientList(self)
        self.listar_cliente.grid(row=0, column=0, padx=10, pady=10)

    def contabilidade(self):
        pass

app = Aplication()
app.mainloop()