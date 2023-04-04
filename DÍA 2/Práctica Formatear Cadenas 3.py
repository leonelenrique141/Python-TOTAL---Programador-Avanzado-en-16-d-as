'''Práctica Formatear Cadenas 3 Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase: "Has ganado 
(puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos" En esta ocasión, la cantidad de puntos acumulados (totales) 
será igual a los puntos_anteriores más los puntos_nuevos. Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación),
es muy importante para llegar al resultado correcto. puntos_anteriores = 875 puntos_nuevos = 350'''

puntos_anteriores = 875
puntos_nuevos = 350

print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos')