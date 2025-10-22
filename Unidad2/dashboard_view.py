import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self,usuario):
        self.username=usuario
        self.root=tk.Tk()
        self.root.title(f"Bienvenido {usuario}")
        self.root.geometry("600x400")
        self.root.resizable(False,False)
        self.crear_elementos()
        self.root.mainloop()
        
    def crear_elementos(self):
        tk.Label(self.root,text=f"hola {self.username}",font=("Arial",22,"bold")).pack(pady=10)
        tk.Button(self.root,text="Ver usuarios", command=self.ver_usuarios ,width=20).pack(pady=10)
        tk.Button(self.root,text="Agregar usuarios", command=self.agregar_usuarios, width=20).pack(pady=10)
        tk.Button(self.root,text="Actualizar usuarios", command=self.actualizar_usuarios, width=20).pack(pady=10)
        tk.Button(self.root,text="Eliminar usuarios", command=self.eliminar_usuarios , width=20).pack(pady=10)
        tk.Button(self.root,text="Cerrar sesión", width=50,command=self.cerrar_sesion).pack(pady=20)
    def ver_usuarios(self):
        messagebox.showinfo("Lista de usuarios" ,"funcion")
    def agregar_usuarios(self):
        messagebox.showinfo("Agregar usuario" ,"funcion")  
    def actualizar_usuarios(self):
        messagebox.showinfo("Actualizar" ,"funcion") 
    def eliminar_usuarios(self):
        messagebox.showinfo("Eliminar usuario" ,"funcion")
    def cerrar_sesion(self):
        if messagebox.askokcancel("Antes de irte...","Estas seguro de que quieres cerrar tu sesión?"):
            self.root.destroy() 