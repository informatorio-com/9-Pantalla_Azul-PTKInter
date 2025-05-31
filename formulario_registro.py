import tkinter as tk
from tkinter import messagebox
#creamos una ventana
ventana=tk.Tk()
ventana.title("formulario de registro")
ventana.geometry("400x300")
etiqueta=tk.Label(ventana,text="Formulario de registro",font=("arial",18),background="red")
etiqueta.pack()
def registrar():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()


    if nombre and correo and contraseña:
        messagebox.showinfo("Registro exitoso", f"Nombre: {nombre}\nCorreo: {correo}")
    else:
        messagebox.showwarning("incorrecto")
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()


tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()


tk.Label(ventana, text="Contraseña").pack()
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()
botonderegistro=tk.Button(ventana,text="registrar",command=registrar)
botonderegistro.pack()
ventana.mainloop()


# Etiqueta y entrada para Nombre
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack()

# Etiqueta y entrada para Apellido
tk.Label(ventana, text="Apellido:").pack(pady=5)
entry_apellido = tk.Entry(ventana, width=30)
entry_apellido.pack()

# Etiqueta y entrada para Correo Electrónico
tk.Label(ventana, text="Correo electrónico:").pack(pady=5)
entry_correo = tk.Entry(ventana, width=30)
entry_correo.pack()

# Etiqueta y entrada para Contraseña
tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_contrasena = tk.Entry(ventana, width=30, show="*")
entry_contrasena.pack()

# Botón de registro
tk.Button(ventana, text="Registrar", command=registrar).pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
