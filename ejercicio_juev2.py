# Una lavandería de autoservicio tiene las siguientes tarifas fijas: lavar ropa cuesta $5 dolares por cada kilogramo de ropa y el ciclo de secado cuesta 3 dolares planos sin importar el peso. Un cliente lleva cierta cantidad de kilogramos de ropa, paga el lavado y el secado, y entrega un billete de determinada denominación.
# La máquina de cambio del negocio entrega el vuelto en monedas de $10, $5, $2 y 1dolar dolares, priorizando siempre las monedas de mayor denominación. Diseña un algoritmo que lea el peso de la ropa en kilogramos y el valor del billete entregado, calcule el costo total del servicio, calcule el cambio total, determine cuántas monedas de cada denominación se deben entregar y muestre todos los resultados.


#datos que tenemos --> 5 dolares por kg, secado 3 dolares, valor moneda 10,5,2,1
#datos que nos faltan --> peso ropa,valor billete,

#Leer el peso de la ropa
#leer el valor del billete
#costo total del servicio

#6.2
peso_ropa =  float(input("Digite el peso de la ropa en kgs "))
#50
valor_billete = int(input("Digite el valor del billete "))
#31                     6.2  *5
costo_total_lavado = peso_ropa * 5
# 34                           31
costo_total_servicio = costo_total_lavado + 3
#16          50                 34
cambio = valor_billete - costo_total_servicio
#1->10 1->5  1->1

#1             16 //10
monedas_10 =cambio // 10
#6
cambio_faltante =  cambio % 10
1
monedas_5 = cambio_faltante // 5
1
cambio_faltante_dos = cambio_faltante % 5
0
monedas_2 = cambio_faltante_dos // 2
1
cambio_faltante_tres = cambio_faltante_dos % 2
1
monedas_1 = cambio_faltante_tres // 1


print("Costo total ",costo_total_servicio)
print("Cambio ",cambio)
print("Monedas de 10 ",monedas_10)
print("Monedas de 5 ",monedas_5)
print("Monedas de 2 ",monedas_2)
print("Monedas de 1 ",monedas_1)