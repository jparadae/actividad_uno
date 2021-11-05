###Evaluando si es un numero,letra, decimal
numero = 1
letra = "bsdfsdf" 
decimal = 2.5

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
