def pares_impares(lista):
    pares = 0
    impares = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    return [pares, impares]