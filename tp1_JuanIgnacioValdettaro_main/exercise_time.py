def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas= int(total_segundos /(60*60))
    resto= total_segundos//(60*60)
    minutos = resto % 60
    segundos = total_segundos - (horas*3600+minutos*60)


    print(horas)
    print(minutos)
    print(segundos)


