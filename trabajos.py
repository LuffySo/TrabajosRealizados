import lib2to3.pgen2.tokenize
from asyncio.windows_events import NULL
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
raiz = Tk()
raiz.title("Aplicacion de Base de datos")
raiz.geometry("600x350")
miId = StringVar
miNombre = StringVar
miCargo = StringVar
miSalario = StringVar

def conexion():
    miConexion=sqlite3.connect("base")
    miCursor.miConexion.cursor()
    try:
        miCursor.execute("""
        CREATE TABLE empleado(
        ID INTEGER PRIMARY KEY AUTOIMCREMENT,
        NOMBRE VARCHAR(50) NOT NULL,
        CARGO VARCHAR(50) NOT NULL,
        SALARIO INT NOT NULL)""")
        messagebox.showinfo("CONEXION", "base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", "error al crear base de datos")

def salirAplicacion():
    valor=messagebox.askquestion("salir","desea salir")
    if valor=="yes":
        raiz.destroy()

def mensaje():
    Acerca='''
    Aplicacion de base de datos
    version 1
    Autor E.M.V
    '''
    messagebox.showinfo(title="INFORMACION", message=Acerca)

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def mostrar():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM empleado")
        for fila in miCursor:
            tree.insert("",0,text=fila[0], values =(fila[1],fila[2],fila[3]))
    except:
               pass
def eliminar():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="los datos seran eliminados permanetemente",title="Advertencia"):
     miCursor.execute("DROP TABLE empleado")
    else:
        pass

def crear():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)",(datos))
        miConexion.commint()
    except:
        messagebox.showwarnig("Advertencia","Ocurri error al crear registro")
        pass
    limpiarCampos()
    mostrar()
# dibujar tabla
tree=ttk.Treeview(height=10,columns=('#0','#1','#2'))
tree.place(x=0,y=130)
tree.column('#0', width=180)
tree.heading('#0', text='ID', anchor=CENTER)
tree.heading('#1', text='Nombres', anchor=CENTER)
tree.heading('#2', text='Cargo', anchor=CENTER)
tree.column('#3', width=180)
tree.heading('#3', text='Salario', anchor=CENTER)

def seleccionar(event):
	item=tree.identify('item',event.x, event.y)
	miId.set(tree.item(item,'text'))
	miNombre.set(tree.item(item,'Values')[0])
	miCargo.set(tree.item(item,'Values')[1])
	miSalario.set(tree.item(item,'Values')[2])

tree.bind("<Double -1>", seleccionar)

def actualiza():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("UPDATE empleado SET NOMBRE=?, CARGO=?,SALARIO=? WHERE ID="+miId.get(),(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("advertencia","error al actualizar")
        pass
    limpiarCampos()
    mostrar()

def borrar():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        if miConexion.askyesno(message="Desea eliminar?",title="Advertencia"):
            miCursor.execute("DELETE FROM empleado WHERE ID=" + miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning("advertencia","error al borrar")
        pass
    limpiarCampos()
    mostrar()

#-----llenar ventana---
menubar=Menu(raiz)
raiz.config(menu=menubar)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/conectar BD",command=conexion)
menubasedat.add_command(label="Eliminar BD",command=eliminar)
menubasedat.add_command(label="Salir ",command=salirAplicacion)
menubar.add_cascade(label="inicio",menu=menubasedat)
ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca..",command=mensaje)
menubar.add_cascade(label="ayuda",menu=ayudamenu)

#crea botones
L1= Label(raiz, text="Id:")
L1.place(x=20, y=10)
e1=Entry(raiz,textvariable=miId)
e1.place(x=50,y=10)

L2 = Label(raiz, text="Nombres")
L2.place(x=100,y=10)
e2=Entry(raiz, textvariable=miNombre, width=50)
e2.place(x=100,y=10)

L3 = Label(raiz, text="Cargo:")
L3.place(x=50, y=40)
e3=Entry(raiz, textvariable=miCargo, width=30)
e3.place(x=100, y=40)

L4= Label(raiz, text="salario")
L4.place(x=250, y=40)
e4=Entry(raiz,textvariable=miSalario, width=15)
e4.place(x=350, y=40)

#crearbotones

b1= Button(raiz,text="crear registro", command=crear)
b1.place(x=50, y=90)

b2= Button(raiz, text="crear registro", command=actualiza)
b2.place(x=180,y=90)

b3= Button(raiz, text="crear registro", command=mostrar)
b3.place(x=320, y=90)

b4= Button(raiz, text="crear registro", bg="red", command=borrar)
b4.place(x=450, y=90)

raiz.config(menu=menubar)
raiz.mainloop()
