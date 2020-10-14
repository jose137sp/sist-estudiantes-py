from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#CREACIÓN DE LA VENTATA
app= Tk()
app.geometry ("500x300")
app.title("Listado de Estudiantes")
app.resizable(0,0)

#MENÚ DE INICIO
encabezado=Label(app, text ="Listado de Estudiantes")
encabezado.config(
    fg="white",
    bg="black",
    padx=100,
    pady=20,
    font=("Tahoma",30)  
)
encabezado.grid (row=0, column=0, columnspan=11, sticky=W)

# ACCIÓN DEL RADIOBUTTON
def marcar():
    marcado.config(text=opcion)

#AGREGAR ESTUDIANTE
def agregar():
	if(len(nomest)==5):
		top = messagebox.showerror('Error', "Se ha registrado el máximo número de estudiantes posible.")

	else:
	
			#CREAR VENTANA NUEVA
			top = Toplevel()
			top.title("Añadir estudiantes")
			top.geometry("300x205")
			#AGREGAR NOMBRE
			Label(top,text="Introduzca el nombre:").place(x=0,y=0)
			Entry(top,bd=5,bg='white',textvariable=agnom, fg='black').place(x=0,y=30)
			#AGREGAR APELLIDO
			Label(top,text="Introduzca el apellido:").place(x=0,y=60)
			Entry(top,bd=5,bg='white', textvariable=aglast, fg='black').place(x=0,y=80)
			#AGREGAR NOTA
			Label(top,text="Introduzca la nota del estudiante:").place(x=0,y=120)
			Entry(top,bd=5,bg='white', textvariable=agnota, fg='black').place(x=0,y=140)
			#BOTÓN AGREGAR
			Button(top,text= "Agregar",command=agregar2).place(x=0,y=180)
			Button(top,text= "Cerrar",command=top.destroy).place(x=60,y=180)
    
def agregar2():
	if(len(nomest)==10):
		top = messagebox.showerror('Error', "Se ha registrado el máximo número de estudiantes posible.")
	elif((agnom.get()=='') and (aglast.get()=='') and ((agnota.get()<0) or (agnota.get()>100))):
		top = messagebox.showerror('Error', "Todos los datos ingresados son inválidos.")
	elif((agnom.get()=='') and (aglast.get()=='')):
	     top = messagebox.showerror('Error', "Por favor ingrese uno o más nombres y apellidos.")
	elif(agnom.get()==''):
		top = messagebox.showerror('Error', "Por favor ingrese uno o más nombres.")
	elif(aglast.get()==''):
		top = messagebox.showerror('Error', "Por favor ingrese uno o más apellidos.")
	elif((agnota.get()<0) or (agnota.get()>100)):
		top = messagebox.showerror('Error', "La nota ingresada no se encuentra en el intervalo permitido.")
	else:
		nomest.append(agnom.get() + ' ' + aglast.get())
		notaest.append(agnota.get())
		"""print(nomest)
		print(agnom.get())
		print(len(nomest))
		print(notaest)
		print(agnota.get())
		print(len(notaest))"""

#BUSCAR ESTUDIANTE
def buscar():
	if(len(nomest)==0):
		top = messagebox.showerror('Error', "No se han ingresado estudiantes todavía.")

	else:
		top= Toplevel()
		top.title("Buscar estudiante")
		top.geometry("700x205")
		Label(top,text="Introduzca el nombre completo del estudiante por buscar:").place(x=0,y=0)
		Entry(top, bd=5,bg='white', textvariable=busnom, fg='black').place(x=0,y=30)
		Label(top, textvariable=busnota).place(x=0,y=60)
		
		#BOTÓN BUSCAR
		Button(top,text= "Buscar",command=buscar2).place(x=0,y=180)
		Button(top,text= "Cerrar",command=top.destroy).place(x=60,y=180)

def buscar2():
	control = search(nomest, busnom.get())
	if(control == 1234):
		busnota.set("El estudiante que busca no está registrado.")
		messagebox.showerror("Error", "El estudiante que busca no está registrado.")

	else:
		busnota.set("La nota del estudiante " + nomest[control] + " es " + str(notaest[control]) + ".")

def search(list, name):
	for i in range(len(list)):
		if list[i] == name:
			return i
	return 1234

#MODIFICAR NOTA
def modificar():
	if(len(nomest)==0):
		messagebox.showerror("Error", "No se han ingresado estudiantes todavía")
	else:
		top= Toplevel()
		top.title("Modificar Nota")
		top.geometry("700x205")
		Label(top, text="Introduzca el nombre completo del estudiante por cambiar de nota:").place(x=0,y=0)
		Entry(top, bd=5,bg='white', textvariable=modnom, fg='black').place(x=0,y=30)
		Label(top, text="Introduzca la nueva nota:").place(x=0,y=60)
		Entry(top, bd=5,bg='white', textvariable=modnota, fg='black').place(x=0,y=90)
		#BOTÓN BUSCAR
		Button(top,text= "Modificar",command=modificar2).place(x=0,y=140)
		Button(top,text= "Cerrar",command=top.destroy).place(x=70,y=140)

def modificar2():
	control = search(nomest, modnom.get())
	if(control == 1234):
		busnota.set("El estudiante que busca no está registrado.")
		messagebox.showerror("Error", "El estudiante que busca no está registrado.")
	elif((modnota.get()<0)) or (modnota.get()>100):
		messagebox.showerror("Error", "La nota que desea ingresar está fuera del intervalo deseado")
	else:
		v = notaest[control]
		notaest[control]=modnota.get()
		busnota.set("La nota del estudiante " + nomest[control] + " es " + str(notaest[control]) + ".")
		messagebox.showerror("Éxito", "La nota ha sido modificada exitosamente de "+str(v)+" a "+str(notaest[control])+ ".")

#LISTADO POR NOMBRE
def Lnombre():
    top= Toplevel()
    top.title("Listado por Nombre de estudiantes")
    top.geometry("900x200")
    nombres = nomest
    Label(top,text="Listado de los estudiantes por nombre: ").place(x=0,y=0)
    if (len(nomest)==0):
        messagebox.showerror("Error", "No se han registrado estudiantes")
    else:
        for i in range(len(nombres)):
            nombres.sort()
            Label(top,text=nombres).place(x=0,y=25)
    #BOTÓN ACEPTAR
    Button(top,text= "Aceptar",command=top.destroy).place(x=2,y=150)

#BUSCAR ESTUDIANTE
def Lnotas():
	if(len(nomest)==0):
		top = messagebox.showerror('Error', "No se han ingresado estudiantes todavía.")

	else:
		top= Toplevel()
		top.title("Orden por notas")
		top.geometry("700x205")
		Label(top, text = "Listado de estudiantes en orden ascendente de notas:").grid(row=0, column=0, columnspan=10)
		      
		nomcopy = nomest.copy()
		notacopy = notaest.copy()
		for i in range(len(notacopy)):
			for m in range(len(notacopy)):
				p = notacopy[m]
				q = nomcopy[m]
				if(notacopy[m] > notacopy[i]):
					notacopy[m] = notacopy[i]
					notacopy[i] = p
					nomcopy[m] = nomcopy[i]
					nomcopy[i] = q	
		print(nomcopy)
		print(notacopy)	

		for i in range(len(notacopy)):	 
			Label(top, text = nomcopy[i]).grid(row=(i+2), column=0, sticky=W)
			Label(top, text = str(notacopy[i])).grid(row=(i+2), column=1, sticky=W)


#MEDIA DE NOTAS
def media():
	if (len(notaest)==0):
		messagebox.showerror("Error", "No se han registrado estudiantes")
	else:
		top= Toplevel()
		top.title("Media de las notas")
		top.geometry("400x100")
		media1()
		Label(top,text="El valor de la media total de los estudiantes en el sistema es de:").place(x=0,y=0)
		Label(top, text=mediatotal.get()).place(x=0,y=30)
		Button(top,text= "Cerrar",command=top.destroy).place(x=0,y=60)

def media1():
	n=0
	for i in range(len(notaest)):
			n=notaest[i]+n
	media= n/len(notaest)
	mediatotal.set(media)


#ELIMINAR ESTUDIANTE
def eliminar():
	if(len(nomest)==0):
		top = messagebox.showerror('Error', "No se han ingresado estudiantes todavía.")

	else:
		top= Toplevel()
		top.title("Eliminar estudiante")
		top.geometry("500x205")
		Label(top,text="Introduzca el nombre completo del estudiante para eliminarlo:").place(x=0,y=0)
		Entry(top, bd=5,bg='white', textvariable=eliminarnom, fg='black').place(x=0,y=30)

		#BOTÓN BUSCAR
		Button(top,text= "Eliminar",command=eliminar2).place(x=0,y=180)

def eliminar2():
	control = search(nomest, eliminarnom.get())
	if(control == 1234):
		messagebox.showerror("Error", "El estudiante que busca no está registrado.")
		
	else:
		p=nomest[control]
		t=notaest[control]
		nomest.pop(control)
		notaest.pop(control)
		messagebox.showinfo("Operación exitosa", "El estudiante " + p + " con nota de " + str(t) + " ha sido eliminado exitosamente.")


def eliminar2():
	control = search(nomest, eliminarnom.get())
	if(control == 1234):
		messagebox.showerror("Error", "El estudiante que busca no está registrado.")

	else:
		t= notaest[control]
		p=nomest[control]
		notaest.pop(control)
		nomest.pop(control)
		messagebox.showerror("Éxito", "El estudiante " +p+" con nota de " + str(t) + " ha sido eliminado exitosamente")
#FUNCIONES DE CADA RADIOBUTTON
def elegir():
    if opcion.get()==1:
        agregar()
    elif opcion.get()==2:
        buscar()
    elif opcion.get()==3:
        modificar()
    elif opcion.get()==4:
        Lnombre()
    elif opcion.get()==5:
        Lnotas()
    elif opcion.get()==6:
        media()
    elif opcion.get()==7:
        eliminar()
    
#VARIABLES Y LISTAS
nomest = []
notaest = []
opcion = IntVar()

#VARIABLES PARA FUNCIÓN AGREGAR 
agnom = StringVar()
aglast = StringVar()
agnota = DoubleVar()
#VARIABLES PARA FUNCIÓN MEDIA
mediatotal =DoubleVar()
mediatotal.set(0)
#VARIABLES PARA FUNCIÓN BUSCAR
busnom = StringVar()
busnota = StringVar()
busnota.set('')
#VARIABLES PARA FUNCIÓN MODIFICAR
modnom= StringVar()
modnota=DoubleVar()
opcion.set(0)
eliminarnom= StringVar()
#CREAR LOS RADIOBUTTONS
Label(app, text="¿Qué desea realizar?", anchor =W).grid (row=2, column=0, sticky=W)

Radiobutton(app, text ="Añadir estudiantes", value=1,variable=opcion, command=marcar).grid(row=3, column=0, sticky=W)
Radiobutton(app, text ="Buscar estudiantes", value=2, variable=opcion,command=marcar).grid(row=5, column=0, sticky=W)
Radiobutton(app, text ="Modificar nota", value=3,variable=opcion, command=marcar).grid(row=6, column=0, sticky=W)
Radiobutton(app, text ="Listado de estudiantes ordenados por nombre", value=4,variable=opcion, command=marcar).grid(row=7, column=0, sticky=W)
Radiobutton(app, text ="Listado de estudiantes ordenado por notas", value=5,variable=opcion, command=marcar).grid(row=8, column=0, sticky=W)
Radiobutton(app, text ="Mostrar la media de la notas", value=6,variable=opcion, command=marcar).grid(row=9, column=0, sticky=W)
Radiobutton(app, text ="Borrar un estudiante", value=7,variable=opcion, command=marcar).grid(row=10, column=0, sticky=W)

marcado = Label(app)
boton= Button(app,text= "Aceptar",command=elegir)
boton.grid(row=12, column=0, sticky=E+W)

app.mainloop()

