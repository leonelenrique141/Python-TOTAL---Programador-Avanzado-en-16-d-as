'''programa para sacar las comisiones por ventas (13%)'''

nombre = input('Ingresa tú nombre:')
ventas = int(input('Ingresa tus ventas:'))
comision = round(ventas * 13 / 100, 2)

print(f'tus comisiones {nombre} por vender {ventas}$ en el mes son: {comision}')
