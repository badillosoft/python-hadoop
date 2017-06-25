# _*_ coding: utf-8 _*_

persona = {
	"nombre": "Pepe",
	"edad": 28,
	"direccion": {
		"calle": "Av. Siempre Viva",
		"no_ext": "123",
		"no_int": "N/D",
		"colonia": "Condesa"
	},
	"medidas": [80, 60, 90],
	"geo_data": (80.23456, -90.123123)
}

lat, lon = persona["geo_data"]

print lat, lon

print persona["direccion"]["colonia"]