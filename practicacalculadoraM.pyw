from tkinter import *

raiz= Tk()
raiz.resizable(False, False)
raiz.title("Calculadora Simple")

marco=Frame(raiz)
marco.pack()

operacion= ""

resultado=0

reset_pantalla=False

#--------------------------------------------------------pantalla--------------------------------------
numeroPantalla= StringVar()


pantalla=Entry(marco, textvariable=numeroPantalla, width=30)
pantalla.grid(row=1, column=1, padx=15 ,  pady= 15, columnspan=4)
pantalla.config(background="black", fg="green", justify="right", )


#-------------------------------------------------Pulsaciones teclado--------------------------------

def PulsacionesTeclado(num):
	global operacion
	global reset_pantalla
	
	if reset_pantalla!=False:
		numeroPantalla.set(num)
		reset_pantalla=False
	else:
		numeroPantalla.set(numeroPantalla.get()+ num)


#-------------------------------------------------funciones suma--------------------------------
def suma(num):
	global operacion
	global resultado
	global reset_pantalla

	resultado+=int(num)   # resultado=resultado+ int(num)

	operacion= "suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)

#-------------------------------------------------funcion resta--------------------------------
num1=0
contador_resta=0

def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global reset_pantalla

	if contador_resta==0:
		resultado=num1-int(num)
	else:
		resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta= contador_resta+1
	operacion="resta"
	reset_pantalla=True



#-------------------------------------------------funcion multiplica--------------------------------
contador_multi=0
def multiplica(num):
	global operacion
	global resultado
	global num1
	global contador_multi
	global reset_pantalla

	if contador_multi==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*int(num)

		else:
			resultado=int(resultado)*int(num)
			numeroPantalla.set(resultado)
			resultado=numeroPantalla.get()

	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True



#------------------------------------------------- funcion divide --------------------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True

#-------------------------------------------------funcion El_resultado--------------------------------

def El_resultado():
	global resultado
	global operacion
	global operacion
	global contador_resta
	global contador_divi
	global contador_multi
	
	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0




		
		

#--------------------------------------------------------fila 2--------------------------------------
def borrarPantalla():
	global reset_pantalla
	numeroPantalla.set(0)
	reset_pantalla=True



botonBorrar=Button(marco,text="C", width=7,  command=lambda:borrarPantalla())
botonBorrar.grid(row=2, column=4 )



#--------------------------------------------------------fila 3--------------------------------------

boton7=Button(marco,text="7", width=7, command=lambda:PulsacionesTeclado("7"))
boton7.grid(row=3, column= 1)
boton8=Button(marco,text="8", width=7, command=lambda:PulsacionesTeclado("8"))
boton8.grid(row=3, column=2 )
boton9=Button(marco,text="9", width=7, command=lambda:PulsacionesTeclado("9"))
boton9.grid(row=3, column= 3)
botonDiv=Button(marco,text="/", width=7, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=3, column=4 )



#--------------------------------------------------------fila 4--------------------------------------

boton4=Button(marco,text="4", width=7, command=lambda:PulsacionesTeclado("4"))
boton4.grid(row=4, column=1 )
boton5=Button(marco,text="5", width=7, command=lambda:PulsacionesTeclado("5"))
boton5.grid(row=4, column=2 )
boton6=Button(marco,text="6", width=7, command=lambda:PulsacionesTeclado("6"))
boton6.grid(row=4, column=3 )
botonx=Button(marco,text="x", width=7, command=lambda:multiplica(numeroPantalla.get()))
botonx.grid(row=4, column=4 )

#--------------------------------------------------------fila 5--------------------------------------

boton1=Button(marco,text="1", width=7, command=lambda:PulsacionesTeclado("1"))
boton1.grid(row=5, column=1 )
boton2=Button(marco,text="2", width=7, command=lambda:PulsacionesTeclado("2"))
boton2.grid(row=5, column=2 )
boton3=Button(marco,text="3", width=7, command=lambda:PulsacionesTeclado("3"))
boton3.grid(row=5, column=3 )
botonSum=Button(marco,text="+", width=7, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4 )

#--------------------------------------------------------fila 6--------------------------------------

boton0=Button(marco,text="0", width=7, command=lambda:PulsacionesTeclado("0"))
boton0.grid(row=6, column=1 )
botonComa=Button(marco,text=",", width=7, command=lambda:PulsacionesTeclado("."))
botonComa.grid(row=6, column=2 )
botonRest=Button(marco,text="-", width=7, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=6, column=3 )
botonIgual=Button(marco,text="=", width=7, command=lambda:El_resultado())
botonIgual.grid(row=6, column=4 )



raiz.mainloop()
