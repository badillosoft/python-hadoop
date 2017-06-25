# _*_ coding: utf-8 _*_

from random import choice
from random import normalvariate

nombres = ["Pepe", "Diana", "Maria", "Pablo", "Jorge"]
apellidos = ["Escobar", "Gutierrez", "Guzman", "Lopez"]

def persona_fake():
	nombre = choice(nombres)
	apellido_paterno = choice(apellidos)
	apellido_materno = choice(apellidos)

	edad = int(normalvariate(40, 10))

	if edad < 0:
		edad = 0

	escolaridad = choice(["Primaria", "Secundaria", "Prepa", "Uni"])

	return {
		"nombre": nombre,
		"apellido_paterno": apellido_paterno,
		"apellido_materno": apellido_materno,
		"nombre_completo": "%s %s %s" % (nombre, apellido_paterno, apellido_materno),
		"edad": edad,
		"escolaridad": escolaridad
	}

personas = []

for i in range(1000):
	personas.append(persona_fake())

print personas