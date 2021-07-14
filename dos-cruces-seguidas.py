import random

MONEDA = ['CARA','CRUZ']

def muestra(numero_intentos):
    muestra = []
    for _ in range(numero_intentos):
        lanzamientos = [random.choice(MONEDA) for _ in range(2)]
        muestra.append(lanzamientos)
    
    return muestra

if __name__ == '__main__':
    counter = 0
    numero_intentos = int(input('Numero de intentos--->'))

    muestra = muestra(numero_intentos)

    for lanzamientos in muestra:
        if ['CRUZ','CRUZ'] == lanzamientos:
            counter += 1

    dos_cruces_seguidas = counter/numero_intentos

    print(f'Probabilidad de obtener dos cruces seguidas = {dos_cruces_seguidas}')
 