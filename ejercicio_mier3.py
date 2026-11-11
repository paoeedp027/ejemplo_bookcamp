# Gamer Zone cobra una entrada por jugador, una tarifa por cada hora de juego y un refrigerio para cada
# visitante. El programa debe calcular el costo de la visita grupal y el valor que paga cada persona.
# Datos que debe solicitar el programa
# * Responsable de la reserva • Precio por hora y jugador
# * Número de jugadores • Precio del refrigerio por jugador
# * Precio de entrada por jugador • Porcentaje de descuento grupal
# * Horas de juego por jugador

nombre_res_reserva = input("Ingrese el nombre del responsable de la reserva: ")
cantidad_jugadores = int(input("Ingrese cantidad de jugadores: "))
precio_entrada= float(input("Ingrese precio de entrada por jugador: "))
horas_juego_jugador1 = int(input("Ingrese horas del jugador #1: "))
horas_juego_jugador2 = int(input("Ingrese horas del jugador #2: "))
horas_juego_jugador3 = int(input("Ingrese horas del jugador #3: "))
precio_hora = float(input("Ingrese el precio de la hora: "))
precio_refrigerio = float(input("Ingrese precio del refrigerio: "))
porcentaje_descuento_grup = float(input("Ingrese porcentaje de descuento grupal: "))

# calculo de horas grupales:
horas_grupales =  horas_juego_jugador1 + horas_juego_jugador2 + horas_juego_jugador3
costo_horas_grupales = horas_grupales * precio_hora
#calculo de entrada: 
costo_entrada_grup = cantidad_jugadores * precio_entrada
# calculo de refrigerio:
costo_refrigerio_grup = cantidad_jugadores * precio_refrigerio

subtotal_grupal = costo_horas_grupales + costo_entrada_grup + costo_refrigerio_grup
descuento_grupal = subtotal_grupal * porcentaje_descuento_grup / 100
total_grupal = subtotal_grupal - descuento_grupal

#Individuales: 
entrada_jugador1 = horas_juego_jugador1 * precio_hora
entrada_jugador2 = horas_juego_jugador2 * precio_hora
entrada_jugador3 = horas_juego_jugador3 * precio_hora

total_jugador1 = entrada_jugador1 + precio_entrada + precio_refrigerio
total_jugador2 = entrada_jugador2 + precio_entrada + precio_refrigerio
total_jugador3 = entrada_jugador3 + precio_entrada + precio_refrigerio

print("**********************************************************")
print(f"Encargado: {nombre_res_reserva}, Pago total grupal para {cantidad_jugadores} personas: ${total_grupal}")

print("--------- Por jugador invidual---------")
print(f"horas: {horas_juego_jugador1}, Precio de entrada: ${precio_entrada}, Precio refrigerio${precio_refrigerio}, Pago jugador #1:${total_jugador1} ")
print(f"horas: {horas_juego_jugador2}, Precio de entrada: -${precio_entrada}, Precio refrigerio: ${precio_refrigerio}, Pago jugador #2:${total_jugador2} ")
print(f"horas: {horas_juego_jugador3}, Precio de entrada: {precio_entrada}, Precio refrigerio: ${precio_refrigerio}, Pago jugador #3: ${total_jugador3} ")
print("**********************************************************")
