
from tkinter import *
from math import *
import math
 
#VISUALIZAR LA OPERACION EN LA PANTALLA
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
#CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
 
#LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador=("")
    input_text.set("0")
 
 
ventana=Tk()
ventana.title("CALCULADORA CIENTÍFICA")
ventana.geometry("400x700")
ventana.configure(background="SkyBlue4")
color_boton=("gray77")
 
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
 
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=20,y=60)
 
#AÑADIR BOTONES.
#CREAMOS NUESTROS BOTONES
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)

Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=240)

Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=197,y=300)
Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=300
                                                                                                              )
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)

Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt(")).place(x=17,y=420)

Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=480)
Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log(")).place(x=287,y=480)

Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)
Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=420)

Button(ventana,text="Sin",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sin")).place(x=17,y=540)
Button(ventana,text="Cos",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("cos")).place(x=107,y=540)
Button(ventana,text="Tan",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("tan")).place(x=197,y=540)
 
clear()
 
ventana.mainloop()
