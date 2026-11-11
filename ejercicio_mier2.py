# Café Pixel vende sándwiches y jugos por internet. Su propietaria necesita calcular el costo de un pedido,
# aplicar un descuento a los productos y agregar el valor del domicilio.
# Datos que debe solicitar el programa
# * Nombre del cliente • Precio unitario del jugo
# * Cantidad de sándwiches • Porcentaje de descuento
# * Precio unitario del sándwich • Costo fijo del domicilio
# * Cantidad de jugos

nombre_cliente = input("Ingrese nombre del cliente: ")
cantidad_sandw = int(input("Ingrese cantidad de sandwiches: "))
precio_unitario_sand = float(input("Ingrese precio del sandwiches"))
cantidad_jugos = int(input("Ingrese cantidad de jugos: "))
precio_unitario_jugo = float(input("Ingrese precio del jugo: "))
porcentaje_descuento = float(input("Ingrese porcentaje de descuento del pedido: "))
costo_fijo_domicilio = float(input("Ingrese el costo fijo del domicilio: "))

calculo_basico_sand = cantidad_sandw * precio_unitario_sand
calculo_basico_jugo = cantidad_jugos * precio_unitario_jugo
calculo_basico_pedido = calculo_basico_jugo + calculo_basico_sand

descuento = calculo_basico_pedido * porcentaje_descuento / 100

valor_total_pedido = calculo_basico_pedido + costo_fijo_domicilio - descuento

print("******************************************************")
print(f"${cantidad_sandw} sandwiches: ${calculo_basico_sand}")
print(f"${cantidad_jugos} Jugos: ${calculo_basico_jugo}")
print(f"Subtotal del pedido: ${calculo_basico_jugo}")
print(f"Valor del descuento: ${descuento}")
print(f"Costo del domicilio: ${costo_fijo_domicilio}")
print("______________________________________________________")
print(f"${nombre_cliente} Usted debe pagar: ${valor_total_pedido}")
print("******************************************************")