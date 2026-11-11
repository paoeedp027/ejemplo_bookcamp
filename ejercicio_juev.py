# Enunciado: En un restaurante, una familia ordena varios platos. El mesero informa el subtotal antes de impuestos.
# En tu ciudad, el IVA se cobra como un porcentaje del subtotal. Además, la familia desea dejar una propina,
# también expresada como porcentaje del subtotal. Se te pide calcular el total a pagar.

consumo = float(input("Ingrese el valor por cosumo del cliente: "))
iva = float(input("Ingrese el porcentaje del IVA: "))
porcentaje_propina = float(input('Ingrese valor en porcentaje si el cliente desea dejar propina: '))

porcentaje_iva = consumo * iva / 100
subtotal = consumo + porcentaje_iva 
propina = subtotal * porcentaje_propina / 100
total_pago = consumo + porcentaje_iva + propina

print("************CHARLOTTE PIZZERIA*****************")
print("       Descripción                valor        ")
print(f'      Consumo: ..................${consumo}   ')
print(f'      IVA: ......................%{porcentaje_iva} ')
print(f'      Propina: ..................${propina}   ')
print(f'      PAGO TOTAL: ---------------${total_pago}')
print("***********************************************") 