'''Práctica Diccionarios 2 Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario. Si el valor 300 cambiara en el futuro, el código 
debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}} print(mi_dict[])'''

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}

print(mi_dict)

print(mi_dict['puntos']['points2'][1])
