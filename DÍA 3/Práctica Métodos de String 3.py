'''Práctica Métodos de String 3 Reemplaza en la siguiente frase: "Si la implementación es difícil de explicar, puede que sea una mala
idea." los siguientes pares de palabras: "difícil" --> "fácil" "mala" --> "buena" y muestra en pantalla la frase con ambas palabras
modificadas. Si la implementación es difícil de explicar, puede que sea una mala idea.'''

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
print(frase)

print(frase.replace("difícil", "fácil").replace("mala","buena"))