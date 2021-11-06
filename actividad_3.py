###Evaluando si es un numero,letra, decimal
numero = 1
letra = "a" 
decimal = 2.5
#Agregar otras variables que contengan otros type of data
variable_booleana = True

"""estoy consultando el tipo de dato es flotante?, sino imprimo el tipo de dato"""
if type(letra) is float: 
    print('es letra')
else:
    print(f'El tipo de dato es: {type(letra)}') #imprimo el tipo de dato

"""estoy consultando el tipo de dato es string?, sino imprimo el tipo de dato"""
if type(numero) is str:   
    print('esto es un numero')  #imprimo el tipo de dato
else: 
    print(f'El tipo de dato es: {type(numero)}') 


"""Ejemplo de evaluacion de tipo de dato booleano"""
if type(variable_booleana) is int:
    print("La variable es booleana")
else:
    print(f'La variable de nombre variable_booleana es de tipo:  {type(variable_booleana)} ')    
