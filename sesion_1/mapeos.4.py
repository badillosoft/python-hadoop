# _*_ coding: utf-8 _*_

# Se posee una lista con los pesos de diferentes personas,
# se requiere obtener la información de el peso,
# la distancia al peso medio,
# el porcentaje normalizado entre el peso mínimo y el máximo

pesos = [30, 40, 32.8, 39.3, 42.1, 37.5, 54, 38, 41, 23]

pp = float(sum(pesos)) / len(pesos)

pmin = min(pesos)
pmax = max(pesos)

def trans(p):
	dp = p - pp
	np = 100. * float(p - pmin) / (pmax - pmin)
	return {
		"weight": p,
		"dist_prom": dp,
		"norm_weight": np
	}

pesos_trans = map(trans, pesos)

f = open("report.txt", "w")

f.write("List of weights\n")
f.write("-" * 40 + "\n")
f.write("N Data: %d\n" % len(pesos))
f.write("Average: %.6f\n" % pp)
f.write("Min: %.6f\n" % pmin)
f.write("Max: %.6f\n" % pmax)
f.write("-" * 40 + "\n")

for dic in pesos_trans:
	f.write("Weight: %.6f\n" % dic["weight"])
	f.write("Distance: %.6f\n" % dic["dist_prom"])
	f.write("Relative: %.6f%%\n" % dic["norm_weight"])
	f.write("-" * 40 + "\n")

f.close()