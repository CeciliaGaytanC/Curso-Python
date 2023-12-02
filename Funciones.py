# La funcion puede devolver valor, parametros/argumentos, 
# Las funciones tambien llaman metodos cuando se encuentra dentro de una clase
# El objetivo de una funcion es reutilizar el codigo.
# Una funcion es capaz de no recibir ningun parametro,  o de recibir varios parametros(separados por comas)
# 
# En Python todo es referencia
# Sintaxis:
#  def function_name():      --- ():  --- Zona de parametros, dentro de los "()" van los parametros
#    Instruccion de la funcion
#  return

# "print" es una funcion ya definida por el lenguaje, lo que va dentro de (), puede ir en ""  y en ''.
# print, si vamos a imprimir texto va dentro de "" o de '', pero si vamos a imprimir una funcion no va en ninguna comilla

# Declara la funcion "mensaje"
def mensaje():

    print('Hola01') 
    print('Hola02') 
    print('Hola03')  

# Se manda llamar la funcion
mensaje()

print('Pausa')

mensaje()
mensaje()


# Practice 2
def suma():
    num1=1
    num2=7
    print(num1+num2)
suma()

def suma(num1, num2):
 
    print(num1+num2)
suma(4,4)
suma(5,5)
suma(6,6)


def suma(num1, num2):
     
    resultado=num1+num2
    return resultado
# print(suma(5,7))
muestra_resultado=suma(5,9)
print(muestra_resultado)