from tkinter import *

ventana = Tk()
ventana.geometry('274x328')
ventana.config(bg= "white")
ventana.resizable(0,0)
ventana.title('Calculator')

i=0
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)
	
def operacion():
	global i
	ecuacion = Resultado.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = 'ERROR'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1

def borrar_todo():
	Resultado.delete(0, END)	
	#i=0

frame = Frame(ventana, bg ='black', relief = "raised")
frame.grid(column=0, row=0, padx=6, pady=3)

Resultado = Entry(frame,bg='#9EF8E8', width=18, relief='groove', font = 'Montserrat 16',justif = 'right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

#Botones numero

Boton1 = Button(frame, text= "1", borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),relief = "raised", bg ='#999AB8',  anchor="center", command=lambda: obtener(1))  
Boton1.grid( column= 0 ,row=3, pady=1,padx=1)

Boton2 = Button(frame, text= "2", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised",bg ='#999AB8', anchor="center",command=lambda: obtener(2))  
Boton2.grid(column =1 , row=3, pady=1,padx=1)

Boton3 = Button(frame, text= "3", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised",  bg ='#999AB8', anchor="center",command=lambda: obtener(3))  
Boton3.grid(column =2, row=3, pady=1,padx=1)

Boton4 = Button(frame, text= "4",height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8', anchor="center",command=lambda: obtener(4))  
Boton4.grid( column= 0 ,row=2, pady=1,padx=1)

Boton5 = Button(frame, text= "5", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8', anchor="center",command=lambda: obtener(5))  
Boton5.grid(column =1 , row=2, pady=1,padx=1)

Boton6 = Button(frame, text= "6", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8',  anchor="center", command=lambda: obtener(6))  
Boton6.grid(column =2, row=2, pady=1,padx=1)

Boton7 = Button(frame, text= "7",height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8',  anchor="center", command=lambda: obtener(7))  
Boton7.grid( column= 0 ,row=1, pady=1,padx=3)

Boton8 = Button(frame, text= "8", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8', anchor="center", command=lambda: obtener(8))  
Boton8.grid(column =1 , row=1, pady=1,padx=1)

Boton9 = Button(frame, text= "9", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8',  anchor="center", command=lambda: obtener(9))  
Boton9.grid(column =2, row=1, pady=1,padx=1)

Boton0 = Button(frame, text= "0",height=5, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='#999AB8',  anchor="center", command=lambda: obtener(0))  
Boton0.grid( column= 0, rowspan=2, row=4, pady=1,padx=1)

#botones signo
Boton_borrar = Button(frame, text= "⌫", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='indian red',  anchor="center",command=lambda: borrar_uno())  
Boton_borrar.grid(column =3, row=1, pady=2,padx=2)

Boton_mas = Button(frame, text= "+", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='indian red',  anchor="center", command=lambda: obtener('+'))  
Boton_mas.grid(column =3, row=2, pady=2,padx=2)

Boton_menos = Button(frame, text= "-", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='indian red',  anchor="center", command=lambda: obtener('-'))  
Boton_menos.grid(column =3, row=3, pady=2,padx=2)

Boton_punto = Button(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg = 'indian red', anchor="center", command=lambda: obtener('.'))  
Boton_punto.grid(column =1 , row=4, pady=1,padx=1)

Boton_entre = Button(frame, text= "÷", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg = 'indian red',  anchor="center", command=lambda: obtener('/'))  
Boton_entre.grid(column =2, row=4, pady=1,padx=1)

Boton_por = Button(frame, text= "x", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg = 'indian red',  anchor="center", command=lambda: obtener('*'))  
Boton_por.grid(column =3, row=4, pady=2,padx=2)

Boton_igual = Button(frame, text= "=", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg = 'indian red', anchor="center", command=lambda: operacion())  
Boton_igual.grid(column =1 , row=5, pady=1,padx=1)

Boton_raiz = Button(frame, text= "√", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", bg ='indian red', anchor="center", command=lambda: obtener('**(1/2)'))  
Boton_raiz.grid(column = 2 , row=5, pady=1,padx=1)

Boton_borrar = Button(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, relief = "raised", bg = 'indian red', anchor="center", command=lambda: borrar_todo())  
Boton_borrar.grid(column =3, row=5, pady=2,padx=2)

ventana.mainloop()
