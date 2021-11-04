"""Aticivdad N°2: 
Generar metodo que capture mis datos personales
"""
#Declarando variables de formulario
atributos_formulario = ['nombre', 'apellido', 'correo', 'direccion'] #Estos son los atributos
resultados = [input('Ingresa tu nombre: '), input('Ingresa tu apellido: '), input('Ingresa tu correo: '), input('Ingresa tu direccion: ')] #Este es un arreglo que guardara todos los input del usuario ej: nombre,apellido
print(atributos_formulario) #solo estoy imprimiendo el contenido de la variable para saber que es lo que hay
print(resultados)

#es necesario hacer un bucle saber los valores de la variable de atributo_formulario
for i in atributos_formulario:
    print(i) #solo quiero saber el valor de i


