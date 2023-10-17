# Primero se importa el módulo random para poder generar los datos de forma aleatoria:

import random 

# Luego hacemos los listados de donde el programa cogerá de forma aleatoria los datos:

listaNombres = ["Arturo","Beatriz","Carlos","Dionisio","Esteban","Francisco","Guillermo","Herminia","Irene","Juan","Karina","Lucas","Marta","Noelia","Orfelina","Pedro","Quique","Roberto","Sara","Talía","Umberto","Verónica","Willy","Xavier","Yolanda","Zulema"]

listaApellidos = ["Alegría","Balenciaga","Celdrán","Díaz","Enríquez","Fraile","Guillén","Hernández","Idiákez","Jiménez","Klein","López","Moreno","Navas","Ortega","Pérez","Quevedo","Rodríguez","Sánchez","Toledo","Ubago","Velázquez","Werner","Xátiva","Yáquez","Zapatero"]

listaCiudades = ["Ávila","Barcelona","Cádiz","Dos Hermanas","Elche","Fuenlabrada","Granada","Hellín","Irún","Jerez de la Frontera","Jerez de los Caballeros","Lugo","Madrid","Novelda","Oviedo","Pinto","Quintanar de la Orden","Ribadesella","Sevilla","Tarragona","Utrera","Valencia","Málaga","La Coruña","Yuncos","Zaragoza"]

listaProfesiones = ["Abogado","Barrendero","Celador","Conserje","Electricista","Fontanero","Guarda","Auxiliar","Intendente","Camionero","Médico","Cocinero","Enfermero","Naviero","Odontólogo","Pastelero","Quesero","Ganadero","Administrativo","Tornero","Guía","Camarero","Limpiador","Profesor","Recepcionista","Zapatero"]

# Después indicamos los datos que queremos y de que listado los tiene que coger el programa:

nombre = random.choice(listaNombres)

primerApellido = random.choice(listaApellidos)

segundoApellido = random.choice(listaApellidos)

edad = random.randint(18,65) 

profesion = random.choice(listaProfesiones)

lugarResidencia = random.choice(listaCiudades)

# Posteriormente le indicamos al programa que nos muestre en la pantalla los datos generados:

print("Nombre: " + nombre)

print("Primer apellido: " + primerApellido)

print("Segundo apellido: " + segundoApellido)

print("Edad: " + str(edad))

print("Profesión: " + profesion)

print("Lugar de residencia: " + lugarResidencia)

# Y por último... Gracias!!!

print("Gracias!!!")

