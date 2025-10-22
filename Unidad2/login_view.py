import tkinter as tk
from auth_controller import validar_credenciales
from tkinter import messagebox
from dashboard_view import DashboardApp

class LoginApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Inicio de sesión")
        self.root.geometry("400x300")
        self.root.resizable(False,False)
        
        #Encabezado
        tk.Label(root, text="Bienvenido al sistema", font=("Arial",16,"bold")).pack(pady=16)
        
        #Campos de texto
        tk.Label(root,text="Ingresa tu nombre de usuario ").pack()
        self.username_entry=tk.Entry(root)
        self.username_entry.pack(pady=5)
        tk.Label(root,text="Ingresa tu contraseña ").pack()
        self.password_entry=tk.Entry(root,show="*")
        self.password_entry.pack(pady=5)
        
        #Boton
        tk.Button(root, text="Iniciar sesión" , command=self.login).pack(pady=20)
        
    def login(self):
        usuario=self.username_entry.get().strip()
        password=self.password_entry.get().strip()
        if not (usuario and password):
            messagebox.showinfo(title="Ups... algo salio mal *^* ",message="Faltan datos. Favor de ingresar usuario y contraseña")
        
        if validar_credenciales(usuario,password):
            messagebox.showinfo(title="Acceso permitido",message=f"Bienvenido {usuario}")
            self.root.destroy()
            DashboardApp(usuario)
        else:
            messagebox.showerror(title="Accesso denegado",message=" tus credenciales son incorrectas")
def iniciar():    
    root=tk.Tk()
    app=LoginApp(root)
    root.mainloop()