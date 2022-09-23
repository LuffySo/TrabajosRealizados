from asyncio.windows_events import NULL
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
raiz = Tk()
raiz.title("Aplicacion CRUD con Base de datos")
raiz.geometry("600x350")
miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()
def conexion():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute("""
        CREATE TABLE empleado(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL,
        CARGO VARCHAR(50) NOT NULL,
        SALARIO INT NOT NULL)""")
        messagebox.showinfo("CONEXION","base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION","base de datos creada exitosamente")

def eliminar():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente",title="Advertencia"):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass

def salirAplicacion():
    valor=messagebox.askquestion("Salir","Desea salir?")
    if valor=="yes":
        raiz.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def mensaje():
    Acerca='''
    Aplicacion CRUD
    Version 1
    Autor: Juan Perez
    '''
    messagebox.showinfo(title="INFORMACION",message=Acerca)

#===== Metodos CRUD ==========
def crear():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)", (datos))
        miConexion.commit()    
    except:
        messagebox.showwarning("Advertencia","Ocurrio un error al crear el registro")
        pass
    limpiarCampos()
    mostrar()

def mostrar():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM empleado")
        for fila in miCursor:
            tree.insert("",0,text=fila[0], values=(fila[1],fila[2], fila[3]))
    except:
        pass

  # ===== DibujarTabla =====
tree=ttk.Treeview(height=10,columns=('#0','#1','#2'))
tree.place(x=0, y=130)
tree.column('#0',width=100)
tree.heading('#0',text='ID', anchor=CENTER)
tree.heading('#1',text='Nombre del Empleado', anchor=CENTER)
tree.heading('#2',text='Cargo', anchor=CENTER)
tree.column('#3',width=100)
tree.heading('#3',text='Salario', anchor=CENTER)

def seleccionar(event):
    item=tree.identify('item',event.x, event.y)
    miId.set(tree.item(item,'text'))
    miNombre.set(tree.item(item,'values')[0])
    miCargo.set(tree.item(item,'values')[1])
    miSalario.set(tree.item(item,'values')[2])

tree.bind("<Double-1>",seleccionar)


def actualiza():
    miConexion = sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("UPDATE empleado SET NOMBRE=?, CARGO=?, SALARIO=? WHERE ID="+miId.get(), (datos))
        miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","Error al Actualizar")
        pass
    limpiarCampos()
    mostrar()

def borrar():
    miConexion=sqlite3.connect('base')
    miCursor=miConexion.cursor()
    try:
        if messagebox.askyesno(message="¿Desea eliminar",title="Advertencia"):
            miCursor.execute("DELETE FROM empleado WHERE ID=" + miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","Error al Eliminar")
        pass
    limpiarCampos()
    mostrar()    

 # Fin funciones, inicio de llenar ventana
menubar=Menu(raiz)
#raiz.config(menu=menubar)
menubasedat=Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear/conectar Base de Datos", command=conexion)
menubasedat.add_command(label="Eliminar Base de Datos",command=eliminar)
menubasedat.add_command(label="Salir",command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear campos",command=limpiarCampos)
ayudamenu.add_command(label="Acerca",command=mensaje)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)

e1=Entry(raiz,textvariable=miId)

L2 = Label(raiz, text="Nombre")
L2.place(x=50,y=10)
e2=Entry(raiz,textvariable=miNombre,width=50)
e2.place(x=100, y=10)

L3=Label(raiz,text="Cargo")
L3.place(x=50,y=40)
e3=Entry(raiz,textvariable=miCargo)
e3.place(x=100, y=40)

L4=Label(raiz,text="Salario")
L4.place(x=280,y=40)
e4=Entry(raiz,textvariable=miSalario, width=10)
e4.place(x=320, y=40)

L5=Label(raiz,text="Soles")
L5.place(x=390,y=40)

#===== CREAR BOTONES ===== #
b1=Button(raiz,text="Crear Registro",command=crear)
b1.place(x=50, y=90)
b2=Button(raiz,text="Modificar Registro",command=actualiza)
b2.place(x=180, y=90)
b3=Button(raiz,text="Mostrar Registro",command=mostrar)
b3.place(x=320, y=90)
b4=Button(raiz,text="Eliminar Registro",bg="red",command=borrar)
b4.place(x=450, y=90)

raiz.config(menu=menubar)

raiz.mainloop()
