#TALLER NÚMERO 1:
#EJERCICIO NÚMERO 11:Calcular el salario que debe recibir una persona teniendo en cuenta lo siguiente, el
#salario básico mensual se ingresa por teclado, el número de horas extras se ingresa por
#teclado, el tipo de horas extras que puede trabajar la persona son; horas extras diurna,
#el valor de una hora extra diurna corresponde a 25% más del valor de la hora normal
#de trabajo, horas extras nocturnas el valor de una hora extra nocturna corresponde a
#35% más del valor de la hora normal de trabajo, horas extras festivas el valor de una
#hora extra festiva corresponde a 75% más del valor de la hora normal de trabajo, horas
#extras dominicales el valor de una hora extra dominica corresponde a 100% más del
#valor de la hora normal de trabajo. El número de horas extras que trabaja la persona se
#ingresan por teclado. Al trabajador le descuenta del total de lo que recibe el 4% para
#salud y el 4% para pensión. Se debe tener presente que el trabajador puede fallar uno o
#más días y si es así se debe descontar ese día(s) del salario básico. El algoritmo debe
#mostrar salario básico, total de ingresos por horas extras, descuentos y total a pagar.
#(Los días de trabajo en Colombia son 30, de 8 horas diarias.


#DATOS QUE INGRESA EL USUARIO:
salario_basico = int(input("Ingrese salario básico: "))
horas_extras_diurnas = int(input("Ingrese horas extras diurnas si tiene de lo contrario ingrese (0): "))
horas_extras_nocturnas = int(input("Ingrese horas extras nocturnas si tiene de lo contrario ingrese (0): "))
horas_extras_festivas = int(input("Ingrese horas extras festivas si tiene de lo contrario ingrese (0): "))
horas_extras_dominicales = int(input("Ingrese horas extras dominicales si tiene de lo contrario ingrese (0): "))

#CALCULO DEL VALOR DEL DÍA Y LA HORA:
valor_dia = salario_basico / 30
valor_hora = valor_dia / 8

#"""""CALCULOS DE HORAS EXTRAS:"""""

#CALCULO DE PORCENTAJE SEGÚN EL TIPO DE HORAS EXTRAS:
por_ext_diurnas = valor_hora * 25 / 100
por_ext_nocturnas = valor_hora * 35 / 100
por_ext_festivas = valor_hora * 75 / 100
por_ext_dominicales = valor_hora * 100 / 100

#SUMA DEL VALOR DE LA HORA MÁS EL PORCENTAJE(VALOR TOTAL DE LA HORA EXTRA):
total_extra_diurnas = valor_hora + por_ext_diurnas
total_extra_nocturnas = valor_hora + por_ext_nocturnas
total_extra_festivas = valor_hora + por_ext_festivas
total_extra_dominicales= valor_hora + por_ext_dominicales

#CALCULO DEL VALOR SEGÚN LAS HORAS QUE INGRESE EL USUARIO POR EL TOTAL DE LA HORA EXTRA:
calculo_ext_diurnas = horas_extras_diurnas * total_extra_diurnas
calculo_ext_nocturnas = horas_extras_nocturnas * total_extra_nocturnas
calculo_ext_festivas = horas_extras_festivas * total_extra_festivas
calculo_ext_dominicales = horas_extras_dominicales * total_extra_dominicales

#SUBTOTAL CON PORCENTAJE DE PENSIÓN Y SALUD, MÁS EL DESCUENTO DE LOS MISMOS:
subtotal_pago = salario_basico + calculo_ext_diurnas + calculo_ext_nocturnas + calculo_ext_festivas + calculo_ext_dominicales
pension = subtotal_pago * 4 / 100
salud = subtotal_pago * 4 / 100
descuento = pension + salud

#INGRESOS POR HORAS:
ingreso_horas = calculo_ext_diurnas + calculo_ext_nocturnas + calculo_ext_festivas + calculo_ext_dominicales

#PAGO FINAL:
pago_total = subtotal_pago - descuento

print("""

▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
""")
print("Su salario básico es: ", salario_basico)
print("Su ingreso por horas extras es de: ", ingreso_horas)
print("Su descuento por salud y pensión es de: ", descuento)
print("__________________________________________________________")
print("Su pago total del mes es de: ", pago_total)
