# El gobierno del estado de México desea reforestar un bosque que mide determinado número de
# hectáreas.
# Si la superficie del terreno excede a 1 millón de
# metros cuadrados, entonces decidirá sembrar
# de la siguiente manera:
# Porcentaje de la superficie del bosque y tipo
# de árbol: 70% pino
# 20% oyamel
# 10% cedro
# Si la superficie del terreno es menor o igual a
# un millón de metros cuadrados, entonces
# decidirá sembrar de la siguiente manera:
# Porcentaje de la superficie del bosque y tipo
# de árbol: 50% pino
# 30% oyamel
# 20% cedro
#  El gobierno desea saber el número de pinos, oyameles y cedros que tendrá que sembrar en el
# bosque, si se sabe que en 10 metros cuadrados caben 8 pinos, en 15 metros cuadrados caben 15
# oyameles y en 18 metros cuadrados caben 10 cedros. También se sabe que una hectárea equivale
# a 10 mil metros cuadrados




superficie = int(input("Ingrese los metros que desea reforestar: "))

hectareas = 10000
sup_hectareas = superficie / hectareas

if superficie > 1000000: 
    pino =  sup_hectareas * 70 / 100
    oyamel =  sup_hectareas * 20 / 100
    cedro = sup_hectareas * 10 / 100
else:
    pino = sup_hectareas * 50 / 100
    oyamel = sup_hectareas * 30 / 100
    cedro = sup_hectareas * 20 / 100

pinos = int(pino / 10 * 8)
oyameles = int(oyamel / 15 * 15)
cedros = int(cedro / 18 * 10)

    
print("pinos: ", pino, "mts2")
print("oyameles: ", oyamel, "mts2")
print("cedros: ", cedro, "mts2")
print("Se deben sembrar: ", pinos, "pinos", oyameles, "oyameles y ", cedros, "cedros.")

                   